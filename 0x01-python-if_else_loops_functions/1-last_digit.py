#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dgt = abs(number) % 10
if number < 0:
    dgt = -dgt
print(f"Last digit of {number:d} is {dgt:d} and is ", end="")
if dgt > 5:
    print("greater than 5")
elif dgt == 0:
    print("0")
else:
    print("less than 6 and not 0")
