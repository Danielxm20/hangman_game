import random

with open("palabras.txt", "r") as f:
	palabras = f.readlines()

palabra = random.choice(palabras)[:-1]

errores_restantes = 5
aciertos = []
exito = False

while not exito:
	for letra in palabra:
		if letra.lower() in aciertos:
			print(letra, end=" ")
		else:
			print("_", end=" ")
	print("")
	intento = input(f"Tienes {errores_restantes} oportunidades mas, Siguiente intento:")
	aciertos.append(intento.lower())
	if intento.lower() not in palabra.lower():
		errores_restantes -= 1
		if errores_restantes == 0:
			break
	exito = True
	for letra in palabra:
		if letra.lower() not in aciertos:
			exito = False
if exito:
	print(f"Acertaste la palabra era: {palabra}")
else:
	print(f"Juego Terminado, la palabra es: {palabra}")
