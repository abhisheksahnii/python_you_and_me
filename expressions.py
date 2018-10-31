#!/usr/bin/env python3

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

x = a - b / 3 + c * 2 - 1
y = a - b / (3 + c) * (2 - 1)
z = a - (b / (3 + c) * 2) - 1
print ("X = ",x)
print ("Y = ",y)
print ("Z = ",z)
