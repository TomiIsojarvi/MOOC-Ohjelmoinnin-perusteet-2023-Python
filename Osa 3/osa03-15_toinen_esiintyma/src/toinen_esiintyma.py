sana = input("Anna merkkijono: ")
osa = input("Anna osajono: ")
esiintymat = 0
tarkka_kohta = 0

i = 0

while i < 2:

    if len(sana) == 0:
        break

    kohta = sana.find(osa)
    
    if i == 0:
        tarkka_kohta = kohta
    else:
        tarkka_kohta = tarkka_kohta + len(osa) + kohta

    if kohta == -1:
        break

    esiintymat += 1
        
    sana = sana[kohta + len(osa):]
    i += 1

if esiintymat < 2:
    print("Osajono ei esiinny merkkijonossa kahdesti.")
else:
    print(f"Osajonon toinen esiintymä on kohdassa {tarkka_kohta}.")