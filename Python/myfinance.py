hw = 0.0
rate = 0.0
grossPay = 0.0
revenue = []
expenses = []
finished = False
def calcGrossPay():
    global hw, rate, grossPay
    while True:
        try:
            hw = float(input("What is your hourly wage? "))
            break
        except ValueError:
            print("Please provide a valid number")
            continue
    while True:
        try:
            rate = float(input("How many hours did you work? "))
            break
        except ValueError:
            print("Please provide a valid number")
            continue
    grossPay = hw * rate
    return grossPay
    
def calcNetPay():
    calcGrossPay()
    print("\nGross Pay: $%.2f(%.1f hours @ %.2f/hr)" % (grossPay, rate, hw))
    print("Federal Tax: $%.2f" % (grossPay * 0.1))
    print("State Tax: $%.2f" % (grossPay * 0.05))
    print("Social Security: $%.2f" % (grossPay * 0.06))
    netPay = grossPay - (grossPay * 0.1) - (grossPay * 0.05) - (grossPay * 0.06)
    print("Net pay: $%.2f" % netPay)
    return True
def promptRevenue():
    done = False
    while done == False:
        type = input("Enter transaction name: ")
        while True:
            try:
                inp = float(input("Enter amount (use negative sign for expense): "))
                if inp >= 0:
                    revenue.append((type, inp))
                else:
                    expenses.append((type, inp))
                break
            except ValueError:
                print("Please provide a valid number")
                continue
        while True:
            inp = input("Another? (Y/N): ")
            if inp.lower() == "n":
                done = True
                break
            elif inp.lower() == "y":
                break
            else:
                print("Invalid choice")
    return True
def showDiscretionaryIncome():
    total = 0
    cost = 0
    for type, amount in revenue:
        total += amount
    for type, amount in expenses:
        cost += amount
    print("\nRevenu: $%.2f  Expenses: $%.2f Discretionary: $%.2f" % (total, cost, total + cost))
    return True
def exitP():
    print("\nThanks for using My Finance!")
    global finished
    finished = True
    return False
while finished == False:
    menu = {"1": calcNetPay, "2": promptRevenue, "3": showDiscretionaryIncome , "4" : exitP}
    print("\n1-Calculate net pay")
    print("2-Enter revenue or expense")
    print("3-Show discretionary income")
    print("4-Exit")
    choice = input("Choice: ")
    if choice in menu:
        if not menu[choice]():
            break
    else:
        print("Invalid choice")