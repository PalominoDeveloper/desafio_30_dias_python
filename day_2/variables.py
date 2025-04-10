'''
    Ejercicios: Nivel 1
    Dentro de 30DaysOfPython crea una carpeta llamada day_2. Dentro de esta carpeta, cree un archivo llamado variables.py
    Escribe un comentario de python diciendo 'Día 2: 30 Días de programación de python'
    Declare una variable de nombre y asígnele un valor
    Declare una variable de apellido y asígnele un valor
    Declare una variable de nombre completo y asígnele un valor
    Declarar una variable de país y asignarle un valor
    Declarar una variable de ciudad y asignarle un valor
    Declarar una variable de edad y asignarle un valor
    Declarar una variable de año y asignarle un valor
    Declarar una variable is_married y asignarle un valor
    Declare una variable is_true y asigne un valor a ella
    Declarar una variable is_light_on y asignarle un valor
    Declarar variable múltiple en una línea
'''

#Día 2: 30 Días de programación de python

nombre = "Daniel"
apellido = "Palomino"
nombre_completo = "Daniel Palomino"
pais = "Colombia"
ciudad = "Medellín"
edad = 25
anio = 2025
esta_casado = True
es_verdadero = True
esta_luz_encendida = False
dia, mes, color_favorito, tiene_mascota = 10, 4, 'verde', True

'''
Ejercicios: Nivel 2
    1. Compruebe el tipo de datos de todas sus variables utilizando la función incorporada type()
    2. Usando el len() función incorporada, encuentre la longitud de su nombre
    3. Compare la longitud de su nombre y su apellido
    4. Declarar 5 como num_one y 4 como num_two
    5. Agregue num_one y num_two y asigne el valor a un total variable
    6. Reste num_two de num_one y asigne el valor a una variable diff
    7. Multiplique num_two y num_one y asigne el valor a un producto variable
    8. Divida num_one por num_two y asigne el valor a una división variable
    9. Use la división de módulo para encontrar num_two dividido por num_one y asigne el valor a una variable restante
    10. Calcule num_one a la potencia de num_two y asigne el valor a una variable exp
    11. Encuentre la división de piso de num_one por num_two y asigne el valor a una variable floor_division
    12. El radio de un círculo es de 30 metros.
        12.1 Calcule el área de un círculo y asigne el valor a un nombre de variable de area_of_círculo
        12.2 Calcule la circunferencia de un círculo y asigne el valor a un nombre de variable de circum_of_círculo
        12.3 Tome el radio como entrada del usuario y calcule el área.
    13. Utilice la función de entrada incorporada para obtener el nombre, apellido, país y edad de un usuario y almacenar el valor a sus nombres de variables correspondientes
    14. Ejecute help('keywords') en el shell de Python o en su archivo para verificar las palabras o palabras clave reservadas de Python
'''
print("💻 Ejercicios - Día 2", "\n")
print("Punto 1:")
print("type(nombre):", type(nombre))
print("type(apellido):", type(apellido))
print("type(nombre_completo):", type(nombre_completo))
print("type(pais):", type(pais))
print("type(ciudad):", type(ciudad))
print("type(edad):", type(edad))
print("type(anio):", type(anio))
print("type(esta_casado):", type(esta_casado))
print("type(es_verdadero):", type(es_verdadero))
print("type(esta_luz_encendida):", type(esta_luz_encendida))
print("type(dia):", type(dia))
print("type(mes):", type(mes))
print("type(color_favorito):", type(color_favorito))
print("type(tiene_mascota):", type(tiene_mascota))

print("\nPunto 2:")
print("len(nombre):", len(nombre))

print("\nPunto 3:")
print("len(nombre) > len(apellido):", len(nombre) > len(apellido))

print("\nPunto 4:")
num_one = 5
num_two = 4

print("\nPunto 5:")
total = num_one + num_two
print("total:", total)

print("\nPunto 6:")
diff = num_one - num_two
print("diff:", diff)

print("\nPunto 7:")
producto = num_one * num_two
print("producto:", producto)

print("\nPunto 8:")
division = num_one / num_two
print("division:", division)

print("\nPunto 9:")
resto = num_one % num_two
print("Módulo:", resto)

print("\nPunto 10:")
exp = num_one ** num_two
print("Exponente:", exp)

print("\nPunto 11:")
floor_division = num_one // num_two
print("División de piso:", floor_division)

print("\nPunto 12:")
radio = 30
area_of_circle = 3.14 * radio ** 2
print("Área del círculo:", area_of_circle)

print("\nPunto 12.2:")
circum_of_circle = 2 * 3.14 * radio
print("Circunferencia del círculo:", circum_of_circle)

print("\nPunto 12.3:")
radio = float(input("Ingrese el radio del círculo: "))
area_of_circle = 3.14 * radio ** 2
print("Área del círculo:", area_of_circle)

print("\nPunto 13:")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
edad = int(input("Ingrese su edad: "))

print("\nPunto 14:")
help('keywords')










