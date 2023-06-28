pisteet = int(input("Anna pisteet [0-100]: "))
arvosana = "Arvosana: "

if pisteet < 0:
    arvosana += "mahdotonta!"
elif pisteet >= 0 and pisteet <= 49:
    arvosana += "hylätty"
elif pisteet >= 50 and pisteet <= 59:
    arvosana += "1"
elif pisteet >= 60 and pisteet <= 69:
    arvosana += "2"
elif pisteet >= 70 and pisteet <= 79:
    arvosana += "3"
elif pisteet >= 80 and pisteet <= 89:
    arvosana += "4"
elif pisteet >= 90 and pisteet <= 100:
    arvosana += "5"
else:
    arvosana += "mahdotonta!"

print(arvosana)