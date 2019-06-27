from turtle import *


def koch(size,n):
    if n==0:
        fd(size)
    else:
        for angel in [0,60,-120,60]:
            left(angel)
            koch(size/3,n-1)




def main():
    setup(600,600)
    penup()
    goto(-200,100)
    pendown()
    pensize(2)
    level=3
    koch(400,level)
    right(120)
    koch(400,level)
    right(120)
    koch(400,level)
    hideturtle()

main()