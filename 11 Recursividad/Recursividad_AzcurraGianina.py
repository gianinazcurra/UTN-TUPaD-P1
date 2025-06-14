#Ejercicio 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

limite = int(input("Ingrese un número entero para calcular factoriales hasta ese número: "))
for i in range(1, limite + 1):
    print(f"Factorial de {i} es {factorial(i)}")

#Ejercicio 2

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input("Ingrese hasta qué posición quiere ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(fibonacci(i), end=" ")

#Ejercicio 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

b = int(input("\nIngrese la base: "))
e = int(input("Ingrese el exponente: "))
print(f"{b}^ {e} = {potencia(b, e)}")

#Ejercicio 4

def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingrese un número decimal para convertir a binario:"))
binario = decimal_a_binario(numero)
print(f"Binario: {binario if binario else '0'}")

#Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingrese una palabra para verificar si es palíndromo:").lower()
print("Es palíndromo" if es_palindromo(texto) else "No es palíndromo")

#Ejercicio 6

def suma_digitos(n):
    if n < 10:
        return n
    else:
        return n % 10 + suma_digitos(n // 10)

num = int(input("Ingrese un número para sumar sus dígitos:"))
print(f"Suma de dígitos: {suma_digitos(num)}")

#Ejercicio 7

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

niveles = int(input("Ingrese el número de bloques en el nivel más bajo:"))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

#Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    if numero % 10 == digito:
        return 1 + contar_digito(numero // 10, digito)
    else:
        return contar_digito(numero // 10, digito)

n = int(input("Ingrese un número entero: "))
d = int(input("Ingrese el dígito a contar (0-9): "))
print(f"El dígito {d} aparece {contar_digito(n, d)} veces")
