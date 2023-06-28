# tee ratkaisu tänne

# lisaa_opiskelija - funktio
# Lisää opiskelijan rekisteriin
def lisaa_opiskelija(opiskelijat: dict, nimi: str):
	if nimi not in opiskelijat:
		opiskelijat[nimi] = []

# lisaa_suoritus - funktio
# Lisää suorituksen rekisteriin
def lisaa_suoritus(opiskelijat: dict, nimi: str, suoritus: tuple):
	if nimi in opiskelijat:
		if suoritus[1] == 0:
			return

		for kurssi in opiskelijat[nimi]:
			# Onko suoritus jo rekisterissä?
			if kurssi[0] == suoritus[0]:
				# Onko arvosana noussut?
				if kurssi[1] < suoritus[1]:
					opiskelijat[nimi].append(suoritus)
					opiskelijat[nimi].remove(kurssi)
				return
	
		opiskelijat[nimi].append(suoritus)

# laske_keskiarvo - funktio
# Laskee suoritusten keskiarvon
def laske_keskiarvo(suoritukset: list):
	maara = len(suoritukset)
	summa = 0

	for suoritus in suoritukset:
		summa += suoritus[1]

	return summa / maara

# tulosta_suoritukset - funktio
# Apufunktio, joka tulostaa suoritukset
def tulosta_suoritukset(suoritukset: list):
	maara = len(suoritukset)

	if maara == 0:
		print(" ei suorituksia")
		return

	print(f" suorituksia {maara} kurssilta:")

	for suoritus in suoritukset:
		print(f"  {suoritus[0]} {suoritus[1]}")

	keskiarvo = laske_keskiarvo(suoritukset)

	print(f" keskiarvo {keskiarvo}")

# tulosta - funktio
# Tulostaa rekisterin
def tulosta(opiskelijat: dict, nimi: str):
	if nimi not in opiskelijat:
		print(f"ei löytynyt ketään nimellä {nimi}")
	else:
		print(f"{nimi}:")
		tulosta_suoritukset(opiskelijat[nimi])

# kooste - funktio
# Tulostaa koosteen kaikista opiskelijoista ja suorituksista
def kooste(opiskelijat: dict):
	maara = 0
	maara_nimi = ""
	keskiarvo = 0
	keskiarvo_nimi = ""

	print(f"opiskelijoita {len(opiskelijat)}")

	for nimi in opiskelijat:
		if len(opiskelijat[nimi]) > maara:
			maara = len(opiskelijat[nimi])
			maara_nimi = nimi

		if laske_keskiarvo(opiskelijat[nimi]) > keskiarvo:
			keskiarvo = laske_keskiarvo(opiskelijat[nimi]) 
			keskiarvo_nimi = nimi

	print(f"eniten suorituksia {maara} {maara_nimi}")
	print(f"paras keskiarvo {keskiarvo} {keskiarvo_nimi}")


# main - funktio
# Pääfunktio
def main():
	opiskelijat = {}
	lisaa_opiskelija(opiskelijat, "Pekka")
	lisaa_opiskelija(opiskelijat, "Liisa")
	lisaa_suoritus(opiskelijat, "Pekka", ("Lama", 1))
	lisaa_suoritus(opiskelijat, "Pekka", ("Ohpe", 1))
	lisaa_suoritus(opiskelijat, "Pekka", ("Tira", 1))
	lisaa_suoritus(opiskelijat, "Liisa", ("Ohpe", 5))
	lisaa_suoritus(opiskelijat, "Liisa", ("Jtkt", 4))
	#tulosta(opiskelijat, "Pekka")
	#tulosta(opiskelijat, "Liisa")
	kooste(opiskelijat)

if __name__ == "__main__":
	main()