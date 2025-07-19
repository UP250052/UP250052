#Ejercicios Nivel 3
print("Ejercicios nivel 3:")

#Ejercicio 1
#Convert the ages to a set and compare the length of the list and the set, 
#which one is bigger?
print("Ejercicio 1:")
age = [22, 19, 24, 25, 26, 24, 25, 24]
ages = set(age)
print("age converido en set es:", ages)
len(age)
print("La longitud del set es:", len(ages))
len(ages)
print("La longitud de la lista es:", len(age))
if len(age) > len(ages) :
    print("La longitud de la lista es mas grande")
else : 
    print("La longitud del set es mas grande")



#Ejercicio 2
#Explain the difference between the following data types: string, list, tuple and set
print("Ejercicio 2:")
#Ejemplo string: 
#String:Definicion y se usa para representar un texto.
string = "Hola mundo"
print("El string se usa para definir un texto o de algun caracter que se va a utilizar:", string)
#Ejemplo list:
#list:Una lista ordenada de datos que puede ser de diferentes tipos.
lista = ['Frutas', 'Comida', 'Numeros', 'Edades', 'Etc']
print("La lista se usa para ordenar datos que pueden ser de distintos tipos:", lista)
#Ejemplo tuple:
#tuple:Esta es igual a la lista solo que en esta puedes editar los datos en ella.
tuple = ('Frutas', 'Comida', 'Numeros', 'Edades', 'Animales', 'Etc')
print("La funcion tuple es igual a una lista solo que esta te permite editarla cuando la estas usando", tuple)
#Ejemplo Set:
#set:Esta funcion se usa cuando los elementos son desordenados y para unirlos ya sean de listas o tuples.
set = {'Frutas', 'Comida', 'Numeros', 'Edades', 'Animales', 'Etc'}
print("La funcion set se utiliza para elementos desordenados y que se pueden unir o etc:", set)



#Ejercicio 3
#I am a teacher and I love to inspire and teach people. 
#How many unique words have been used in the sentence? 
#Use the split methods and set to get the unique words.
print("Ejercicio 3:")
sentence = "I am a teacher and I love to inspire and teach people."
spWord = sentence.split()
print("Las palabras unicas son:", len(sentence))
print("Las palabras unicas son:", spWord)



print("revisado")