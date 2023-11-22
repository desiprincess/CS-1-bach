print("1. Euros")
print("2. Libras Esterlinas")
print("3. Yenes Japoneses")
elección = int(input("Elige a qué moneda quiere convertir sus dólares"))

if elección == 1: 
    euros = print (input("Ingrese la cantidad en dólares para convertir en euros"))
elif elección == 2:
    libras_esterlinas = print (input("Ingrese la cantidad en dólares para convertir en Libras Esterlinas"))
elif elección == 3: 
    yenes_japoneses = print (input("Ingrese la cantidad en dólares para convertir en Yenes Japoneses"))
    
tasa_euros = euros * 0.91
print (f"La cantidad de {euros} dólares, son aproximadamente {tasa_euros} euros")
    
    
