# Kirjoita ratkaisu tähän
lista = []
luku = 1

while True:
	print("Lista on nyt", lista)
	komento = input("(l)isää, (p)oista vai e(x)it: ")

	if komento == "l":
		lista.append(luku)
		luku += 1
		continue

	if komento == "p":
		luku -= 1
		lista.remove(luku)
		continue

	if komento == "x":
		print("Moi!")
		break
