#RETO 7 - Punto 5
#Imprimir el factorial de un número natural n dado.

def introducir():
    #Se introduce el valor de a variable
    numero : int = int(input("Introduzca un numero natural para imprimir el factorial. Ejemplo: 5: "))
    desarrollo(numero)

def desarrollo(numero):
    #Definimos dos nuevas variables
    n : int = numero
    factorial : int = 1
    #Con laposibilidad de que el número sea 0 se define instantaneamente el valor del factorial
    if n == 0:
        print("El factorial de 0 es 1")
        return
    #El ciclo while continuará siempre y cuando n sea mayor a 1
    while n>1:
        factorial *= n
        n -=1
    print(f"El factorial de {numero} es {factorial}")

def continuar():
    opcion : int = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Programa para determinar el factorial de un número dado")

    while True:
        introducir()
        opcion = continuar()
        #Saber si el usuario quiere volver a ejecutar el código
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Sintax error")
            break

# ! /\|=\/
