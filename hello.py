print("Hello World!")

# variables
age = 20
print(age)  #20
age = 30
print(age) #30

price = 20.99
firstName = "Rajib"
isLoggedIn = True


# input
# name = input("What is your name? ")
# print("Hello " + name)


# Type Conversion
# birthYear = input("Enter your Birth Year: ")
# age = 2021 - int(birthYear)
# print(age)

# Sum of Two nums
# num1 = input("Num1: ")
# # num1 = float(input("Num1: "))
# num2 = input("Num2: ")
# print(num1+num2)
# sum = float(num1) + float(num2)
# print(sum)
# print("Sum: " + str(sum))


# Strings
intro = "My Name is Rajib Mondal"
print(intro.upper())
print(intro)
print(intro.find('n')) #19
print(intro.find('is')) #8
print(intro.replace('is', '2'))
print("Rajib" in intro) #True


# Arithmetic Operators
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
print(10 ** 3)
# Augmented Assignment Operator
x = 3
x += 3

# Logical Operators
price = 5
print(price > 10 or price < 30) #True
print(price > 10 and price < 30) #False
print(not price > 10) #True

# if Statements

temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
elif temperature > 10:
    print("It's abit cold day")
else:
    print("It's a cold day")
print("Done")

# while loops
i = 1
while i <= 1_00:
    print(i)
    i += 1

i = 1
while i <= 10:
    print(i * '*')
    i += 1


# Lists or arrays
names = ["John", "Bob", "Rajib", "Sam", "Marry"]
print(names)
print(names[2])
print(names[-2]) #Sam
names[0] = "Jon"
print(names[0:3]) #Excluding the end index

# List Methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, -1)
numbers.remove(3)
print(1 in numbers)
print(10 in numbers)
print(len(numbers))
numbers.clear()

# for loops  -> break and continue as well
numbers = [1, 2, 3, 4, 5, 6]
for item in numbers:
    print(item)

# The range function
numbers = range(5)
print(numbers)
for number in numbers:
    print(number)

numbers = range(10, 15)
for number in numbers:
    print(number)

numbers = range(5, 10, 2)
for number in numbers:
    print(number)


for number in range(5, 10, 2):
    print(number)

# Tuples
numbers = (1, 2, 3, 3, 3)
print(numbers.index(3))
# numbers[1] = 5 #Error -> Tuples are immutable or unchangeable
print(numbers.count(3)) #3 -> count of 3

# Sets -> similar to tuple but stores only unique values
numbers = {1, 2, 3, 3, 3}
print(numbers)
# can only be iterate through loop


# Dictionary
marks = {
    "English": 95,
    "Chemistry": 92
}
print(marks["Chemistry"])
marks["physics"] = 97
marks["english"] = 97

# Functions
# 1. in-built functions
# 2. Module functions
# 3. User defined functions

import math
print(dir(math))

from math import sqrt
print(sqrt(16))

from math import *


def printSum(first, second = 6):
    print(first + second)

printSum(1, 4)
printSum(6)