import pgzrun
import random

TITLE = "shoot the elf game by houd"

score = 0

WIDTH = 500
HEIGHT = 500    

elf = Actor("elf.png")

message = ""

def draw():
    screen.clear()
    screen.fill("black")
    elf.draw()
    screen.draw.text(message,(300,10),fontsize = 30)
    screen.draw.text(str(score),(100,10),fontsize = 30)


    




def place_elf():
    elf.x = random.randint(50,450)
    elf.y = random.randint(50,450)




def on_mouse_down(pos):
    global message
    global score
    if elf.collidepoint(pos):
        message = "good shot"
        score = score +10
        place_elf()

    
        



    else:
        message = "you missed the shot"
        score = score -10



place_elf()







pgzrun.go()

















