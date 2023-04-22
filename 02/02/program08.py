# Testování malé násobilky
# Nechte počítač náhodně vygenerovat dvě čísla v rozsahu 1 až 10 a uživatele vyzvěte k zadání jejich součinu. Ověřte, jestli uživatel odpověděl správně.

from random import randrange

chcete_pokracovat = "ano"

while chcete_pokracovat == "ano":
    cislo1 = randrange(11)
    cislo2 = randrange(11)
    vysledek = int(input(f"Zadejte součin čísel: {cislo1} a {cislo2}\n"))
    if vysledek == cislo1 * cislo2:
        print("Správně")
    else:
        print("Špatně")

    chcete_pokracovat = input("Chcete pokracovat ano/ne ? ")

