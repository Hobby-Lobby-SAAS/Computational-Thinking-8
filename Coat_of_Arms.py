# Section 1 - Your code
from utils import *
set_background("winter")

s1 = create_sprite("cardinal", 200, 200)
s2 = create_sprite("Calvin", -200, 200)
s3 = create_sprite("fox", -200, -200)
s4 = create_sprite("Ireland", 200, -200)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("Hobbes",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Never back down",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()