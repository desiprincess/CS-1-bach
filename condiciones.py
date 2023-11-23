print("1. Euros")
print("2. Libras Esterlinas")
print("3. Rupias")

eleccion = int(input("Elige a qué moneda quieres convertir tus dólares: "))

if eleccion == 1:
    dolares = float(input("Ingrese la cantidad en dólares para convertir a Euros: "))
    tasa_euros = dolares * 0.91
    print(f"La cantidad de {dolares} dólares es aproximadamente {tasa_euros} Euros")
elif eleccion == 2:
    dolares = float(input("Ingrese la cantidad en dólares para convertir a Libras Esterlinas: "))
    tasa_libras = dolares * 0.80
    print(f"La cantidad de {dolares} dólares es aproximadamente {tasa_libras} Libras")
elif eleccion == 3:
    dolares = float(input("Ingrese la cantidad en dólares para convertir a Rupias: "))
    tasa_rupias = dolares * 83.33
    print(f"La cantidad de {dolares} dólares es aproximadamente {tasa_rupias} Rupias")
else:
    print("Opción no válida. Por favor, elige 1, 2 o 3.")
    
