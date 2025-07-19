#Exercises: Level 2
print("Ejercicios nivel 2:")
#Ejercicio 1
#Join A and B
print("Ejercicio 1:")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
print("La union de A Y B es:", A)



#Ejercicio 2
#Find A intersection B
print("Ejercicio 2:")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
int_a_b = A.intersection(B)
print("La interseccion de A y B es:", int_a_b)


#Ejercicio 3
#Is A subset of B
print("Ejercicio 3:")
A = {19, 22, 24, 20, 25, 26}
B ={19, 22, 20, 25, 26, 24, 28, 27}
A.issubset(B)
print("El subset de A of B es:", A.issubset(B))


#Ejercicio 4
#Are A and B disjoint sets
print("Ejercicio 4:")
A = {19, 22, 24, 20, 25, 26}
B ={19, 22, 20, 25, 26, 24, 28, 27}
A.isdisjoint(B)
print("El disjoint de A y B sets es:", A.isdisjoint(B))


#Ejercicio 5
#Join A with B and B with A
print("Ejercicio 5:")
A = {19, 22, 24, 20, 25, 26}
B ={19, 22, 20, 25, 26, 24, 28, 27}
A.update(B)
B.update(A)
print("A Y B juntos son:", A)
print("B y A juntos es:", B)



#Ejercicio 6
#What is the symmetric difference between A and B
#Delete the sets completely
print("Ejercicio 6:")
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
A.symmetric_difference(B)
print("La diferencia de simetria entre A y B es:", A.symmetric_difference(B))
del A
del B
#Esto se elimino.
