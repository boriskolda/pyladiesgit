rychlost = int(input('Jak jedete rychle? '))
if rychlost >= 150:
    print('Dobré auto?')
elif rychlost >= 100:
    print('Skoda auto?')
elif rychlost >= 20:
    print('Kolo?')
elif rychlost >= 5:
    print('Kolobezka?')
else:
    print('Spatna volba')