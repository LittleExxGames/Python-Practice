import math

while True:
    inp = 0
    while True:
        try :
            inp = int(input("Please enter a whole number (i.e., an integer): "))
            break
        except ValueError:
            print("Please enter a valid number.\n")
    print("The number you entered is ", inp)
    if inp % 2 == 0:
        print("%d is an even number." % inp)
    else:
        print("%d is an odd number." % inp)
    if math.sqrt(inp) % 1 == 0:
        print("%d does have a perfect square root." % inp)
    else:
        print("%d does not have a perfect square root." % inp)
    factors = []
    for i in range(1, inp + 1):
        if inp % i == 0:
            factors.append(i)
    sFactors = ""
    for fac in factors:
        sFactors += str(fac)
        if fac != factors[-1]:
            sFactors += ", "
    print("The factors of %d are %s." % (inp, sFactors))
    inp = input("Would you like to enter another number? (y/n): ")
    if inp.lower() != 'y':
        print("Thank you for playing!")
        break
