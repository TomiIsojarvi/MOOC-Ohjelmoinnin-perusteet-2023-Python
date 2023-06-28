# tee ratkaisu tänne
import math

# hae_asematiedot - Hakee asematiedot tiedostosta
def hae_asematiedot(tiedosto: str):
	asemat = {}

	with open(tiedosto) as data:
		for rivi in data:
			rivi = rivi.replace("\n", "")
			osat = rivi.split(';')

			if osat[0] == "Longitude":
				continue

			paikka = (float(osat[0]), float(osat[1]))
			nimi = osat[3]

			asemat[nimi] = paikka

		return asemat

# etaisyys - Laskee etäisyyden kahden aseman välillä
def etaisyys(asemat: dict, asema1: str, asema2: str):
	longitude1 = 0.0
	latitude1 = 0.0

	for asema in asemat:
		if asema == asema1:
			longitude1 = asemat[asema][0]
			latitude1 = asemat[asema][1]

		if asema == asema2:
			longitude2 = asemat[asema][0]
			latitude2 = asemat[asema][1]

	x_kilometreina = (longitude1 - longitude2) * 55.26
	y_kilometreina = (latitude1 - latitude2) * 111.2
	etaisyys = math.sqrt(x_kilometreina**2 + y_kilometreina**2)

	return etaisyys

# suurin_etaisyys - Laskee kaikkien asemien välisen pisimmän etäisyyden
def suurin_etaisyys(asemat: dict):
	suurin = 0.0
	suurin1 = ""
	suurin2 = ""

	for asema1 in asemat:
		for asema2 in asemat:
			if asema1 == asema2:
				continue
			
			distance = etaisyys(asemat, asema1, asema2)
			if distance > suurin:
				suurin = distance
				suurin1 = asema1
				suurin2 = asema2


	return (suurin1, suurin2, suurin)

if __name__ == "__main__":
	asemat = hae_asematiedot('stations1.csv')
	asema1, asema2, suurin = suurin_etaisyys(asemat)
	print(asema1, asema2, suurin)