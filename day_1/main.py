#Day 1

##Conocer la version de python 
# python --version

##Para imprimir un mensaje en la consola
print("Hello, World!")

#Operaciones matematicas
#Suma
print(f"5 + 5 = {5 + 5}")

#Resta
print(f"5 - 5 = {5 - 5}")

#Multiplicacion
print(f"5 * 5 = {5 * 5}")

#Division
print(f"5 / 5 = {5 / 5}")

#Potencia
print(f"5 ** 5 = {5 ** 5}") 

#Modulo
print(f"5 % 5 = {5 % 5}")

#Division entera
print(f"5 // 5 = {5 // 5}")

#Comentarios
#Este es un comentario de una linea

"""
Este es un comentario de 
varias lineas
"""

'''
Indentación:
    Python usa la sangría para crear bloques de código.
    Una sangría es un espacio en blanco en un texto.
'''

#Tipos de datos
'''
A.Númerico
    int: Entero
    float: Decimal
    complex: Complejo

B.Texto: Una colección de uno o más caracteres bajo una sola o doble cita.
    str: Cadena de caracteres

C.Booleano: Un tipo de dato que puede tener dos valores: True o False (1 o 0)
    bool: True o False (1 o 0)

D.Secuencial: Una secuencia de datos.
    list: Lista (La lista de Python es una colección ordenada que permite almacenar diferentes elementos de tipo de datos.)
        Ejemplo:
        lista = [1, 2, 3, 4, 5]
        print(lista)
        print(lista[0])
        print(lista[1])
        print(lista[2])
        print(lista[3])
    tuple: Tupla (La tupla de Python es una colección ordenada e inmutable que permite almacenar diferentes elementos de tipo de datos.)
        Ejemplo:
        tupla = (1, 2, 3, 4, 5)
        print(tupla)
        print(tupla[0])
        print(tupla[1])
        print(tupla[2])
        print(tupla[3])
    dict: Diccionario (El diccionario de Python es una colección desordenada que permite almacenar diferentes elementos de tipo de datos.)
        Ejemplo:
        diccionario = {"nombre": "Juan", "edad": 20, "ciudad": "Madrid"}
        print(diccionario)
        print(diccionario["nombre"])
        print(diccionario["edad"])
        print(diccionario["ciudad"])
    set: Conjunto (El conjunto de Python es una colección desordenada que permite almacenar diferentes elementos de tipo de datos.)
        Ejemplo:
        conjunto = {1, 2, 3, 4, 5}
        print(conjunto)
        print(conjunto[0])
        print(conjunto[1])
        print(conjunto[2])
        print(conjunto[3])
    range: Rango (El rango de Python es una colección ordenada que permite almacenar diferentes elementos de tipo de datos.)
        Ejemplo:
        rango = range(1, 10)
        print(rango)
        print(rango[0])
        print(rango[1])
        print(rango[2])
'''

#Mostrrar tipos de datos
print(f"El tipo de dato de 5 es: {type(5)}")
print(f"El tipo de dato de 5.5 es: {type(5.5)}")
print(f"El tipo de dato de True es: {type(True)}")
print(f"El tipo de dato de [1, 2, 3, 4, 5] es: {type([1, 2, 3, 4, 5])}")
print(f"El tipo de dato de (1, 2, 3, 4, 5) es: {type((1, 2, 3, 4, 5))}")
print(f"El tipo de dato de {{'nombre': 'Juan', 'edad': 20, 'ciudad': 'Madrid'}} es: {type({'nombre': 'Juan', 'edad': 20, 'ciudad': 'Madrid'})}")
print(f"El tipo de dato de {{1, 2, 3, 4, 5}} es: {type({1, 2, 3, 4, 5})}")
print(f"El tipo de dato de range(1, 10) es: {type(range(1, 10))}")

'''
Ejercicio 1: Hacer las siguientes operaciones con los operandos 3 y 4.
    addition(+)
    subtraction(-)
    multiplication(*)
    modulus(%)
    division(/)
    exponential(**)
    floor division operator(//)
'''
print("Ejercicio 1","\n","Operando 1: 3","\n","Operando 2: 4")

#addition(+)
print(f"Suma: {3 + 4}")

#subtraction(-)
print(f"Resta: {3 - 4}")

#multiplication(*)
print(f"Multiplicación: {3 * 4}")

#modulus(%)
print(f"Módulo: {3 % 4}")

#division(/)
print(f"División: {3 / 4}")

#exponential(**)
print(f"Potencia: {3 ** 4}")

#floor division operator(//)
print(f"División entera: {3 // 4}")


#Ejercicio 2: Encuentra un Distancia euclidiana entre (2, 3) y (10, 8).

print("Ejercicio 2","\n","Punto 2.1: (2, 3)")
print("  Distancia euclidiana entre (2, 3): ", ((3-2)**2 + (4-3)**2)**0.5)


print(" Punto 2.2: (10, 8)")
print("  Distancia euclidiana entre (10, 8): ", ((10-2)**2 + (8-3)**2)**0.5)

print("Fin del programa :D")






