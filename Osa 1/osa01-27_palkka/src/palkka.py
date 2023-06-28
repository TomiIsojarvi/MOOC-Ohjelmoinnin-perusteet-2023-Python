tuntipalkka = float(input("Tuntipalkka: "))
tunnit = int(input("Työtunnit: "))
viikonpaiva = input("Viikonpäivä: ")

palkka = tuntipalkka * tunnit

if viikonpaiva == "sunnuntai":
    palkka *= 2

print("Palkka", palkka, "euroa")