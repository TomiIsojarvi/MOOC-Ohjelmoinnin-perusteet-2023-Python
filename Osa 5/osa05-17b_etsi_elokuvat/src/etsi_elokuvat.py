# tee ratkaisu tänne
def lisaa_elokuva(rekisteri: list, nimi: str, ohjaaja: str, vuosi: int, pituus: int):
	elokuva = { "nimi": nimi, "ohjaaja": ohjaaja, "vuosi": vuosi, "pituus": pituus }

	rekisteri.append(elokuva)

def etsi_elokuvat(rekisteri: list, hakusana: str):
	haetut_elokuvat = []

	for elokuva in rekisteri:
		if elokuva["nimi"].lower().find(hakusana.lower()) != -1:
			haetut_elokuvat.append(elokuva)
	
	return haetut_elokuvat

if __name__ == "__main__":
	rekisteri = [{"nimi": "Pythonin viemää", "ohjaaja": "Pekka Python", "vuosi": 2017, "pituus": 116},
	{"nimi": "Python lentokoneessa", "ohjaaja": "Renny Pythonen", "vuosi": 2001, "pituus": 94},
	{"nimi": "Koodaajien yö", "ohjaaja": "M. Night Python", "vuosi": 2011, "pituus": 101}]

	lista = etsi_elokuvat(rekisteri, "Python")
	print(lista)