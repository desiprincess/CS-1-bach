x = float(input("Ingrese las coordenadas x: "))
y = float(input("Ingrese las coordenadas y: "))

if x > 0 and y > 0: 
    print ("El punto se encuentra en el cuadrante 1")
elif x < 0 and y > 0: 
    print ("El punto se encuentra en el cuadrante 2")
elif x < 0 and y < 0:
    print ("El punto se encuentra en el cuadrante 3")
elif x > 0 and y < 0:
    print ("El punto se encuentra en el ciadrante 4")
elif x or y == 0:
    print ("El punto se encuentra en un eje")
