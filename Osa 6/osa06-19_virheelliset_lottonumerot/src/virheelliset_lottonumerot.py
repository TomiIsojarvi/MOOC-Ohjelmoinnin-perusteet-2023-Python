# tee ratkaisu tänne
def suodata_virheelliset():
	viikot = []
	lottorivit = []

	# Avataan korruptoitunut lottonumerot.csv-tiedosto ja tallentetaan tiedot
	# erillisiin taulukoihin.
	with open("lottonumerot.csv") as tiedosto:
		for rivi in tiedosto:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')

			viikot.append(osat[0])
			lottorivit.append(osat[1])

	with open("korjatut_numerot.csv", "w") as tiedosto:
		# Suodatetaan
		for i in range(0, len(viikot)):
			try:
				viikko = viikot[i].split()
				# Tämä saa aikaan keskeytyksen, jos viikkonumero ei ole numero.
				viikko_nro = int(viikko[1])

				# Viikon lottonumerot
				numerot = lottorivit[i].split(",")
				
				# Liian vähän numeroita
				if len(numerot) != 7:
					raise ValueError("Liian vähän numeroita.")
				
				for j in range(0, 7):
					# Tämä saa aikaan keskeytyksen, jos lottonumero ei ole mumero.
					numero = int(numerot[j])
					
					# Onko numero väliltä 1-39?
					if numero < 1 or numero > 39:
						raise ValueError("Lottonumero liian suuri tai pieni")
					
					# Numero useampaan kertaan.
					if numerot.count(str(numero)) > 1:
						raise ValueError("Numero enemmän kuin yksi kertaa lottorivillä")
					
				tiedosto.write(viikot[i] + ";" + lottorivit[i] + "\n")
					
			except:
				continue

if __name__ == "__main__":
	suodata_virheelliset()