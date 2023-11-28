altura = float (input ("Ingrese su altura: "))
peso = float(input ("Ingrese su peso: "))

IMC = peso / (altura*altura)
print (f"Su índice de masa coporal (IMC) es: {IMC}")
if IMC < 18.5:
    print ("Su IMC indica que su peso está por debajo de lo normal")
elif 18.5 <= IMC < 24.9: 
    print ("Su IMC indica que su peso es normal")
elif 24.9 <= IMC < 29.9:
    print ("Su IMC indica que tiene sobrepeso")
else:
    print ("Su IMC indica que está obeso")
