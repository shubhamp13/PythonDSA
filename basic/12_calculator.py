num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))

operator=input("Enter operator: (+,-,*,/)")

if operator=='+':
    print(f"The Sum of {num1} and {num2} is {num1+num2}")
elif operator=='-':
    print(f"The difference between {num1} and {num2} is {num1-num2}")
elif operator=='*':
    print(f"The product of {num1} and {num2} is {num1*num2}")
elif operator=='/':
    print(f"The division of {num1} and {num2} is {num1/num2}")
else:
    print("Invalid operator")