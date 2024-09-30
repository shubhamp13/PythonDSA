#sum of digits

number=int(input("Enter The Number"))
sum=0
temp_number=number
while temp_number !=0:
    rem= temp_number %10
    sum= sum+ rem
    temp_number//=10

print(sum)

#product of digits

mul=1
temp_number=number
while temp_number !=0:
    rem=temp_number %10
    mul*=rem
    temp_number//=10

print(f"Multiplication of Digits is {mul}")

#Reverse The Number
temp_number=number
reverse_number=0
while temp_number !=0:
    rem=temp_number %10
    reverse_number=reverse_number*10+rem
    temp_number//=10
print(f"Reversed Number is {reverse_number}")

if number == reverse_number:
    print(f"{number} is palindrome number")
else:
    print(f"{number} is not palindrome number")