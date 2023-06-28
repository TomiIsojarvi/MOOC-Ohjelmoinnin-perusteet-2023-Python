# Kirjoita ratkaisu tähän
# lue_syotteet - funktio
def lue_syotteet():
	syotteet = []

	while True:
		syote = input("Koepisteet ja harjoitusten määrä: ")

		if syote == "":
			break

		syote = syote.split()
		syotteet.append(int(syote[0]))
		syotteet.append(int(syote[1]))

	return syotteet

# laske_harjoituspisteet - funktio
def laske_harjoituspisteet(syote: list):
	pisteet = []

	for i in range(1,len(syote),2):
		pisteet.append(syote[i] // 10)

	return pisteet

# laske_pisteet - funktio
def laske_pisteet(syote: list):
	harj_pisteet = laske_harjoituspisteet(syote)
	pisteet = []

	for i in range(0, len(syote), 2):
		pisteet.append(syote[i] + harj_pisteet[i // 2])

	return pisteet

# laske_arvosanat - funktio
def laske_arvosanat(syote: list):
	pisteet = laske_pisteet(syote)
	arvosanat = []

	for i in range(0, len(syote), 2):
		j = i // 2

		if syote[i] < 10:
			arvosanat.append(0)
			continue

		if pisteet[j] >= 0 and pisteet[j] < 15:
			arvosanat.append(0)
		elif pisteet[j] >= 15 and pisteet[j] < 18:
			arvosanat.append(1)
		elif pisteet[j] >= 18 and pisteet[j] < 21:
			arvosanat.append(2)
		elif pisteet[j] >= 21 and pisteet[j] < 24:
			arvosanat.append(3)
		elif pisteet[j] >= 24 and pisteet[j] < 28:
			arvosanat.append(4)
		else:
			arvosanat.append(5)

	return arvosanat

# tulosta_arvosanat - funktio
def tulosta_arvosanat(arvosanat: list):
	print("Arvosanajakauma:")
	print("5:", '*' * arvosanat.count(5))
	print("4:", '*' * arvosanat.count(4))
	print("3:", '*' * arvosanat.count(3))
	print("2:", '*' * arvosanat.count(2))
	print("1:", '*' * arvosanat.count(1))
	print("0:", '*' * arvosanat.count(0))

# tilastot - funktio
def tilastot(syote: list):
	pisteet = laske_pisteet(syote)
	arvosanat = laske_arvosanat(syote)

	maara = len(pisteet)
	summa = sum(pisteet)
	keskiarvo = summa / maara
	
	hyvaksyttyja = maara - arvosanat.count(0)

	print("Tilasto:")
	print(f"Pisteiden keskiarvo:{keskiarvo: .1f}")
	print(f"Hyväksymisprosentti:{(hyvaksyttyja / maara * 100): .1f}")
	tulosta_arvosanat(arvosanat)



# main - funktio
def main():
	syote = lue_syotteet()
	#syote = [15, 87, 10, 55, 11, 40, 4, 17]
	tilastot(syote)

main()