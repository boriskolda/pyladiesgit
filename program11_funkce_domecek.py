from turtle import forward, left, right, shape, penup, pendown, exitonclick
from math import sqrt

def vykresli_domecek(velikost):
    for i in range(4):
        forward(velikost)
        left(90)

    left(45)
    forward(sqrt(2)*velikost)
    left(90)
    forward(sqrt(2)*velikost/2)
    left(90)
    forward(sqrt(2)*velikost/2)
    left(90)
    forward(sqrt(2)*velikost)
    left(45)
    forward(50)

vykresli_domecek(50)
vykresli_domecek(100)
vykresli_domecek(150)

exitonclick()
