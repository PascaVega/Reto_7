#Reto 7 - Punto 4
#En 2022 el país A tendrá una población de 25 millones de habitantes y el país B de 18.9 millones. Las tasas de crecimiento anual de la población serán de 2% y 3% respectivamente. Desarrollar un algoritmo para informar en que año la población del país B superará a la de A.

#Se definen los valores iniciales de las poblaciones y el año
a = 25000000
b = 18900000
año = 2022

if __name__ == "__main__":
    #Hasta que la población B sea igual o mayor a la población A el código continuará ejecutandose.
    while b <= a:
        #Definimos las tasas de crecimiento en valores decimales
        a = a + (a * 0.02)
        b = b + (b * 0.03)
        año = año + 1
    print(f"El año en el que la población del país B será mayor que la del país A es: {año}")

# ! /\|=\/
