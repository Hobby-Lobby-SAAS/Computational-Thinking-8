import turtle, math, time, random
from utils import *
# The goal of the game is to tag the other character more times than you get tagged, in 30 seconds or first to 5
# Section 1: Setup
# TODO - create your player character and any other sprites
# TODO - set your background
# TODO - set the starting value for your variables
s1 = create_sprite("LeBron", 200, 0)
s2 = create_sprite("Bronny", -200, 0)
set_background("Lakers")
sprite_list = []

Bronny_tags = 0
LeBron_tags = 0
who_is_it = "Bronny"
timer = 0
message_sprite = create_sprite("alien", -200, 100 )
message_sprite.hideturtle()


# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control
def move_up_1():
    x = s1.xcor()
    y = s1.ycor() + 5
    s1.goto(x,y)
window.onkeypress(move_up_1, "w")
def move_down_1():
    x = s1.xcor()
    y = s1.ycor() - 5
    s1.goto(x,y)
window.onkeypress(move_down_1, "s")
def move_left_1():
    x = s1.xcor() - 5
    y = s1.ycor()
    s1.goto(x,y)
window.onkeypress(move_left_1, "a")
def move_right_1():
    x = s1.xcor() + 5
    y = s1.ycor()
    s1.goto(x,y)
window.onkeypress(move_right_1, "d")


def move_up_2():
    x = s2.xcor()
    y = s2.ycor() + 5
    s2.goto(x,y)
window.onkeypress(move_up_2, "Up")
def move_down_2():
    x = s2.xcor()
    y = s2.ycor() - 5
    s2.goto(x,y)
window.onkeypress(move_down_2, "Down")
def move_left_2():
    x = s2.xcor() - 5
    y = s2.ycor()
    s2.goto(x,y)
window.onkeypress(move_left_2, "Left")
def move_right_2():
    x = s2.xcor() + 5
    y = s2.ycor()
    s2.goto(x,y)
window.onkeypress(move_right_2, "Right")

# Section 3: Game Loop
window.listen()
for i in range(10000000000):
    
    if get_distance(s1,s2) <100:
        if who_is_it == "Bronny":
            Bronny_tags += 1
            who_is_it = "LeBron"
            s1.goto(200,0)
            s2.goto(-200,0)
        elif who_is_it == "LeBron":
            LeBron_tags += 1
            who_is_it = "Bronny"
            s1.goto(200,0)
            s2.goto(-200,0)
    message_sprite.clear()
    message_sprite.write(f"Bronny_tags: {Bronny_tags}\n LeBron_tags: {LeBron_tags}\n who_is_it: {who_is_it}\n timer:{timer}" , font = ("Arial",30, "normal"))
    if Bronny_tags >= 5: 
     message_sprite.write("Bronny Wins Yayayyaayayya", font = ("Arial",30, "normal"))
    elif LeBron_tags >= 5:
     message_sprite.write("LeBron wins yyayayayayayayayyaya", font = ("Arial",30, "normal"))
    
    if i % 100 == 0:
         timer += 1
    
    if timer >= 30 and Bronny_tags >= LeBron_tags:
        message_sprite.clear()
        message_sprite.write("Bronny Wins Yayayyaayayya", font = ("Arial",30, "normal"))
    elif timer >= 30 and LeBron_tags > Bronny_tags:
        message_sprite.write("LeBron wins yyayayayayayayayyaya", font = ("Arial",30, "normal"))



    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")