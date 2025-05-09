#Ejercicio 1 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

for x in range(0,101,1):
    print(x)

#Ejercicio 2 Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.

numero_entero=input("Ingrese un número entero: ")
cantidad_digitos=len(numero_entero.lstrip('-')) #me saca el signo negativo o positivo, sino lo cuenta como un dígito más
print("La cantidad de dígitos que contiene el número ingresado es : " , cantidad_digitos)


#Ejercicio 3 Escribe un programa que sume todos los números enteros comprendidos entre dos valores
#dados por el usuario, excluyendo esos dos valores.

numero1=int(input("Ingrese el primer número : "))
numero2=int(input("Ingrese el segundo número : "))

if numero1 == numero2:
    print("Los números ingresados son iguales, no hay números entre ellos para sumar.")
else:
    suma=0
    inicio=min(numero1,numero2)+1
    fin=max(numero1,numero2)
    for x in range (inicio,fin):
        suma=suma+x
    print("La sumatoria de todos los números comprendidos entre los dos valores es de : " , suma)

#Ejercicio 4 Elabora un programa que permita al usuario ingresar números enteros y los sume en
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
#un 0.

suma=0

while numero_entero != 0:
    numero_entero=int(input("Ingrese número enteros. Cuando desee finalizar presione 0 : "))
    suma +=numero_entero

print("La suma total de los número ingresados es : " , suma)

#Ejercicio 5 Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

import random

numero_aleatorio = random.randint(0, 9)
cont=0
intento=0

print("Adivine un número aleatorio entre 0 y 9")
while intento != numero_aleatorio:
        intento=int(input("Ingrese un número : " ))
        cont += 1

print("Número aleatorio entre 0 y 9:", numero_aleatorio, "Usted realizó", cont, "intentos.")

#Ejericio 6 Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
#entre 0 y 100, en orden decreciente.

for x in range (100,-1,-2):
    print(x)

#Ejercicio 7 Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario.

numero=int(input("Ingrese un número entero positivo"))

#Ejercicio 8 Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos.

conteo_pares=0
conteo_impares=0
conteo_negativos=0
conteo_positivos=0
cantidad_maxima=10 #el programa funciona para 100 números 

for numero in range (0,10,1):
    numero=int(input("Ingrese 10 números enteros, pueden ser positivos o negativos : "))

    if numero % 2 == 0:
        conteo_pares += 1
    else:
        conteo_impares += 1

    if numero < 0:
        conteo_negativos += 1
    elif numero > 0:
        conteo_positivos += 1


print("Mostrando números... ")
print("Números pares : ", conteo_pares)
print("Número impares : ", conteo_impares)
print("Números negativos : ", conteo_negativos)
print("Número positivos : ", conteo_positivos)

#Ejercicio 9 Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. 

cantidad_maxima=10
sumatoria=0

for numero in range (0,10,1):
    numero=int(input("Ingrese 10 números enteros : "))
    sumatoria+=numero 

print("La media de los valores ingresados es de : " , sumatoria/cantidad_maxima) 

#Ejercicio 10 Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
# usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero=input("Ingrese un número e invertiremos los dígitos")
