mates = int(input("Introduce tu nota de mates"))
lengua = int(input<("Introduce tu nota de lengua"))
inglés = int(input("Introduce tu nota de inglés"))
informática = int(input("Introduce tu nota de informática"))
biología = int(input("Introduce tu nota en biología"))
tecnología = int(input("Introduce tu nota de tecnología"))
música = int(input("Introduce tu nota de música"))
plástica = int(input("Introduce tu nota de plástica"))

media = (mates + lengua + inglés + infromática + biología + tecnología + música + plástica) / 8
if media >= 5:
    print("Enhorabuena")
else:
    print("Haber estudiado")
