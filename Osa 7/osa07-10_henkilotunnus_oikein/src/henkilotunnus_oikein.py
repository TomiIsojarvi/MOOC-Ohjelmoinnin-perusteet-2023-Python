# tee ratkaisu tänne
from datetime import datetime

def onko_validi(hetu: str):
	paiva = int(hetu[:2])
	kk = int(hetu[2:4])
	vuosi = int(hetu[4:6])
	valimerkki = hetu[6:7]
	yksilonumero = int(hetu[7:10])
	tarkistusnumero = hetu[10:11]

	# Onko hetu oikean pituinen?
	if len(hetu) > 11:
		return False

	# Onko välimerkki validi?
	if valimerkki == "+":
		vuosi += 1800
	elif valimerkki == "-":
		vuosi += 1900
	elif valimerkki == "A":
		vuosi += 2000
	else:
		return False

	# Onko syntymäpäivä validi?
	try:
		syntymapaiva = datetime(vuosi, kk, paiva)
	except:
		return False
	
	tarkistus = int(hetu[0:6] + hetu[7:10])
	tarkistus %= 31

	tarkistusmerkit = "0123456789ABCDEFHJKLMNPRSTUVWXY"
	tarkistusmerkki = tarkistusmerkit[tarkistus]

	# Onko tarkistusnumero väärin?
	if tarkistusmerkki != tarkistusnumero:
		return False
	
	return True
	
if __name__ == "__main__":
	onko_validi("230827-906F")