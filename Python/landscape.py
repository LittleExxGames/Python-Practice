import math


while True:
    l1 = float(input("What is the length of the front section? "))
    w1 = float(input("What is the width of the front section? "))
    l2 = float(input("What is the length of the rear section? "))
    w2 = float(input("What is the width of the rear section? "))
    l3 = float(input("What is the length of the left section? "))
    w3 = float(input("What is the width of the left section? "))
    l4 = float(input("What is the length of the right section? "))
    w4 = float(input("What is the width of the right section? "))
    if (l1 < 0 or w1 < 0 or l2 < 0 or w2 < 0 or l3 < 0 or w3 < 0 or l4 < 0 or w4 < 0):
        print("Please enter a positive number for the dimensions.")
    else:
        break
sum = l1 * w1 + l2 * w2 + l3 * w3 + l4 * w4
bags = sum / 2000
bagCost = int(math.ceil(bags) * 27)
hours = int(math.ceil(sum / 2500))
hoursCost = hours * 20
costTotal = bagCost + hoursCost
print("Your application has a total area of %d sq. feet. That will require %d bags of fertilizer. The cost of the fertilizer will be $%d." % (sum, math.ceil(bags), bagCost))
print("Our technicians will require %d hours to finish the job and the labor cost will be $%d. The total cost to the company will be $%d. The application will result in %.3f pounds of nitrogen and %.3f pounds of potassium being added to the soil." % (hours, hoursCost, costTotal, bags, bags * 1.125))