# variable is container for value in which we store the value
# (string,integer,float,double)
from statistics import quantiles

# Strings
first_name='Shubham'
last_name='Puri'
print(first_name)
print(last_name)
print(type(first_name))#<class 'str'>

# Printing with f
print(f"My First Name is {first_name} and last name is {last_name}")

# Integers
age=26
quantity=50
print(f"My Age is {age}")
print(f"My Quantity is {quantity}")
print(type(age))#<class 'int'>

# Float

price=352.255
print(f"Product Price is${price}")
print(type(price)) #<class 'float'>

#boolean

isAvailabe=False
print(isAvailabe)
print(type(isAvailabe))#<class 'bool'>


if isAvailabe:
    print("You are eligible")
else:
    print("You are not eligible")