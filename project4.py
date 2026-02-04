import turtle, time, random
from utils import *
# The goal of the game is to get as many seahawks, and jsn's as you can!
# Section 1 - setup
# TODO - set a background using set_background()
set_background("Stadium")
# TODO - create at least two variables and set their starting value. ex: cookies = 0
seahawks = 0
jsn = 0
cost = 10
seahawks_list = []
# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -200,100)
message_sprite.hideturtle()



# Section 2 - controls
# TODO - define an action. ex: def my_control()
def get_seahawks():
    global seahawks, seahawks_list
    seahawks += 1
    x= random.randint (-200, 200)
    y= random.randint (-200,200)
    sprite1 = create_sprite ("seahawks",x,y)
    seahawks_list.append (sprite1)

window.onkeypress (get_seahawks, "space")
# if you press "space" then you get a seahawk.
def get_jsn():
    global seahawks, jsn, cost, seahawks_list
    if seahawks >= cost:
        seahawks -= cost
        for i in range(cost):
            sprite1 = seahawks_list.pop()
            sprite1.hideturtle()

        cost=cost *2
        jsn += 1
        x = -400 +120*jsn
        y = -250
        create_sprite ("jsn", x, y)

window.onkeypress(get_jsn, "j")
# if you press "j" then you get a jsn





# Section 3 - game loop
window.listen()
for i in range(1000000000):
    message_sprite.clear()
    message_sprite.write(f"seahawks: {seahawks}\n cost:{cost}\n jsn:{jsn}", font = ("Arial",30, "normal"))
    
    # seahawks += jsn 

    if i % 10 == 0: 
    
        for j in range (jsn):
            get_seahawks ()
    # TODO - put any automatic actions here
    



    # OPTIONAL - use the message sprite to say a message
    # message_sprite.clear()
    # message_sprite.write("Hello")

    time.sleep(0.01)
    window.update()