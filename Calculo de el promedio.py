numeros = []
while True:
    datos = input("Ingresa datos, cuando trmines escribe fin: ")
    if datos.lower() == "fin":
        break

    numeros.append(float(datos))

promedio = sum(numeros) / len(numeros)
print(f"El promedio es:  {promedio:.2f}")
