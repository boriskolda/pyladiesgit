from random import randrange
nahodne_cislo = randrange(3)

if nahodne_cislo == 0:
    tvar = "trojúhelník"
elif nahodne_cislo == 1:
    tvar = "čtverec"
else:
    tvar = "kolečko"

print(tvar)