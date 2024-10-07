import pgzrun
import random
WIDTH = 500
HEIGHT = 500
def draw():
    screen.fill("white")
    r1=240
    for i in range (10):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        screen.draw.filled_circle((250,250),r1,(r,g,b))
        r1=r1-20
pgzrun.go()