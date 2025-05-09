#Ejercicio 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

mi_lista = list(range(4, 101, 4))
print(mi_lista)

#Ejercicio 2)Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. 
# ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

mi_lista= ["Felipe","Alba","Candy","Willy","WillyII"]

print(mi_lista[3])

#Ejercicio 3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla.
#Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []

mi_lista= []
mi_lista.append("Felipe")
mi_lista.append("Alba")
mi_lista.append("WillyII")

print(mi_lista)

#Ejercicio 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. 
# Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el 
# indexing con números negativos! 

animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"  
print(animales)

#Ejercicio 5)Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. 
#La función remove elimina elementos específicos de la lista. La función max encuentra el valor máximo
#dentro de la lista y a través de remove lo elimina. 

mi_lista.remove(max(mi_lista))

#Ejercicio 6)Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 
# y mostrar por pantalla los dos primeros.

mi_lista = list(range(10,31,5))

print(mi_lista[0])
print(mi_lista[1])

#Ejercicio 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos 
# nuevos valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"]

autos =["sedan" , "polo" , "suran" , "gol"]
autos[1] = "208"
autos[-1]= "yaris"

print(autos)

#Ejercicio 8)Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. 
# Imprimir la lista resultante por pantalla.

dobles = []
dobles.append(10)
dobles.append(20)
dobles.append(30)

print(dobles)

#Ejercicio 9)Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
#compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#Agregar "jugo" a la lista del tercer cliente usando append.
#b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
#c) Eliminar "pan" de la lista del primer cliente.
#d) Imprimir la lista resultante por pantalla

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
print(compras)

compras[2].append("jugo")
print(compras)
compras[1][1]= "tallarines" #indice 1 posición 1
compras[0].remove("pan")
print("compras")

#Ejercicio 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
#● Posición lista_anidada[0]: 15
#● Posición lista_anidada[1]: True
# Posición lista_anidada[2][0]: 25.5
#Posición lista_anidada[2][1]: 57.9
#Posición lista_anidada[2][2]: 30.6
#Posición lista_anidada[3]: False
#Imprimir la lista resultante por pantalla. 

lista_anidada=[ 15, True , [25.5,57.9,30.6], False]
print(lista_anidada)