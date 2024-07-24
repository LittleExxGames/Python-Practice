import math

radius = 0
while True:
    try :
        radius = float(input("What is the radius of the circle? "))
        break
    except ValueError:
        print("Please enter a valid number\n")
        
d = 2 * radius
c = round(2 * math.pi * radius, 2)
a = round(math.pi * (radius ** 2), 2)
print("A circle with a radius of {} units will have a diameter of {} units, a circumference of {} units and an area of {} square units.".format(radius, d, c, a))
        
