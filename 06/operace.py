def nacti_cislo(textovy_vstup):
    while True:
        odpoved = input(textovy_vstup)
        try:
            return int(odpoved)
        except ValueError:
            print('To nebylo číslo!')

cislo1 = nacti_cislo("Zadej prvni cislo: ")
cislo2 = nacti_cislo("Zadej druhe cislo: ")

operace = input("Zadej operaci + - * / co s cisly chces delat: ")

try:
    if operace == "+":
        vysledek = cislo1 + cislo2
    elif operace == "-":
       vysledek = cislo1 - cislo2
    elif operace == "*":
        vysledek = cislo1 * cislo2
    elif operace == "/":
        vysledek = cislo1 / cislo2

    print(vysledek)

except ZeroDivisionError:
    print('Nulou se nedá dělit!')

