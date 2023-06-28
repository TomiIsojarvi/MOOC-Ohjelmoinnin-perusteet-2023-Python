# tee ratkaisu tänne
def lisaa_sanapari(sana1: str, sana2: str):
	with open("sanakirja.txt", "a") as tiedosto:
		rivi = sana1 + ";" + sana2 + "\n"
		tiedosto.write(rivi)

def hae_sanaa(sana: str):
	sanat = []

	with open("sanakirja.txt") as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')
			sanat.append(osat)

	for sanapari in sanat:
		if sanapari[0].find(sana) >= 0 or sanapari[1].find(sana) >= 0:
			print(sanapari[0] + " - " + sanapari[1])

def main():
	while True:
		print("1 - Lisää sana, 2 - Hae sanaa, 3 - Poistu")
		valinta = int(input("Valinta: "))
		
		if valinta == 3:
			print("Moi!")
			break
		elif valinta == 1:
			sana1 = input("Anna sana suomeksi: ")
			sana2 = input("Anna sana englanniksi: ")
			lisaa_sanapari(sana1, sana2)
			print("Sanapari lisätty")
		elif valinta == 2:
			sana = input("Anna sana: ")
			hae_sanaa(sana)

main()