#Day 3 of 30 in python

#ejercicio 1
edad = 25  
estatura = 1.75  
numero_complejo = 2 + 3j  

print()

#ejercicio 2 

# Área de un triángulo
base = float(input("Ingresa la base del triángulo: "))
altura_triangulo = float(input("Ingresa la altura del triángulo: "))
area_triangulo = 0.5 * base * altura_triangulo
print("El área del triángulo es", int(area_triangulo))

print()

#ejercicio 3

# Perímetro de un triángulo
a = float(input("Ingresa el lado a: "))
b = float(input("Ingresa el lado b: "))
c = float(input("Ingresa el lado c: "))
perimetro = a + b + c
print("El perímetro del triángulo es", int(perimetro))

print()

#ejercicio 4

# Área y perímetro de un rectángulo
largo = float(input("Ingresa el largo del rectángulo: "))
ancho = float(input("Ingresa el ancho del rectángulo: "))
area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
print("Área del rectángulo:", area_rectangulo)
print("Perímetro del rectángulo:", perimetro_rectangulo)

print()

#ejercicio 5

# Área y circunferencia de un círculo
radio = float(input("Ingresa el radio del círculo: "))
pi = 3.14
area_circulo = pi * radio ** 2
circunferencia = 2 * pi * radio
print("Área del círculo:", area_circulo)
print("Circunferencia del círculo:", circunferencia)

print()

#ejercicio 6

# Ecuación de la recta y = 2x - 2
pendiente1 = 2
interseccion_x = 2 / 2  # Cuando y = 0, x = 1
interseccion_y = -2     # Cuando x = 0, y = -2
print("Pendiente:", pendiente1)
print("Intersección con el eje x:", interseccion_x)
print("Intersección con el eje y:", interseccion_y)

print()

#ejercicio 7

# Pendiente y distancia euclidiana entre dos puntos
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente2 = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1) * 2 + (y2 - y1) * 2) ** 0.5
print("Pendiente entre los puntos:", pendiente2)
print("Distancia euclidiana:", distancia)

print()

#ejercicio 8 

# Comparar pendientes
print("¿Son iguales las pendientes?", pendiente1 == pendiente2)

print()

#ejercicio 9 

# Evaluar y = x^2 + 6x + 9 y hallar x cuando y = 0
valores_x = [-3, -2, 0, 1]
for x in valores_x:
    y = x**2 + 6*x + 9
    print(f"Cuando x = {x}, y = {y}")

print()

#ejerccio 10 

# Comparar longitud de palabras
print(len("python") != len("dragon"))

print()

#ejercicio 11

# Verificar si 'on' está en ambas palabras
print('on' in 'python' and 'on' in 'dragon')

print()

#ejercicio 12

# Verificar si "jargon" está en la oración
oracion = "Espero que este curso no esté lleno de jerga."
print("jargon" in oracion)

print()

#ejercicio 13

# Afirmación falsa: no hay 'on' en python ni en dragon
print('on' not in 'dragon' and 'on' not in 'python')

print()

#ejercicio 14

# Longitud de "python" a float y a string
longitud_python = len("python")
print(float(longitud_python))
print(str(longitud_python))

print()

#ejercico 15

# Verificar si un número es par
numero = int(input("Ingresa un número para verificar si es par: "))
print(numero % 2 == 0)

print()

#ejercicio 16

# Verificar división entera
print(7 // 3 == int(2.7))

print()

#ejercicio 17

# Verificar tipos
print(type('10') == type(10))

print()

#ejercicio 18

# Verificar conversión de cadena
try:
    print(int('9.8') == 10)
except ValueError:
    print("No se puede convertir '9.8' a entero directamente.")

print()

#ejercicio 19 

# Calcular salario
horas = float(input("Ingresa las horas trabajadas: "))
tarifa = float(input("Ingresa la tarifa por hora: "))
salario = horas * tarifa
print("Tu ingreso semanal es", int(salario))

print()

#ejercico 20

# Calcular segundos vividos
años = int(input("Ingresa el número de años que has vivido: "))
segundos = años * 365 * 24 * 60 * 60
print(f"Has vivido {segundos} segundos.")

print()

#ejercicio 23

# Mostrar tabla
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")