#Pozn. Nutná znalost cyklu while
#Naprogramujte hádání čísla: počítač vygeneruje náhodné číslo z rozsahu 1 až 100, ale nevypíše ho. Nechá uživatele v cyklu se ptát na to číslo a vypíše pouze informaci, jestli je hádané číslo větší nebo menší než náhodné číslo.

from random import randrange

nahodne_cislo = randrange(0, 101)
# print(nahodne_cislo)
cislo = 101

while cislo != nahodne_cislo:
    cislo = int(input("Hadejte cislo \n"))

    if cislo == nahodne_cislo:
        print("Uhadl jsi")
    elif cislo < nahodne_cislo:
        print("Hadane cislo je vetsi")
    elif cislo > nahodne_cislo:
        print("Hadane cislo je mensi")