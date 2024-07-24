import turtle as t
import random as r

done = False
while done == False:
    sides = 0
    length = 0
    color = ""
    while True:
        try:
            sides = int(input('How many sides does your polygon have?(0-100)  '))
            if (sides < 0 or sides > 100):
                print("Please provide a number between 0 and 100.")
                continue
            break
        except ValueError:
            print("Please provide a valid number.")
            continue
    while True:
        try:
            length = int(input('How long are the sides of your polygon?  '))
            break
        except ValueError:
            print("Please provide a whole number.")
            continue
    
    while True:
        colorMenu = {"1": "red", "2": "orange", "3": "green", "4": "indigo", "5": "blue", "6": "purple", "7": "violet", "8": "black", "9": "gold", "10": "cyan", "11": "random"}
        print("\nWhat color would you like your polygon to be?")
        print("%-13s%-13s%-13s" % ("1-Red", "2-Orange", "3-Black"))
        print("%-13s%-13s%-13s" % ("4-Green", "5-Indigo", "6-Blue"))
        print("%-13s%-13s%-13s" % ("7-Purple", "8-Violet", "9-Gold"))
        print("%-13s%-13s" % ("10-Cyan", "11-Random"))
        colorChoice = input("Choose a color: ")
        if colorChoice in colorMenu:
            color = colorMenu[colorChoice]
            break
        else:
            print("Please provide a valid option.")
    angle = 360 / sides


    for _ in range(sides):
        if color == "random":
            t.color(r.random(), r.random(), r.random())
        else:
            t.color(color)
        t.forward(length)
        t.right(angle)

    while True:
        inp = input("Would you like to draw another polygon? (Y/N): ")
        if inp.lower() == "n":
            done = True
            break
        elif inp.lower() == "y":
            break
        else:
            print("Invalid choice")
        t.hideturtle()
        t.done()
    