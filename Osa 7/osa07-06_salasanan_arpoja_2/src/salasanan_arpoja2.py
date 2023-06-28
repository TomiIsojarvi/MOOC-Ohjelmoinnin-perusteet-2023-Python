# tee ratkaisu tänne
from random import shuffle
from random import choice
from random import randint
import string

def luo_hyva_salasana(pituus: int, numeroita: bool, erikoismerkkeja: bool):
	erikoismerkit = "!?=+-()#"
	salasana = ""
	ascii_salasana = ""
	numero_salasana = ""
	erikois_salasana = ""

	for i in range(pituus):
		# Luodaan listat ASCII-kirjaimille (pienet kirjaimet),
		# numeroille ja erikoismerkeille
		ascii_salasana += choice(string.ascii_lowercase)
		if numeroita == True:
			numero_salasana += choice(string.digits)
		if erikoismerkkeja == True:
			erikois_salasana += choice(erikoismerkit)

	# Jos ei numeroita eikä erikoismerkkejä, niin palautetaan pienillä kirjaimilla.
	if not numeroita and not erikoismerkkeja:
		salasana += ascii_salasana[:pituus]
		return salasana
	
	# Alustetaan pituudet
	ascii_pituus = pituus
	numero_pituus = 0
	erikois_pituus = 0

	# Lasketaan pienten merkkien maksimimäärä.
	if numeroita and erikoismerkkeja:
		ascii_pituus -= 2
	else:
		ascii_pituus -= 1

	# Pienten merkkien määrä
	ascii_pituus = randint(1, ascii_pituus)

	# Jos numeroita, niin lasketaan niiden määrä
	if numeroita:
		numero_pituus = pituus - ascii_pituus

		if erikoismerkkeja:
			numero_pituus -= 1
			numero_pituus = randint(1, numero_pituus)

	# jos erikoismerkkejä, niin lasketaan niiden määrä.
	if erikoismerkkeja:
		erikois_pituus = pituus - ascii_pituus - numero_pituus

	#Lisätään salasanaan kaikki merkit.
	salasana += ascii_salasana[:ascii_pituus]
	if numeroita:
		salasana += numero_salasana[:numero_pituus]
	if erikoismerkkeja:
		salasana += erikois_salasana[:erikois_pituus]

	# Sekoitetaan
	l = list(salasana)
	shuffle(l)
	salasana = ''.join(l)

	# Palautetaan lopullinen salasana.
	return salasana

if __name__ == '__main__':
	for i in range(10):
		print(luo_hyva_salasana(8, True, True))