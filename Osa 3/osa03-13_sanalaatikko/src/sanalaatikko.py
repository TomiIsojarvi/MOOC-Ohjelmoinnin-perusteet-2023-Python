PITUUS = 30

sana = input("Sana: ")
sana_pituus = len(sana)
vasen_tyhja = PITUUS // 2 - sana_pituus // 2 - 1
oikea_tyhja = PITUUS - vasen_tyhja - sana_pituus - 2

print("*" * PITUUS)
print("*" + " " * vasen_tyhja + sana + " " * oikea_tyhja + "*")
print("*" * PITUUS)