print("Holiday personality test!!")
christmas_points=0
halloween_points=0
thanksgiving_points=0

print("Please use uppercase letters when answering questions.")
answer1 = input("do you prefer A chocolate or B candy")
if answer1 == "A":
    christmas_points +=1
    thanksgiving_points +=1
elif answer1 == "B":
    halloween_points += 2

answer2 = input("Do you prefer spending time with A family or B friends")
if answer2 == "A":
    christmas_points +=1
    thanksgiving_points +=2
elif answer2 == "B":
    halloween_points +=1

answer3 = input ("Do you prefer A Hot chocolate B turkey or C pumpkin pie")
if answer3 == "A":
    christmas_points +=1
elif answer3 == "B":
    thanksgiving_points +=1
elif answer3 == "C":
    halloween_points +=1

answer4 = input ("Do you prefer A home alone B a charlie brown thanksgiving or C hocus pocus")
if answer4 == "A":
    christmas_points +=1
elif answer4 == "B":
    thanksgiving_points +=1
elif answer4 == "C":
    halloween_points +=1

answer5 = input("Do you prefer A snow B rainy or C crisp")
if answer5 == "A":
    christmas_points +=1
elif answer5 == "B":
    thanksgiving_points +=1
elif answer5 == "C" or answer5 == "c":
    halloween_points +=1

print(f"Your score is {christmas_points}, {thanksgiving_points}, and {halloween_points}")
if christmas_points >= thanksgiving_points and christmas_points >= halloween_points:
    print("wow you really love christmas, hope you enjoy this one!!")
if thanksgiving_points >= christmas_points and thanksgiving_points >= halloween_points:
    print("Wow you love thanksgiving, I hope you get to spend it with your family and friends!!")
if halloween_points >= christmas_points and halloween_points >= thanksgiving_points:
    print("wow you love halloween, hope you get lots of candy!!")
