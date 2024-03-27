#RETO 7 - Punto 2
#Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.

n : int = 1 #Variable para los número impares
m : int = 2 #Variable para los número pares

if __name__ == "__main__":
    #Imprimir los números impares
    print("Números impares del 1 al 999")
    while n <= 999:
        print(str(n))
        n += 2
        
    #Imprimir los números pares
    print("Números pares del 2 al 1000")
    while m <= 1000:
        print(str(m))
        m += 2

# ! /\|=\/
