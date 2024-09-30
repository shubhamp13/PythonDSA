#Type casting
#It is the process of converting one type of data into another type
# str(), int(), float(), bool()
#Empty String in python is false
#For any non empty string its conversion will be always true

name='Shubham Puri'
age=26
price=358324656.256
isAvailabe=True


print(type(name))
print(type(isAvailabe))

print(type(price))
price=int(price)
print(price)
print(type(price))

print(type(age))
age=float(age)
print(age)
print(type(age))


print(type(age))
age=str(age)
print(age)
print(type(age))

name=bool(name)
print(name)
name=''
name=bool(name)
print(name)
