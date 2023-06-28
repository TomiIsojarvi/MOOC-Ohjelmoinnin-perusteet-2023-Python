# tee ratkaisu tänne

def main():
	nimi = input("Kenelle teos omistetaan: ")
	tiedosto_nimi = input("Mihin kirjoitetaan: ")

	with open(tiedosto_nimi, "w") as tiedosto:
		tiedosto.write(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")

main()