cantidad = 50
precio_botellas = 1.99
descuento = 3.99 
precio_final = cantidad * precio_botellas - descuento

print(f"El precio final de {cantidad} botellas a {precio_botellas} euros cada una y con descuento es de: {precio_final} euros.")

#Bonus

print(round(precio_final,2))
