asti = int(input("Mihin asti: "))
summa = 1
lisattava = 2
lauseke = "Laskettiin 1"

while summa < asti:
    lauseke += " + " + str(lisattava)
    summa += lisattava
    lisattava += 1

print(lauseke + " = " + str(summa))