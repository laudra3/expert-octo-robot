import random

classes=["math","english","science"]
firstname=input("what is your first name?")
lastname=input("what is your last name?")

for var in classes:
    gpa = random.randint(255, 400) / 100
    if gpa<=2.5:
        print("you failed this class")
    elif gpa>= 2.6 and gpa<3.0:
        print("you get a B")
    else:
        print("you get a A")
        print("first name is", firstname, "and last name is", lastname, "with class",var, "and gpa", gpa)