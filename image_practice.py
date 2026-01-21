# Section 1 - Your code
from utils import *
set_background("Bahamas")

s1 = create_sprite("fishy", 100, 100)
s2 = create_sprite("LEBRONNNNNNNNN", -100, 100)
s2 = create_sprite("Jeff", -100, -100)
s2 = create_sprite("Cally", 100, -100)

message1 = create_sprite("alien",-200,200)
message1.color("red")
message1.write("King Harper",font = ("Arial", 40, "normal"))
message1.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()