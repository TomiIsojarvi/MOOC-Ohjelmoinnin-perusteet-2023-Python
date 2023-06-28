# tee ratkaisu tänne
def suodata_laskut():
	with open("oikeat.csv", "w") as oikeat, open("vaarat.csv", "w") as vaarat:
		pass

	with open("laskut.csv") as lasku_tiedosto, \
		open("oikeat.csv", "a") as oikeat_tiedosto, \
		open("vaarat.csv", "a") as vaarat_tiedosto:

		for rivi in lasku_tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')

			nimi = osat[0]
			lasku = eval(osat[1])
			lopputulos = int(osat[2])

			if lasku == lopputulos:
				oikeat_tiedosto.write(f"{nimi};{osat[1]};{lopputulos}\n")
			else:
				vaarat_tiedosto.write(f"{nimi};{osat[1]};{lopputulos}\n")

			print(f"{osat[1]} {lasku} {lopputulos}")

if __name__ == "__main__":
	suodata_laskut()