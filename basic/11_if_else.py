#if ===>conditions statement

age=int(input("Enter your age:"))

if age>0:
    if age>=18 and age<=65:
        print("You are eligible for driving")
    else:
        print("You are not eligible for driving")
else:
    print("Please enter a valid age")