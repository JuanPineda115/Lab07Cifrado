def euclides(a, b):
    if a == 0 :
        return b
    return euclides(b%a, a)

def extEuclid(a, b):
    if a == 0 :  
        return b,0,1
    gcd,x1,y1 = extEuclid(b%a, a)
    x = y1 - (b//a) * x1 
    y = x1
    return gcd,x,y

menuFlag = True
while menuFlag:
    option = input("1. Algoritmo de Euclides \n2. Primalidad de Fermat \n3. Generador de primos aleatorios \n4. Salir \n")
    if option == '1':
        print("\n1. Maximo divisor comun de dos numeros")

        print("\na = 1036, b = 240")
        print("El MDC es: ", euclides(1036, 240), "\n")
        print("a = 22896, b = 192 ")
        print("El MDC es: ", euclides(22896, 192), "\n")
        print("a = 689161, b = 378851")
        print("El MDC es: ", euclides(689161, 378851), "\n")
    if option == '2':
        menuFlag = False
    if option == '3':
        menuFlag = False
    if option == '4':
        menuFlag = False
