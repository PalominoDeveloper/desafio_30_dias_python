#Día 3

'''
Datos booleanos: 
     representa uno de los dos valores: Verdadero o Falso
'''

'''
-OPERADORES-

Operadores de Asignación:  
    se utilizan para asignar valores a variables. 
'''
#Igual
x = 1; #Se asigna el valor de la derecha hacía la izquierda, en este caso una variable
print(f"x = 1: {x}")
#Suma
x += 1; #x = x + 1
print(f"x += 1: {x}")
#Resta
x -= 1; #x = x - 1
print(f"x -= 1: {x}")
#Multiplicación
x *= 2; #x = x * 2
print(f"x *= 2: {x}")
#División
x /= 2; #x = x / 2
print(f"x /= 2: {x}")

#Declar dos variables y asigna valores a cada una
a = 10
b = 20

suma = a + b
#Imprime el resultado de la suma de las dos variables
print(f"a + b: {suma}")

resta = a - b
#Imprime el resultado de la resta de las dos variables
print(f"a - b: {resta}")

multiplicacion = a * b  
#Imprime el resultado de la multiplicación de las dos variables
print(f"a * b: {multiplicacion}")

division = a / b
#Imprime el resultado de la división de las dos variables
print(f"a / b: {division}") 

#Comencemos a lo antes visto haciendo uso de lo que ya sabemos calcular (área, volumen, densidad, peso, perímetro, distancia, fuerza).

#Área
area = a * b
#Imprime el resultado de la área de las dos variables
print(f"a * b: {area}")

#Volumen
volumen = a * b * c
#Imprime el resultado del volumen de las tres variables
print(f"a * b * c: {volumen}")

#Densidad
densidad = a / b
#Imprime el resultado de la densidad de las dos variables
print(f"a / b: {densidad}")


print("Operadores de Comparación")

#Igual
igual = a == b
#Imprime el resultado de la comparación de las dos variables
print(f"a == b: {igual}")   

#Distinto
distinto = a != b
#Imprime el resultado de la comparación de las dos variables
print(f"a != b: {distinto}")    

#Mayor que
mayor = a > b
#Imprime el resultado de la comparación de las dos variables
print(f"a > b: {mayor}")    

#Menor que
menor = a < b
#Imprime el resultado de la comparación de las dos variables
print(f"a < b: {menor}")        

'''
Además de los operadores de comparación anteriores, Python utiliza:
    is: Devuelve true si ambas variables son el mismo objeto (x is y)
    is not: Devuelve true si ambas variables no son el mismo objeto (x is not y)
    in: Devuelve True si la lista consultada contiene un cierto elemento (x in y)
    not in: Devuelve True si la lista consultada no tiene un cierto elemento (x in y)

    Ejemplo:
'''

print('1 is 1', 1 is 1)                   # True - porque los valores son iguales
print('1 is not 2', 1 is not 2)           # True - porque 1 no es 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A encontrado en la cadena
print('B in Asabeneh', 'B' in 'Asabeneh') # False - no hay mayúscula B
print('coding' in 'coding for all') # True - porque coding for all tiene la palabra coding
print('a in an:', 'a' in 'an')      # True - a encontrado en an
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True - 4 es igual a 2 elevado a la 2

#Operadores Lógicos

#and    
print('True and False:', True and False) # False - porque uno de los dos valores es False
print('True and True:', True and True)   # True - porque ambos valores son True

#or
print('True or False:', True or False) # True - porque uno de los dos valores es True
print('False or False:', False or False) # False - porque ambos valores son False

#not
print('not True:', not True) # False - porque el valor es True
print('not False:', not False) # True - porque el valor es False


#Ejercicios - Día 3
'''
    1. Declare su edad como variable entera
    2. Declare su altura como una variable de flotador
    3. Declare una variable que almacene un número complejo
    4. Escribe un script que pida al usuario que ingrese la base y 
        la altura del triángulo y calcule un área de este triángulo (área = 0.5 x b x h).
    5. Escribe un script que pida al usuario que ingrese el lado a, 
        el lado b y el lado c del triángulo. Calcule el perímetro del triángulo (perímetro = a + b + c).
'''

#Declara tu edad como variable entera
edad = 25
print(f"Edad: {edad}")

#Declara tu altura como una variable de flotador
altura = 1.68
print(f"Altura: {altura}")

#Declara una variable que almacene un número complejo
numero_complejo = 2 + 3j
print(f"Número complejo: {numero_complejo}")

#Escribe un script que pida al usuario que ingrese la base y 
#la altura del triángulo y calcule un área de este triángulo (área = 0.5 x b x h).

base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))

area = 0.5 * base * altura
print(f"El área del triángulo es: {area}")

#Escribe un script que pida al usuario que ingrese el lado a, 
#el lado b y el lado c del triángulo. Calcule el perímetro del triángulo (perímetro = a + b + c).

