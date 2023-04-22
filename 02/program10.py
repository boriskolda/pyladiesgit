# Napiš program, který se nejprve uživatele zeptá na těleso, které má vypočítat (krychle, kvádl, koule). Potom se zeptejte, jakou metriku má vypočítat (objem, povrh).

pokracovat = "ano"

while pokracovat == "ano":
    teleso = input("Co chcete pocitat? krychle, kvadr, koule \n")
    if teleso == "krychle":
        strana = int(input("Zadejte strany krychle pro vypocet \n"))
        print(f"Krychle ma objem {strana**3}")
    elif teleso == "kvadr":
        strana1 = int(input("Zadejte stranu1 kvadru "))
        strana2 = int(input("Zadejte stranu2 kvadru "))
        strana3 = int(input("Zadejte stranu3 kvadru "))
        print(f"Objem kvadru je {strana1*strana2*strana3}")
    else:
        print("Zvolte teleso pro vypocet")
    pokracovat = input("Chcete pokracovat ano/ne ? ")