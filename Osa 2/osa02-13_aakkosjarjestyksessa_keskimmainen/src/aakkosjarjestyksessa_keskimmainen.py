kirjain1 = input("Anna 1. kirjain: ")
kirjain2 = input("Anna 2. kirjain: ")
kirjain3 = input("Anna 3. kirjain: ")

if kirjain1 < kirjain2 and kirjain1 < kirjain3:
    if kirjain2 < kirjain3:
        print("Keskimmäinen kirjain on", kirjain2)
    else:
        print("Keskimmäinen kirjain on", kirjain3)
elif kirjain1 > kirjain2 and kirjain1 > kirjain3:
    if kirjain2 > kirjain3:
        print("Keskimmäinen kirjain on", kirjain2)
    else:
        print("Keskimmäinen kirjain on", kirjain3)
else:
    print("Keskimmäinen kirjain on", kirjain1)