#Ejercicios Nivel 1
print("Ejercicios Nivel 1:")
#Ejercicio 1
#Find the length of the set it_companies
print("Ejercicio 1:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
longitud_set = len(it_companies)
print("La longitud de set companies es:", longitud_set)

#Ejercicio 2
#Add 'Twitter' to it_companies
print("Ejercicio 2:")
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.append('Twitter')
print(it_companies)

#Ejercicio 3
#Insert multiple IT companies at once to the set it_companies
print("Ejercicio 3:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter'}
new_companies = {'Instagram', 'Tik Tok', 'WhatsAp', 'Spotify'}
it_companies.update(new_companies)
print("Las multiples companies agregadas son:", it_companies)


#Ejercicio 4
#Remove one of the companies from the set it_companies
print("Ejercicio 4:")
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Twitter', 'Instagram', 'Tik Tok', 'WhatsAp', 'Spotify'}
it_companies.remove("Facebook")
print("El conjunto de companies sin una es:", it_companies)

#Ejercicio 5
#What is the difference between remove and discard
print("Ejercicio 5:")
#Ejemplo
it_companies = {'Facebook', 'Google', 'Microsoft'}
it_companies.remove('Google') #Eliminar ggogle (funciona)
#remove : elimina el elemento del conjunto. Este es para cuando estas eguro de que este.
# si el elemento no esta genera error.
print("remove: se usa cuando estas seguro de que algo si este y poder eliminarlo")
 #Ejemplo:
it_companies = {'Facebook', 'Google', 'Microsoft'}
it_companies.discard('Google')
it_companies.discard('Tiktok') #Este no xiste en esta lista.
#discard : Este tambien elimina elementos del conjunto.
#Tambien si el elemento no se encuentra no hace nada y no marcara error, 
#lo cual es mas seguro cuando no estas seguro de si existe o no.
print("discard: se usa cuando no estas seguro y evitar errores")