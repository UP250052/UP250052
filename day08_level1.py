#Ejercicio 1
#Create an empty dictionary called dog
print("Ejercicio 1:")
dog_empty ={}
print("dog_empty es:", dog_empty)

#Ejercicio 2
#Add name, color, breed, legs, age to the dog dictionary
print("Ejercicio 2:")
dog_empty = {"Abdell", "Azul", "breed","18"}
print(dog_empty)


#Ejercicio 3
#Create a student dictionary and add first_name, last_name, gender, age, 
#marital status, skills, country, city and address as keys for the dictionary
#Get the length of the student dictionary
print("Ejercicio 3:")
student = {
    'first_name' : 'Abdell',
    'last_name' : 'Carranza',
    'gender' : 'masculino',
    'age' : '18',
    'marital status': 'soltero',
    'skills': ['python'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address' : 'De Ladera 210 Villas de la Cantera'
            }   
print(student)  


#Ejercicio 4
#Get the length of the student dictionary  
print("Ejercicio 4:")
student = {
    'first_name' : 'Abdell',
    'last_name' : 'Carranza',
    'gender' : 'masculino',
    'age' : '18',
    'marital status': 'soltero',
    'skills': ['python'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address' : 'De Ladera 210 Villas de la Cantera'
        }
print("La longitud del diccionario student es:",len(student))




#Ejercicio 5
#Get the value of skills and check the data type, it should be a list
print("Ejercicio 5:")
skills = ['python']

print("el valor de skills es:", skills)
print(type(skills))


#Ejercicio 6
#Modify the skills values by adding one or two skills
print("Ejercicio 6:")
skills = ['python', 'JavaScript', 'Node']
print("El valor de skills es:", skills)
print(type(skills))


#Ejercicio 7
#Get the dictionary keys as a list
print("Ejercicio 7:")
student = {
    'first_name' : 'Abdell',
    'last_name' : 'Carranza',
    'gender' : 'masculino',
    'age' : '18',
    'marital status': 'soltero',
    'skills': ['python'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address' : 'De Ladera 210 Villas de la Cantera'
            }  

print("Las llaves del diccionario en lista son:", list(student.keys()))



#Ejercicio 8
#Get the dictionary values as a list
print("Ejercicio 8:")
student = {
    'first_name' : 'Abdell',
    'last_name' : 'Carranza',
    'gender' : 'masculino',
    'age' : '18',
    'marital status': 'soltero',
    'skills': ['python'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address' : 'De Ladera 210 Villas de la Cantera'
            }

print("Los valores del diccionario en lista son:",list(student.values()))


#Ejercicio 9
#Change the dictionary to a list of tuples using items() method
print("Ejercicio 9:")
student = {
    'first_name' : 'Abdell',
    'last_name' : 'Carranza',
    'gender' : 'masculino',
    'age' : '18',
    'marital status': 'soltero',
    'skills': ['python'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address' : 'De Ladera 210 Villas de la Cantera'
        }

student_items = student.items()
student_list_of_tuples = list(student_items)
print("El diccionario a lista de tuples es:", student_list_of_tuples)



#Ejercicio 10
#Delete one of the items in the dictionary
print("Ejercicio 10:")
student = {
    'first_name' : 'Abdell',
    'last_name' : 'Carranza',
    'gender' : 'masculino',
    'age' : '18',
    'marital status': 'soltero',
    'skills': ['python'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address' : 'De Ladera 210 Villas de la Cantera'
        }
student.pop('address')
print("Si eliminamos un item 'address' es:", student)




#Ejercicio 11
#Delete one of the dictionaries
print("Ejercicio 11:")
student = {
    'first_name' : 'Abdell',
    'last_name' : 'Carranza',
    'gender' : 'masculino',
    'age' : '18',
    'marital status': 'soltero',
    'skills': ['python'],
    'country': 'Mexico',
    'city': 'Aguascalientes',
    'address' : 'De Ladera 210 Villas de la Cantera'
        }

print("El diccionario se va a eliminar.")
del student

print("revisado")