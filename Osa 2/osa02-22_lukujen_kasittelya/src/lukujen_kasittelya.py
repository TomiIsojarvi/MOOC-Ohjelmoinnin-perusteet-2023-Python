print("Syötä kokonaislukuja, 0 lopettaa:")
maara = 0
summa = 0
pos = 0
neg = 0

while True:
    luku = int(input("Luku: "))

    if luku == 0:
        break

    if luku > 0:
        pos += 1
    elif luku < 0:
        neg += 1

    maara += 1
    summa += luku

print("Lukuja yhteensä", maara)
print("Lukujen summa", summa)
print("Lukujen keskiarvo", summa / maara)
print("Positiivisia", pos)
print("Negatiivisia", neg)