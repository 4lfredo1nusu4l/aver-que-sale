import random 

def adivinar_el_juego():
    numero_secreto = random.randint(1,100)
    intentos = 0

    while True:
        intento = input(("Ingresa el numero :): "))
        if not intento.isdigit():
            print("Solo puedes introducir numeros :)")
            continue
        
        intento = int(intento)

        if intento < 1 or intento > 100:
            print("Solo números mayores a 0 y menores o iguales a 100 :)")
            continue

        intentos += 1

        if intento > numero_secreto:
            print("Un numero menor: ")
        if intento < numero_secreto:
            print("Un numero mayor: ")

        else:
            print(f"Haz adivindo el numero en {intentos} intentos.")
            break

if __name__  == "__main__":
    adivinar_el_juego()