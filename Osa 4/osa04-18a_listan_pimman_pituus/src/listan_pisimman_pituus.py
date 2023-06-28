# tee ratkaisu tänne
def pisimman_pituus(lista):
  suurin_pituus = 0
  
  for i in lista:
    pituus = len(i)
    if pituus > suurin_pituus:
      suurin_pituus = pituus

  return suurin_pituus

if __name__ == '__main__':
  print(pisimman_pituus(["abc", "ab"]))