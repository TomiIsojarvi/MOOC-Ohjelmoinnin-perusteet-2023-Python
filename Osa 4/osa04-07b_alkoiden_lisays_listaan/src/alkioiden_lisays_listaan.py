# Kirjoita ratkaisu tähän
luvut = []
maara = int(input("Kuinka monta lukua: "))
i = 0

while i < maara:
	luvut.append(int(input(f"Anna luku {i + 1}: ")))
	i += 1

print(luvut)
