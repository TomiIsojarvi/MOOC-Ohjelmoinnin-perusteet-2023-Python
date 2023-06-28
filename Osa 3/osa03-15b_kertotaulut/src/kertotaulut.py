luku = int(input("Anna luku: "))
i = 1

while i <= luku:
    j = 1

    while j <= luku:
        print(f"{i} x {j} = {i * j}")
        j+= 1

    i +=1