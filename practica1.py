#Ejercicio 7

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
    # Definimos el número máximo de días en cada mes
    dias_en_mes = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    # Si el mes es febrero, hay que verificar si es año bisiesto o no
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
    else:  # Hemisferio Sur
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
