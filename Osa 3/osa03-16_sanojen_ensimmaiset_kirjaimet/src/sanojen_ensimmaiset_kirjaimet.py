lause = input("Anna lause: ")
kohta = 0

while True:
    print(lause[0])

    kohta = lause.find(" ")
    lause = lause[kohta + 1:]

    if kohta == -1:
        break