lado_a = float(input("Ingrese el lado a del triángulo: "))
lado_b = float(input("Ingrese el lado b del triángulo: "))
lado_c = float(input("Ingrese el lado c del triángulo: "))

perimetro = lado_a + lado_b + lado_c
print(f"El perímetro del triángulo es: {perimetro}")

#Punto 6: Calcular área y perímetro de un rectángulo
print("\nPunto 6:")
largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
print(f"El área del rectángulo es: {area_rectangulo}")
print(f"El perímetro del rectángulo es: {perimetro_rectangulo}")

#Punto 7: Calcular área y circunferencia de un círculo
print("\nPunto 7:")
radio = float(input("Ingrese el radio del círculo: "))
pi = 3.14

area_circulo = pi * radio * radio
circunferencia = 2 * pi * radio
print(f"El área del círculo es: {area_circulo}")
print(f"La circunferencia del círculo es: {circunferencia}")

#Punto 8: Calcular pendiente, x-intercept e y-intercept de y = 2x -2
print("\nPunto 8:")
# y = 2x - 2
# Para x-intercept, y = 0: 0 = 2x - 2 => x = 1
# Para y-intercept, x = 0: y = -2
pendiente = 2
x_intercept = 1
y_intercept = -2

print(f"Pendiente: {pendiente}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

#Punto 9: Calcular pendiente y distancia euclidiana entre (2, 2) y (6,10)
print("\nPunto 9:")
x1, y1 = 2, 2
x2, y2 = 6, 10

pendiente2 = (y2 - y1)/(x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f"Pendiente: {pendiente2}")
print(f"Distancia euclidiana: {distancia}")

#Punto 10: Comparar pendientes
print("\nPunto 10:")
print(f"¿Las pendientes son iguales?: {pendiente == pendiente2}")

#Punto 11: Calcular y = x^2 + 6x + 9 para diferentes valores de x
print("\nPunto 11:")
def calcular_y(x):
    return x**2 + 6*x + 9

# Probando diferentes valores de x
for x in range(-5, 6):
    y = calcular_y(x)
    print(f"Para x = {x}, y = {y}")
    if y == 0:
        print(f"¡y es igual a 0 cuando x = {x}!")

#Punto 12: Comparar longitudes de 'python' y 'dragon'
print("\nPunto 12:")
len_python = len('python')
len_dragon = len('dragon')
print(f"¿'python' y 'dragon' tienen la misma longitud?: {len_python == len_dragon}")

#Punto 13: Verificar si 'on' está en 'python' y 'dragon'
print("\nPunto 13:")
print(f"¿'on' está en 'python'?: {'on' in 'python'}")
print(f"¿'on' está en 'dragon'?: {'on' in 'dragon'}")

#Punto 14: Verificar si 'jerga' está en la frase
print("\nPunto 14:")
frase = "Espero que este curso no esté lleno de jerga"
print(f"¿'jerga' está en la frase?: {'jerga' in frase}")

#Punto 15: Verificar que no hay 'on' en 'dragón' y 'pitón'
print("\nPunto 15:")
print(f"¿No hay 'on' en 'dragón'?: {'on' not in 'dragón'}")
print(f"¿No hay 'on' en 'pitón'?: {'on' not in 'pitón'}")

#Punto 16: Convertir longitud de 'python' a float y luego a string
print("\nPunto 16:")
longitud = len('python')
longitud_float = float(longitud)
longitud_str = str(longitud_float)
print(f"Longitud como float: {longitud_float}")
print(f"Longitud como string: {longitud_str}")

#Punto 17: Verificar si un número es par
print("\nPunto 17:")
numero = int(input("Ingrese un número para verificar si es par: "))
es_par = numero % 2 == 0
print(f"¿El número {numero} es par?: {es_par}")

#Punto 18: Verificar división de piso
print("\nPunto 18:")
division_piso = 7 // 3
valor_convertido = int(2.7)
print(f"¿La división de piso de 7/3 es igual a int(2.7)?: {division_piso == valor_convertido}")

#Punto 19: Verificar tipos
print("\nPunto 19:")
print(f"¿El tipo de '10' es igual al tipo de 10?: {type('10') == type(10)}")

#Punto 20: Verificar conversión
print("\nPunto 20:")
try:
    print(f"¿int('9.8') es igual a 10?: {int(float('9.8')) == 10}")
except ValueError:
    print("No se puede convertir '9.8' directamente a entero")

#Punto 21: Calcular pago
print("\nPunto 21:")
horas = float(input("Ingrese las horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))
pago = horas * tarifa
print(f"Su pago es: {pago}")

#Punto 22: Calcular segundos de vida
print("\nPunto 22:")
años = int(input("Ingrese el número de años: "))
segundos = años * 365 * 24 * 60 * 60
print(f"Una persona que vive {años} años vivirá aproximadamente {segundos} segundos")

#Punto 23: Mostrar tabla
print("\nPunto 23:")
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")


