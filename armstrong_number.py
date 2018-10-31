#!/usr/bin/env python3

sum = 0

temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //=10

if num ==sum:
    print(num,"is a Armstrong number")
else:
    print(num,"is not an Armstrong number")
