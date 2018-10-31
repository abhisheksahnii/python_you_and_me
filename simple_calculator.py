#!/usr/bin/env python3
'''
Program make a simple calculator that can add, sub, mul and div using functions
'''

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

print("Select Operation.")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print(num1,"+",num2,"=",add(num1, num2))

elif choice == 2:
    print(num1,"-",num2,"=",sub(num1, num2))

elif choice == 3:
    print(num1,"*",num2,"=",mul(num1, num2))

elif choice == 4:
    print(num1,"/",num2,"=",div(num1, num2))

else:
    print("Invalid Input.")




