#RETO 7 - Punto 8
#Implementar el algoritmo que muestre los números primos del 1 al 100. Nota: use funciones

#Se crea una lista con todos los números primos entre el 1 y el 100
primos : list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

n: int = 0
def numero_primo(primos,n):
    #Ya que son 24 números primos, el ciclo while se repitirá 24 veces
    while n<=24:
        print(primos[n])
        n+=1
    return

#Inicia el programa
if __name__ == "__main__":
    print("Programa para conocer los numero primos del 1 al 100:")
    numero_primo(primos,n)

# ! /\|=\/
