pisteet = int(input("Kuinka paljon pisteitä? "))
uudet_pisteet = 0

if pisteet < 100:
    uudet_pisteet = pisteet * 1.1
    print("Sait 10 % bonusta")

if pisteet >= 100:
    uudet_pisteet = pisteet * 1.15
    print("Sait 15 % bonusta")

pisteet = uudet_pisteet

print("Pisteitä on nyt", pisteet)