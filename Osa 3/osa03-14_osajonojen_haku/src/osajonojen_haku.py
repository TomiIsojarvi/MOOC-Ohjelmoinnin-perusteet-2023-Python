sana = input("Sana: ")
merkki = input("Merkki: ")

while True:
    if len(sana) == 0:
        break

    kohta = sana.find(merkki)

    if kohta == -1:
        break

    if kohta + 3 <= len(sana):
        print(sana[kohta:kohta + 3])
        
    sana = sana[kohta + 1:]