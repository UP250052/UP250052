#Day 2 of 30 in python

#Exercise Level 2 

import math

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product= num_one * num_two
divison= num_one / num_two
remainder= num_one % num_two
exp = num_one ^ num_two
floor_division= num_one // num_two

radius_circle = 30
area_of_circle = math.pi * (radius_circle ** 2)
circum_of_circle = 2 * math.pi * radius_circle

print()

print("El total de la suma es: ",total)
print("El resultado de la resta es: ",diff)
print("El total de la mutltiplicacion es: ",product)
print("El total de la division es: ",divison)
print("El total de remainder es: ",remainder)
print("El total del exponenet es: ",exp)
print("El total de floor division es: ",floor_division)
print("El resultado del area del circulo es: ",radius_circle)
print("La cricunferencia del circulo es: ",circum_of_circle)

print()

user_radius_int= float(input("Introduce el radio del círculo: "))
user_area = math.pi * (user_radius_int ** 2)
print("El area del circulo es: ",user_area)

first_name = input("Introduce tu nombre: ")
last_name = input("Introduce tu apellido: ")
country = input("Introduce tu país: ")
age = int(input("Introduce tu edad: "))