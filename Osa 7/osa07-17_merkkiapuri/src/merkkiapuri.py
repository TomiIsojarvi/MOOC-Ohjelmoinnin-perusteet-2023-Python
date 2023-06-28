import string

def vaihda_koko(merkkijono: str) -> str:
	return merkkijono.swapcase()

def puolita(merkkijono: str) -> tuple:
	koko = len(merkkijono)
	keskikohta = koko // 2

	m1 = merkkijono[0:keskikohta]
	m2 = merkkijono[keskikohta:koko]

	return m1, m2

def poista_erikoismerkit(merkkijono: str) -> str:
	jono = merkkijono
	erikoismerkit = string.punctuation + "¤"

	for merkki in jono:
		if merkki in erikoismerkit:
			jono = jono.replace(merkki, "")

	return jono
	

if __name__ == '__main__':
	mjono = "Moi kaikki!"

	print(vaihda_koko(mjono))

	p1, p2 = puolita(mjono)

	print(p1)
	print(p2)

	m2 = poista_erikoismerkit("Tämä on testi, katsotaan miten käy!!!11!")
	print(m2)