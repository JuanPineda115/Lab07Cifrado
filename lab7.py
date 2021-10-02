import random
from random import randint


#Euclides
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


#Modulo inverso
def xgcd(a, b):
    
    if b == 0:
        return 0,1,0
 
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
 
    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        #Update a,b
        a = b
        b = r
        #Update for next iteration
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
 
    return  a, u0, v0

def modInv(n, a):
   
    mcd , u , v = xgcd(n,a)
    if mcd != 1:
        print("No existe inverso")
        return 0
     
    return u%a



#Fermat
def fermat_test(n, k):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for i in range(k):
        a = random.randint(1, n-1)

        if pow(a, n-1) % n != 1:
            return False
    return True

def randomNumeros(n, k):
    p = []
    cont = 0
    range_start = 10**(n-1)
    range_end = 10**(n)-1
      
    while len(p) < k:
        n = random.randint(range_start, range_end)
        if n == 2:
          p.append(n)
        if n % 2 == 0:
          pass
        for i in range(k):
          a = random.randint(1, n-1)
          if pow(a, n-1) % n != 1:
            pass
          else:
            cont += 1        

        if cont == k:
          p.append(n)
        cont = 0
      
    return p



menuFlag = True
while menuFlag:
    option = input("1. Algoritmo de Euclides \n2. Modulo Inverso \n3. Primalidad de Fermat \n4. Generador de primos aleatorios \n5. Salir \n")
    if option == '1':
        print("\n1. Maximo divisor comun de dos numeros")

        print("\na = 1036, b = 240")
        print("El MDC es: ", euclides(1036, 240), "\n")
        print("a = 22896, b = 192 ")
        print("El MDC es: ", euclides(22896, 192), "\n")
        print("a = 689161, b = 378851")
        print("El MDC es: ", euclides(689161, 378851), "\n")
    if option == '2':
        
        print("Inverso a = 47 n = 20: ", modInv(47,2020))
        print("Inverso a = 31 b = 1234: ", modInv(31,1234))
        print("Inverso: a = 65 b = 17316:  ", modInv(65,17316))
       
    if option == '3':
        print("True = Primo |", "False = Compuesto")
        print("1317: ", fermat_test(1317, 5))
        
        print("2709: ", fermat_test(2709, 5))
        
        print("3525: ", fermat_test(3525, 5))
        
        print("3911: ", fermat_test(3911, 5))
        
        print("4279: ", fermat_test(4279, 5))
        
        print("5497: ", fermat_test(5497, 5))
        
        print("6311: ", fermat_test(8311, 5))
        
        print("7223: ", fermat_test(7223, 5))
        
        print("8431: ", fermat_test(8431, 5))
        
        print("9203: ", fermat_test(9203, 5))
        
    if option == '4':
        print(randomNumeros(7,5))
        
    if option == '5':
        menuFlag = False


    




