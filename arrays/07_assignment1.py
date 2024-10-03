#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Even Odd Number
def evenOdd(num):
    return num % 2 == 0


num = int(input("Enter Number"))

if evenOdd(num):
    print(f" {num} is even number");
else:
    print(f" {num} is odd number");


# In[8]:


# Prime Number:

def primeNumber(num):
    for x in range(2, (num // 2) + 1):
        if num % x == 0:
            return False
    return True


number = int(input("Enter Number"))

if primeNumber(number):
    print(f" {number} is Prime Number")
else:
    print(f"{number} is not prime Number")


# In[11]:


# Factorial Of Number

def factorial(num):
    fact = 1
    for x in range(1, num + 1):
        fact *= x
    return fact


number = int(input("Enter Number"))

print(f"Factorial of {number} is {factorial(number)}")


# In[23]:


# Perfect Number
def perfect_number(num):
    add = 0
    for x in range(1, (num // 2) + 1):
        if num % x == 0:
            add += x
    return add == num


number = int(input("Enter Number"))
if perfect_number(number):
    print(f"{number} is perfect number")
else:
    print(f"{number} is not perfect number")


# In[28]:


# reverse the number
def reverse_number(number):
    reverse = 0
    while number != 0:
        rem = number % 10
        reverse = reverse * 10 + rem
        number = number // 10
    return reverse


print(reverse_number(2342))


# In[32]:


# palindrome number
def palindrome_number(num):
    temp = num
    reverse = 0
    while temp != 0:
        rem = temp % 10
        reverse = reverse * 10 + rem
        temp = temp // 10
    return reverse == num


num = int(input("Enter Number"))
if palindrome_number(num):
    print(f"{num} is palindrome")
else:
    print(f"{num} is not palindrome")


# In[34]:


# square of number
def square_number(num):
    return num * num


num = int(input("Enter Number"))
print(f"Square root of {num} is {square_number(num)}")


# In[35]:


# No Of Digits
def no_of_digits(num):
    count = 0
    while num != 0:
        count += 1
        num = num // 10
    return count


number = int(input("Enter Number"))

print(f"No Of Digits {number} is {no_of_digits(number)}")


# In[43]:


# Armstrong Number
def no_of_digits(num):
    count = 0
    while num != 0:
        count += 1
        num = num // 10
    return count


def power_of_number(a, b):
    power = 1
    for x in range(0, b):
        power *= a
    return power


def armstrong_number(num):
    add = 0
    temp = num
    power = no_of_digits(num)
    while temp != 0:
        rem = temp % 10
        add = add + power_of_number(rem, power)
        temp = temp // 10
    return add == num


print(armstrong_number(103))


# In[47]:


def sum_of_digits(num):
    add = 0
    while num != 0:
        rem = num % 10
        add += rem
        num = num // 10
    return add


number = int(input("Enter Number"))
print(f"Sum Of Digits Is {sum_of_digits(number)}")

# In[ ]:




