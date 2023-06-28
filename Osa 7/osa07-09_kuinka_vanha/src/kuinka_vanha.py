# tee ratkaisu tänne
from datetime import datetime

vuosituhat = datetime(1999, 12, 31)

paiva = int(input("Päivä: "))
kuukausi = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))

syntymapaiva = datetime(vuosi, kuukausi, paiva)

if syntymapaiva > vuosituhat:
  print("Et ollut syntynyt, kun vuosituhat vaihtui.")
else:
  ika = vuosituhat - syntymapaiva
  print(f"Olit {ika.days} päivää vanha, kun vuosituhat vaihtui.")