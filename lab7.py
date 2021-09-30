def euclides(a, b):
    while b:
        a, b = b, a % b
    return a

menuFlag = True
while menuFlag:
    option = input("1. Algoritmo de Euclides \n2. Primalidad de Fermat \n3. Generador de primos aleatorios \n")
    if option == '1':
        print("\na = 1036, b = 240")
        print("El MDC es: ", euclides(1036, 240), "\n")
        print("a = 22896, b = 192")
        print("El MDC es: ", euclides(22896, 192), "\n")
        print("a = 689161, b = 378851")
        print("El MDC es: ", euclides(689161, 378851), "\n")