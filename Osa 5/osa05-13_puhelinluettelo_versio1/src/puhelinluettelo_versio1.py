# tee ratkaisu tänne

# hae_numero - funktio
def hae_numero(puhelinluettelo):
	nimi = input("nimi: ")

	if nimi not in puhelinluettelo:
		print("ei numeroa")
	else:
		print(puhelinluettelo[nimi])

# lisaa_numero - funktio
def lisaa_numero(puhelinluettelo):
	nimi = input("nimi: ")
	numero = input("numero: ")

	puhelinluettelo[nimi] = numero
	print("ok!")

# main - funktio
def main():
	puhelinluettelo = {}

	while True:
		komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")

		if komento == "1":
			hae_numero(puhelinluettelo)

		if komento == "2":
			lisaa_numero(puhelinluettelo)
			
		if komento == "3":
			print("lopetetaan...")
			break

main()