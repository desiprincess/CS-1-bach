a = float(input ("Ingrese la primera longitud del triángulo"))
b = float(input ("Ingrese la segunda longitud del triángulo"))
c = float(input ("Ingrese la tecera longitud del triángulo"))

if a == b == c: 
    print ("El triángulo es equilátero")
elif a == b or a==c or b==c: 
    print ("El triángulo es isóceles")
else: 
    print ("El triángulo es escaleno")
