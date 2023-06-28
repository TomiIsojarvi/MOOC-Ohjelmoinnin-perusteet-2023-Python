# tee ratkaisu tänne
def kaikki_vaarinpain(lista):
	uusi_lista = lista[::-1]
	uusi_lista2 = []

	for sana in uusi_lista:
		sana = sana[::-1]
		uusi_lista2.append(sana)

	return uusi_lista2

if __name__ == '__main__':
	lista = ["Moi", "kaikki", "esimerkki", "vielä yksi"]
	lista2 = kaikki_vaarinpain(lista)
	print(lista2)