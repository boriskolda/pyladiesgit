def bumbac(cislo):
    if cislo % 2 == 0:
        return "Bum"
    return "Bác"
    
def vypis_bum_bac(pocet):
    for i in range(pocet):
        print(bumbac(i))


vypis_bum_bac(5)