merkkijono = input("Anna merkkijono: ")
pituus = len(merkkijono)
i = pituus - 1

while i >= 0:
    print(merkkijono[i:])
    i -= 1