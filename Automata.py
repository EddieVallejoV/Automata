from sys import stdin


def pulso(reglas, cadena):
    proxima = cadena[::]
    for i in range(len(cadena)-2):
        if (cadena[i] + cadena[i+1] + cadena[i+2]) in reglas.keys():
            proxima[i+1] = reglas[(cadena[i] + cadena[i+1] + cadena[i+2])]
    return proxima


def main():
    print("Bienvenido")
    print("Ingrese longitud del automata: ", end="")
    long_automata = int(stdin.readline().strip())
    print("Ingrese los valores del automata")
    automata = [stdin.readline().strip() for i in range(long_automata)]

    print("Ingrese el número de reglas: ", end="")
    n_reglas = int(stdin.readline().strip())
    print("Ingrese el número de pulsos: ", end="")
    pulsos = int(stdin.readline().strip())

    reglas = {}

    # Añadimos las reglas en el diccionario
    for i in range(n_reglas):
        print("Ingrese patrón de la regla #{}:".format(i+1), end=" ")
        patron = stdin.readline().strip()
        print("Ingrese resultado de la regla #{}:".format(i+1), end=" ")
        resultado = stdin.readline().strip()
        reglas[patron] = resultado

    for i in range(pulsos):
        print("Pulso {}: ".format(i), end="")
        automata = pulso(reglas, automata)
        print(" ".join(automata))


main()
