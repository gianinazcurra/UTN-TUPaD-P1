#ejercicio1
print("Hola mundo!")

#ejercicio2
nombre=input("ingrese su nombre")
print(f"Hola {nombre}")

#ejericio3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su país de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años, y vivo en {pais}.")

#ejercicio4"
radio = input("Ingrese el radio de un círculo: ")
radio = int(radio)  
pi = 3.14159
area = pi * radio * radio  
perimetro = 2 * pi * radio  
print(f"El área del círculo es {area} y su perímetro es {perimetro}")

#ejercicio5
segundos=input("Ingrese una cantidad de segundos y le daremos su equivalente enhoras")
segundos = float(segundos) 
horas=segundos/3600
print(f"La cantidad de segundos ingresados equivalen a {horas} horas")

#ejercicio6
numero=int (input("Ingrese un número y le mostraremos el resultado de dicha tabla de multiplicar"))
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11): 
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#ejercicio7
numero1=int(input("Ingrese un número distinto de 0 : "))
numero2=int(input("Ingrese otro número distinto de 0 : "))
suma=numero1+numero2
resta=numero1-numero2
multiplicacion=numero1*numero2
division=numero1/numero2
print(f"El resultado de la suma es {suma}")
print(f"El resultado de la resta es {resta}")
print(f"El resultado de la multiplicación es {multiplicacion}")
print(f"El resultado de la división es {division}")

#ejercicio8
altura=float(input("Ingrese su altura: "))
peso=float(input("Ingrese su peso: "))
imc=peso/altura**21.65
print(f"Su IMC es {imc}")

#ejercicio9
temperatura_celsius=int(input("Ingrese la temperatura actual en grados Celsius: "))
temperatura_fahrenheit=(9/5)*temperatura_celsius+32
print(f"La temperatura en grados Fahrenheit es de {temperatura_fahrenheit}")

#ejercicio10
numero1=int(input("Ingrese el primer número: "))
numero2=int(input("Ingrese el segundo número: "))
numero3=int(input("Ingrese un tercer número: "))
promedio=(numero1+numero2+numero3)/3
print(f"El promedio de los números ingresados es {promedio}")