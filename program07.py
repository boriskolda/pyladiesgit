def pocet_vterin(cas_min, cas_sec):
    return cas_min*60 + cas_sec


minuty = int(input('Zadej minuty: '))
vteriny = int(input('Zadej vteriny, vratim cas v sekundach: '))

print(pocet_vterin(minuty,vteriny))