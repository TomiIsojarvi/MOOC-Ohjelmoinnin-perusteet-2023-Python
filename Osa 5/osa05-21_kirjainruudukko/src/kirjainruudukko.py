# Kirjoita ratkaisu tähän
def luo_ruudukko(ruudukko:list, kerrokset: int):
  for kerros in range(0, kerrokset):
    rivi = []
    kirjain = chr(65 + kerros)
    
    # Keskimmäiset kirjaimet
    for i in range(0, kerros * 2 + 1):
      rivi.append(kirjain)

    # ulkommaiset kirjaimet
    for i in range(1, kerrokset - kerros):
      rivi.insert(0, chr(65 + kerros + i))
      rivi.append(chr(65 + kerros + i))

    if kerros != 0:
      ruudukko.insert(0, rivi)

    ruudukko.append(rivi)

def tulosta_ruudukko(ruudukko: list):
  for i in range(len(ruudukko)):
    for j in range(len(ruudukko[i])):
      print(ruudukko[i][j], end="")
    print()

def main():
  ruudukko = []

  kerrokset = int(input("Kerrokset: "))
  luo_ruudukko(ruudukko, kerrokset)
  tulosta_ruudukko(ruudukko)

  
main()