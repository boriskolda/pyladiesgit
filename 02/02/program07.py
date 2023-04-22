# kamen, nuzky, papir
from random import randrange

nahodne_cislo = randrange(3)


if nahodne_cislo == 0:
    tah_pocitace = "kámen"
elif nahodne_cislo == 1:
    tah_pocitace = "nůžky"
else:
    tah_pocitace = "papír"


tah_hrace = input("Jak budete táhnout, zadejte kámen, nůžky, papír :-) ")

print("Počítač zvolil: ", tah_pocitace)

if tah_hrace == "kámen":
    if tah_pocitace == "kámen":
        print("Remíza!")
    if tah_pocitace == "nůžky":
        print("Vyhrál jsi!")
    if tah_pocitace == "papír":
        print("Prohrál jsi!")
elif tah_hrace == "nůžky":
    if tah_pocitace == "kámen":
        print("Prohrál jsi!")
    if tah_pocitace == "nůžky":
        print("Remíza!")
    if tah_pocitace == "papír":
        print("Vyhrál jsi!")
elif tah_hrace == "papír":
    if tah_pocitace == "kámen":
        print("Vyhrál jsi!")
    if tah_pocitace == "nůžky":
        print("Prohrál jsi!")
    if tah_pocitace == "papír":
        print("Remíza!")

else:
    print("Je potřeba zadat přesně kámen, nůžky, papír")
