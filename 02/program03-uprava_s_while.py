zadani = " "
i = 0

while zadani != "tajneheslo":
    zadani = input("Zadej tajne heslo: ")

    if zadani == "tajneheslo":
        print("\nTajná zpráva je: V pátek jsem viděl černého havrana")
        input()
    else:
        print("Špatné heslo")
        i = i + 1
        if i == 3: 
            print("Pocet pokusu vyprsel, max 3")
            break
