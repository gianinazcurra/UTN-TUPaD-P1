#Ejercicio 1

def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa pcpal
if __name__ == "__main__":
    imprimir_hola_mundo()

#Ejercicio 2

def saludar_usuario(nombre):
    print(f"Hola {nombre} !")

#Programa pcpal

if __name__ == "__main__":
    nombre=input("Ingrese su nombre : ")
saludar_usuario(nombre)

#Ejercicio 3

def informacion_personal(nombre,apellido,edad,residencia) : 
    print(f"Su nombre es {nombre} , su apellido es {apellido} , su edad es {edad} años y vive en {residencia}")

#Programa pcpal

if __name__ == "__main__":
    nombre=input("Hola, ingrese su nombre : ")
    apellido=input("Ingrese su apellido : ")
    edad=int(input("Ingrese su edad : "))
    residencia=input("Diganos su lugar de residencia : ")

informacion_personal(nombre,apellido,edad,residencia)

#Ejercicio 4

import math

def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area 

def calcular_perimetro_circulo(radio): 
    perimetro = 2 * math.pi * radio
    return perimetro

#Programa pcpal

if __name__ == "__main__": 
    radio=float(input("Ingrese el radio de un círculo : "))
    area=calcular_area_circulo(radio)
    perimetro=calcular_perimetro_circulo(radio)
    print(f"El área del círculo es {area} mientras que el perímetro es {perimetro} ")

#Ejercicio 5

def segundos_a_horas(segundos) :
    return segundos/3600

#Programa pcpal

if __name__ == "__main__": 
    segundos=int(input("Ingrese una cantidad de segundos para convertirlos a su equivalente en horas : "))
    conversion=segundos_a_horas(segundos)

    print(f"La cantidad de segundos ingresada corresponde a {conversion:.2f} horas. ")

#Ejercicio 6

def tabla_multiplicar(numero):
    for i in range (1,11):
        print(f"{numero} x {i}= {numero*i}")

#Programa pcpal

if __name__ == "__main__": 
    numero=int(input("Ingrese un número para realizar su tabla de multiplicar "))

    tabla_multiplicar(numero)

#Ejercicio 7

def operaciones_basicas(a,b):
    suma= a+b
    resta= a-b
    multiplicacion= a*b
    division= a/b

    return (suma,resta,multiplicacion,division)

#Programa pcpal

if __name__ == "__main__": 
    a=int(input("Ingrese el primer número : "))
    b=int(input("Ingrese el segundo número : "))

    resultados=operaciones_basicas(a,b)
    print(f"Suma = {resultados[0]}")
    print(f"Resta = {resultados[1]}")
    print(f"Multiplicación = {resultados[2]}")
    print(f"División = {resultados[3]}")

    #Ejercicio 8
def calcular_imc(peso,altura):
    return peso/altura **2

#Programa pcpal
if __name__ == "__main__": 
    peso=float(input("Ingrese su peso en kg. : "))
    altura=float(input("Ingrese su altura en mts. : "))

    imc=calcular_imc(peso,altura)
    print(f"Su índice de masa corporal es {imc:.2f}")

    #Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return(celsius * 9/5) + 32

#Programa pcpal
if __name__ == "__main__": 
    celsius=float(input("Ingrese la temperatura en grados Celsius : "))
    resultado=celsius_a_fahrenheit(celsius)

    print(f"La temperatura en grados Celsius ingresada equivale a {resultado:.2f} en grados Fahrenheit")

    #Ejercicio 10

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# Programa principal
if __name__ == "__main__": 
    a = float(input("Ingrese la primera nota: "))
    b = float(input("Ingrese la segunda nota: "))
    c = float(input("Ingrese la tercera nota: "))
    
    promedio = calcular_promedio(a, b, c)

    print(f"El promedio de las notas ingresadas es de: {promedio:.2f}")
