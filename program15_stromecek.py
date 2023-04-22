from turtle import forward, left, right, exitonclick
from math import sqrt

def stromecek(delka, uhel):
    if delka < 20:
        forward(delka)
        left(180)
        forward(delka)
        left(180)
    else:
        forward(delka/2)
        right(uhel)
        stromecek(delka/2, uhel*2/3)
        left(uhel)
        stromecek(delka/2, uhel*2/3)
        left(uhel)
        

stromecek(100,45)

exitonclick()
