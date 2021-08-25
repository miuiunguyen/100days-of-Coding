year = int(input("Which year do you want to check?"))
if (year/400) % 2 == 0:
    print("Leap Year")
elif (year/100) % 2 == 0:
    print("Leap Year")
elif (year/4) % 2 == 0:
    print("Leap Year")
else:
    print("Not leap Year")
##Solution from Udemy
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("not leap year")