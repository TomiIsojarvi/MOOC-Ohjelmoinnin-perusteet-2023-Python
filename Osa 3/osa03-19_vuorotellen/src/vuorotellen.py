luku = int(input("Anna luku: "))

i = 1
j = luku

while i <= luku and j > 0:
    if i > j:
        break 

    print(i)
    if j != i:
        print(j)

    i += 1
    j -= 1