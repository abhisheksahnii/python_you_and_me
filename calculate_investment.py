#!/usr/bin/env python3

amount = float(input("Enter the amount: "))

inrate = float(input("Enter the inrate: "))

period = int(input("Enter the period: "))

value = 0

year = 1

while year <= period:
    value = amount + (inrate * amount)
    print("Year %d Rs. %.2f" % (year, value))
    amount = value
    year = year + 1

