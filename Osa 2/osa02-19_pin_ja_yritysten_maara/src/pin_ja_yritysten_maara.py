yritykset = 0

while True:
    pin = input("PIN-koodi: ")
    yritykset += 1

    if pin == "4321":
        if yritykset == 1:
            print("Oikein, tarvitsit vain yhden yrityksen!")
        else:
            print("Oikein, tarvitsit", yritykset, "yritystä")
        break

    print("Väärin")
