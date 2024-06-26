#RETO 7 - Punto 3
#Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado

def introducir():
    #Se introduce el número de la variable
    n : int = int(input("Introduzca un numero natural mayor o igual a 2: "))
    desarrollo(n)

def desarrollo(n):
    #Repetir el código hasta que el número sea 2
    while n>=2:
        #Si el número es divisible en 2 imprimirlo
        if n%2==0:
            print(str(n))
            n -=2
        #Sino restarle 1
        else:
            n = n-1

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

#Iniciar el código
if __name__ == "__main__":
    print("Ingrese un número natural para obtener los números pares descendentes hasta 2")

    while True:
        introducir()
        #Saber si el usuario quiere volver a ejecutar el código
        opcion = continuar()
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
