# tee ratkaisu tänne

# palauta_rivit - Lukee tiedostosta rivit ja paluttaa ne listana.
def palauta_rivit(tiedosto: str):
	rivit = []

	with open(tiedosto) as data:
		for rivi in data:
			rivi = rivi.replace("\n", "")
			rivit.append(rivi)

	return rivit

# luo_reseptit - Lukee rivilistan ja luo siitä reseptit.
def luo_reseptit(rivit: list):
	reseptit = []
	resepti = []

	for i in range(0, len(rivit)):
		if rivit[i]:
			resepti.append(rivit[i])

			if i == len(rivit) - 1:
				reseptit.append(resepti)
			continue
		else:
			reseptit.append(resepti)
			resepti = []

	return reseptit

# hae_aika - Haku reseptin keittoajan mukaan.
def hae_aika(tiedosto: str, aika: int):
	rivit = palauta_rivit(tiedosto)
	reseptit = luo_reseptit(rivit)

	loydetyt = []

	# Etsitään sanaa resepteistä.
	for resepti in reseptit:
		kesto = int(resepti[1])

		if kesto <= aika:
			loydetyt.append(f"{resepti[0]}, valmistusaika {resepti[1]} min")

	return loydetyt

# hae_nimi - Haku reseptin nimen perusteella.
def hae_nimi(tiedosto: str, sana: str):
	rivit = palauta_rivit(tiedosto)
	reseptit = luo_reseptit(rivit)
	
	loydetyt = []

	# Etsitään sanaa resepteistä.
	for resepti in reseptit:
		nimi = resepti[0]
		nimi = nimi.lower()

		if nimi.find(sana.lower()) != -1:
			loydetyt.append(resepti[0])

	return loydetyt

# hae-raakaaine - Haku raaka-aineen perusteella.
def hae_raakaaine(tiedosto: str, aine: str):
	rivit = palauta_rivit(tiedosto)
	reseptit = luo_reseptit(rivit)

	loydetyt = []

	for resepti in reseptit:
		aineosat = resepti[2:]

		for osa in aineosat:
			osa.lower()

			if osa.find(aine.lower()) != -1:
				#loydetyt.append(resepti)
				loydetyt.append(f"{resepti[0]}, valmistusaika {resepti[1]} min")

	return loydetyt
				
# main - Pääohjelma
def main():
	loydetyt = hae_raakaaine("reseptit1.txt", "maito")

	for resepti in loydetyt:
		print(resepti)

if __name__ == "__main__":
	main()