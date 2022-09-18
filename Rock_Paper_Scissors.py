from guizero import App, PushButton, Box, Picture
import random

def redraw():
    item1.enabled = True
    item2.enabled = True
    item3.enabled = True
    item1.visible = True
    item2.visible = True
    item3.visible = True
    citem1.visible = False
    citem2.visible = False
    citem3.visible = False
    outcome.visible = False
    app.update()

def rock():
    item1.enabled = False
    item2.enabled = False
    item3.enabled = False
    computer_choice = random.randrange(1, 3)
    item2.visible = False
    item3.visible = False
    if computer_choice == 1:
        citem1.visible= True
        outcome.image = "draw.png"
        outcome.visible = True
    elif computer_choice == 2:
        citem2.visible= True
        outcome.image = "win.png"
        outcome.visible = True
    else:
        citem3.visible= True
        outcome.image = "lose.png"
        outcome.visible = True

def paper():
    item1.enabled = False
    item2.enabled = False
    item3.enabled = False
    computer_choice = random.randrange(1, 3)
    item1.visible = False
    item2.visible = False
    if computer_choice == 1:
        citem1.visible= True
        outcome.image = "win.png"
        outcome.visible = True
    elif computer_choice == 2:
        citem2.visible= True
        outcome.image = "lose.png"
        outcome.visible = True
    else:
        citem3.visible= True
        outcome.image = "draw.png"
        outcome.visible = True

def scissors():
    item1.enabled = False
    item2.enabled = False
    item3.enabled = False
    computer_choice = random.randrange(1, 3)
    item1.visible = False
    item3.visible = False
    if computer_choice == 1:
        citem1.visible= True
        outcome.image = "lose.png"
        outcome.visible = True
    elif computer_choice == 2:
        citem2.visible= True
        outcome.image = "draw.png"
        outcome.visible = True
    else:
        citem3.visible= True
        outcome.image = "win.png"
        outcome.visible = True

app = App (title  = "Rock, Paper, Scissors Shoot!!")
app.bg = "Blue"
board = Box(app, layout="grid")
item1 = PushButton (board, image="rock.png", grid=[1, 1], command = rock)
item2 = PushButton (board, image="sisers.png", grid=[2, 1], command = scissors)
item3 = PushButton (board, image="paper.png", grid=[3, 1], command = paper)
vs = Picture (board, image="VS.png", grid=[2, 2])
citem1 = Picture (board, image="rock.png", grid=[1, 3], visible = False)
citem2 = Picture (board, image="sisers.png", grid=[2, 3], visible = False)
citem3 = Picture (board, image="paper.png", grid=[3, 3], visible = False)
outcome = PushButton(board, image="win.png", grid= [2, 4], visible = False, command = redraw)



app.display()