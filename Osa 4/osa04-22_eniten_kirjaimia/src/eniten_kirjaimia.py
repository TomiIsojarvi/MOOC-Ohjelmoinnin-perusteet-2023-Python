# tee ratkaisu tänne
def eniten_kirjainta(mjono):
	eniten = ""
	maara = 0

	for kirjain in mjono:
		count = mjono.count(kirjain)
		if count > maara:
			maara = count
			eniten = kirjain

	return eniten

if __name__ == '__main__':
	mjono = "abcbdbe"
	print(eniten_kirjainta(mjono))

	toinen_jono = "esimerkkimerkkijonokki"
	print(eniten_kirjainta(toinen_jono))