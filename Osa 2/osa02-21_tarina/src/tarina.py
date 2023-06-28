lause = ""
edellinen_sana = ""

while True:
    sana = input("Anna sana: ")

    if sana == "loppu" or edellinen_sana == sana:
        break

    lause += sana + " "
    edellinen_sana = sana

print(lause)