#Exercises: Level 2
print("Ejercicios nivel 2:")

#Ejercicio 1
#Unpack siblings and parents from family_members
print("Ejercicio 1:")
family_members ='Junior', 'Felipe', 'Daniel', 'Veronica', 'Mama Evelia', 'Papa Hector'
print("Los hermanos son:",family_members[:4])
print("Los padres son:", family_members[4:])


#Ejercicio 2
#Create fruits, vegetables and animal products tuples. 
#Join the three tuples and assign it to a variable called food_stuff_tp.
print("Ejercicio 2:")
frutas =  "Fresa", "Sandia", "Manzana", "Melon","Naranja" 
vegetales = "Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria"  
productos_animal = "Leche", "Huevos","Queso"
food_stuff_tp = frutas + vegetales + productos_animal
print( "la variable food_stuff_tp:", food_stuff_tp)



#Ejercicio 3
#Change the about food_stuff_tp tuple to a food_stuff_lt list
print("Ejercicio 3:")
food_stuff_tp = "Fresa", "Sandia", "Manzana", "Melon","Naranja","Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria", "Leche", "Huevos","Queso"
food_stuff_lt = list(food_stuff_tp)
print( "La food_stuff_lt es:",  food_stuff_lt)


#Ejercicio 4
#Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
print("Ejercicio 4:")
food_stuff_tp = ("Fresa", "Sandia", "Manzana", "Melon","Naranja","Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria", "Leche", "Huevos","Queso")
food_stuff_lt = list(food_stuff_tp)
longitud = len(food_stuff_tp)
items_middle_tp = food_stuff_tp[(longitud - 1) //2 :  longitud // 2 + 1]
items_middle_lt = food_stuff_lt[(longitud - 1) // 2 : longitud // 2 + 1]
print("Los items del miedo en el tuple son:", items_middle_tp)
print("Los items del medio en el list son:", items_middle_lt)

#Ejercicio 5
#Slice out the first three items and the last three items from food_staff_lt list
print("Ejercicio 5:")
food_stuff_lt = ("Fresa", "Sandia", "Manzana", "Melon","Naranja","Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria", "Leche", "Huevos","Queso")
longitud = len(food_stuff_lt)
primeros_tres_items = food_stuff_lt[:3]
ultimos_tres_items = food_stuff_lt[-3:]
print("Los primeros tres items son:", primeros_tres_items)
print("Los ultimos tres elementos son:", ultimos_tres_items)

#Ejercicio 6
#Delete the food_staff_tp tuple completely
print("Ejercicio 6:")
food_stuff_lt = ("Fresa", "Sandia", "Manzana", "Melon","Naranja","Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria", "Leche", "Huevos","Queso")
del food_stuff_lt
print("Se elimino food_stuff_lt, si se usa despues causara error")


#Ejercicio 7
#Check if an item exists in tuple:
print("Ejercicio 7: ")
food_stuff_tp = ("Fresa", "Sandia", "Manzana", "Melon","Naranja","Lechuga", "Limon", "Cebolla", "Brocoli","Zanahoria", "Leche", "Huevos","Queso")
item_exitente = "Cereza"
if item_exitente in food_stuff_tp:
    print("Cereza esta en:", food_stuff_tp)
else: 
    print("Cereza no esta")
    

#Ejercicio 8
#Check if 'Estonia' is a nordic country
print("Ejercicio 8: ")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in  nordic_countries:
    print('Estonia esta en:', nordic_countries('Estonia'))
else: 
    print('No esta')
print("'Estonia' no esta")

#Ejercicio 9
#Check if 'Iceland' is a nordic country
print("Ejercicio 9:")
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Iceland' in nordic_countries:
    print('Iceland esta en nordic_countries')
else:
    print ('No esta')
print("Iceland si esta.")

print("revisado")