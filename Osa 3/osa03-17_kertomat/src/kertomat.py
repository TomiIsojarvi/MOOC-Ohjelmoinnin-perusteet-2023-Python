while True:
    luku = int(input("Anna luku: "))

    if luku < 0 or luku == 0:
        print("Kiitos ja moi!")
        break

    i = 1
    kertoma = 1
    while i <= luku:
        kertoma = kertoma * i
        i += 1

    print(f"Luvun {luku} kertoma on {kertoma}")