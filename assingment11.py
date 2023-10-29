desayuno = int(input("Ingrese la cantidad de calorías cosumidas en el desayuno"))
almuerzo = int(input("Ingrese la cantidad de calorías consumidas en el alumerzo"))
cena = int(input("Ingrese la cantidad de calorías consumidas en la cena"))
refrigerios = int(input("Ingrese la cantidad de calorías consumidas en refrigerios"))

consumo_total = desayuno + almuerzo + cena + refrigerios
print("Calorías totales consumidas: ",consumo_total)
print("Resumen.","\n","Calorias consumidas durante el desayuno: ", desayuno, "\n", "Calorias consumidas durante el almuerzo: ", almuerzo, "\n", "Calorías consumidas durante la cena: ", cena, "\n", "Calorías consumidas en los refrigerios: ", refrigerios, "\n", "Calorías totales consumidas: ", consumo_total)
