sana = input("Sana: ")
merkki = input("Merkki: ")

kohta = sana.find(merkki)

if kohta != -1:
    if kohta + 3 <= len(sana):
        print(sana[kohta:kohta + 3])