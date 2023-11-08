import math

kg = float(input("Introduzca su peso en kg"))
m = float(input("Introduzca su altura en m"))

calc = kg / math.pow(m,2)

print(calc)
print(round(calc,2))
