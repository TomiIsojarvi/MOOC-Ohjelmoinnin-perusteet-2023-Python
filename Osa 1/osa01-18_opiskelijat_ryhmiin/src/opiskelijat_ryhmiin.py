opiskelijat = int(input("Montako opiskelijaa? "))
ryhma_koko = int(input("Mikä on ryhmän koko? "))
maara = opiskelijat // ryhma_koko

if opiskelijat - maara * ryhma_koko > 0:
    maara += 1

print("Ryhmien määrä:", maara)