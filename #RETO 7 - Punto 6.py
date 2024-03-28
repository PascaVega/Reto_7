#RETO 7 - Punto 6
#Implementar un algoritmo que permita adivinar un número dado de 1 a 100, preguntando en cada caso si el número es mayor, menor o igual.
#Se importa el módulo random para que el programa escoja un número aleatorio
import random

def introducir():
    #El programa selecciona un número aleatorio entre 1 y 100
    adivinar : int = random.randint(1,100)
    print("Adivina el número")
    adivinar_numero(adivinar)

def adivinar_numero(adivinar):
    #El usuario ingresa el número que supone que es
    numero = int(input("Ingresa un numero entero: "))
    #Se crea la variable intentos
    intentos : int = 1
    #El cilo while se repetirá hasta que el número del usuario sea igual número aleatorio
    while numero != adivinar:
        #Si el número es menor al aleatorio
        if numero < adivinar:
            print("Buen intento, pero el número es mayor.")
            #El usuario ingresa otro número y se suma 1 al número de intentos
            numero = int(input("Ingresa otro número: "))
            intentos +=1
            continue
        #Si el número es mayor al aleatorio
        elif numero > adivinar:
            print("Buen intento, pero el número es menor.")
            #El usuario ingresa otro número y se suma 1 al número de intentos
            numero = int(input("Ingresa otro número: "))
            intentos +=1
            continue
    print(f"¡Felicitaciones! Adivinaste el número {adivinar} en {intentos} intentos.")
            

def continuar():
    opcion = int(input("¿Desea continuar? Marque 1 (sí) o 2 (no): "))
    return opcion

if __name__ == "__main__":
    print("Bienvenido, adivina un número entre 1 y 100.")

    while True:
        introducir()
        opcion = continuar()
        #El usuario decide si quiere volver a ejecutar ell código
        if opcion == 2:
            break
        elif opcion != 1 and 2:
            print("Error de sintaxis")
            break

# ! /\|=\/
