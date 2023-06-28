vuosi = int(input("Vuosi: "))
seuraava = vuosi + 1

while True:
    if seuraava % 4 == 0:
        if seuraava % 100 == 0:
            if seuraava % 400 == 0:
                break
            else:
                seuraava += 1
        else:
            break
    else:
        seuraava += 1

print("Vuotta", vuosi, "seuraava karkausvuosi on", seuraava)