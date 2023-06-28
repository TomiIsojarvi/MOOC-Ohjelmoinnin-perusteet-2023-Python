# tee ratkaisu tänne
def uniikit(lista):
  uusi_lista = []

  for i in lista:
    if i not in uusi_lista:
      uusi_lista.append(i)
  
  uusi_lista.sort()

  return uusi_lista

if __name__ == '__main__':
  lista = [3, 2, 2, 1, 3, 3, 1]
  print(uniikit(lista)) # [1, 2, 3]