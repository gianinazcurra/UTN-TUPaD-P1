#Ejercicio 1

edad=int(input("Ingrese su edad"))
if edad >= 18 :
    print("Eres mayor de edad")
else :
    print ("No eres mayor de edad aún")

#Ejercicio 2

nota=int(input("Ingrese la nota obtenida en el exámen : "))
if nota >= 6 :
    print("Aprobaste")
else :
    print ("No aprobaste")

#Ejercicio 3

while True: 
    numero_par = int(input("Ingrese un número par: "))
    
    if numero_par % 2 == 0:
        print("Es un número par")
        break  
    else:
        print("El número ingresado no es par. Vuelva a intentarlo.")

#Ejercicio 4

edad = int(input("Ingrese su edad : "))
if edad < 12 : 
    print("Usted es un niño")
elif edad >= 12 and edad <= 18 :   
        print("Usted es adolescente")
elif edad >=18 and edad <= 30 :
    print ("Usted es un adulto joven")
else :
    print ("Usted es adulto")
       
#Ejercicio 5

contrasena = (input("Ingrese una contraseña de entre 8 y 14 caracteres "))
longitud_contrasena=len(contrasena)

while longitud_contrasena < 8 or longitud_contrasena > 14:
    print("La contraseña debe tener entre 8 y 14 caracteres.")
    contrasena = input("Por favor, ingrese una contraseña de entre 8 y 14 caracteres: ")
    longitud_contrasena = len(contrasena)

print("Ha ingresado una contraseña correcta.")

#Ejercicio 6
from statistics import mode, median, mean 
import random

#creo la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
print (numeros_aleatorios) #los puedo imprimir y ver por pantalla

# calculo la moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# imprimo los resultados de moda, mediana y media
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)

if media > mediana and mediana > moda:
    print("Hay sesgo positivo (a la derecha).")
elif media < mediana and mediana < moda:
    print("Hay sesgo negativo (a la izquierda).")
else:
    print("No hay sesgo.")

#Ejercicio 7

palabra=(input("Ingrese una palabra"))
if palabra [-1].lower() in 'aeiou':  
    palabra += '!'
print(palabra)

#Ejercicio 8

nombre=input("Ingrese su nombre")

print("ELige una opción : ")
print("1.Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("2.Si quiere su nombre en mayúsculas. Por ejemplo: pedro.")
print("Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

opcion = int(input("Ingrese el número de acuerdo a las siguientes opciones: "))

match opcion:
    case 1: 
         nombre2=nombre.upper()
         print("Tu nombre de acuerdo a la opción elegida es : ", nombre2)

    case 2:
        nombre2=nombre.lower()
        print("Tu nombre de acuerdo a la opción elegida es : ", nombre2)

    case 3:
        nombre2=nombre.title()
        print("Tu nombre de acuerdo a la opción elegida es : ", nombre2)

    case _:
        print("Opción no válida. Por favor, elige un número entre 1 y 3.")

#Ejercicio 9

magnitud_terremoto = int(input("Ingrese la magnitud del terremoto : "))
if magnitud_terremoto < 3 : 
    print("Muy leve, prácticamente imperceptible")
elif magnitud_terremoto >= 3 and magnitud_terremoto < 4 :   
        print("Sismo leve, ligeramente perceptible")
elif magnitud_terremoto >=4 and magnitud_terremoto < 5 :
    print ("Moderado: sentido por personas, pero generalmente no causa daños")
elif magnitud_terremoto >=5 and magnitud_terremoto < 6 :
    print ("Fuerte: puede causar daños en estructuras débiles")
elif magnitud_terremoto >=6 and magnitud_terremoto < 7 :
    print ("Muy Fuerte: puede causar daños significativos")
else :
    print ("Extremo:RESGUARDARSE ya que puede causar daños a gran escala")

#Ejercicio 10

def validar_hemisferio():
    hemisferio = input("Ingrese el hemisferio en el que se encuentra, SUR ó NORTE: N/S : ").strip().upper()
    while hemisferio not in ["N", "S"]:
        print("Por favor, ingresa 'N' para hemisferio norte o 'S' para hemisferio sur.")
        hemisferio = input("Ingrese el hemisferio en el que se encuentra, SUR ó NORTE: N/S : ").strip().upper()
    return hemisferio

def validar_mes():
    mes = int(input("Ingrese el mes del año en el que se encuentra (1-12): "))
    while mes < 1 or mes > 12:
        print("Mes inválido. Debe ser un número entre 1 y 12.")
        mes = int(input("Ingrese el mes del año en el que se encuentra (1-12): "))
    return mes

def validar_dia(mes):
   
    dias_en_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if mes == 2:
        dia = int(input(f"Ingrese el día del mes (1-{dias_en_mes[mes]}) : "))
    else:
        dia = int(input(f"Ingrese el día del mes (1-{dias_en_mes[mes]}) : "))
    
    while dia < 1 or dia > dias_en_mes[mes]:
        print(f"Día inválido. Debe ser un número entre 1 y {dias_en_mes[mes]}.")
        dia = int(input(f"Ingrese el día del mes (1-{dias_en_mes[mes]}) : "))
    
    return dia

def determinar_estacion(hemisferio, mes, dia):
    if hemisferio == "N":
        if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
            return "Invierno"
        elif (3 <= mes <= 5) and (mes != 6 or dia <= 20):
            return "Primavera"
        elif (6 <= mes <= 8) and (mes != 9 or dia <= 20):
            return "Verano"
        else:
            return "Otoño"
    else: 
        if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
            return "Verano"
        elif (3 <= mes <= 5) and (mes != 6 or dia <= 20):
            return "Otoño"
        elif (6 <= mes <= 8) and (mes != 9 or dia <= 20):
            return "Invierno"
        else:
            return "Primavera"

def main():
    hemisferio = validar_hemisferio()
    mes = validar_mes()
    dia = validar_dia(mes)

    estacion = determinar_estacion(hemisferio, mes, dia)
    print(f"Estás en {estacion}.")

if __name__ == "__main__":
    main()
