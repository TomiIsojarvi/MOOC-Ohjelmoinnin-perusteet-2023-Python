# tee ratkaisu tänne
import json

def tulosta_henkilot(tiedosto: str):
	with open(tiedosto) as file:
		data = file.read()
	henkilot = json.loads(data)

	for henkilo in henkilot:
		print(f"{henkilo['nimi']} {henkilo['ika']} vuotta (", end="")
		tulostus =  ', '.join(henkilo['harrastukset'])
		print(tulostus, end="")
		print(")")

if __name__ == '__main__':
	tulosta_henkilot("tiedosto1.json")