#RETO 7 - Punto 1
#Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.

n : int = 1

#Iniciar el código
if __name__ == "__main__":
    print("Números del 1 al 100 con su respectivo cuadrado.")

    #Ciclo while para imprimir el listado
    while n <= 100:
        m : int = n**2
        print(str(n) , str(m))
        n += 1

# ! /\|=\/
