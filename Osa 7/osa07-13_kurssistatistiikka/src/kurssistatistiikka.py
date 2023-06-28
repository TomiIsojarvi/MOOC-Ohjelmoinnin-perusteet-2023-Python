# tee ratkaisu tänne
import urllib.request
import json
from math import floor

def hae_kaikki():
	kurssit = []
	pyynto = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
	pyynto = pyynto.read()
	data = json.loads(pyynto)

	for kurssi in data:
		if kurssi["enabled"] == True:
			harjoitus_yht = 0
			for harjoitus in kurssi['exercises']:
				harjoitus_yht += harjoitus

			kurssit.append((kurssi["fullName"], kurssi["name"], kurssi["year"], harjoitus_yht))

	return kurssit

def hae_kurssi(kurssi: str):
	pyynto = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{kurssi}/stats")
	pyynto = pyynto.read()
	data = json.loads(pyynto)
	
	# Viikkojen määrä
	viikkoja = len(data)

	# Opiskelijat, tunnit ja tehtävät
	opiskelijat = []
	tunteja = 0
	tehtavia = 0

	for viikko in data:
		opiskelijat.append(data[viikko]["students"])
		tunteja += data[viikko]["hour_total"]
		tehtavia += data[viikko]["exercise_total"]

	# Eniten opiskelijoita
	eniten = max(opiskelijat)

	# Tunteja keskimäärin
	tunteja_kesk = floor(tunteja / eniten)
	tehtavia_kesk = floor(tehtavia / eniten)

	return {'viikkoja': viikkoja, 'opiskelijoita': eniten, 'tunteja': tunteja, \
	 "tunteja_keskimaarin": tunteja_kesk, "tehtavia": tehtavia, "tehtavia_keskimaarin": tehtavia_kesk}

if __name__ == "__main__":
	hae_kaikki()
	print(hae_kurssi("docker2019"))