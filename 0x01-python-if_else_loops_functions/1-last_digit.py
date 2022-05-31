#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = number
if number < 0:
    a = number * -1
    last = a % 10
    if last != 0:
        last = last * -1
else:
    last = a % 10
if last > 5:
    print(f"Last digit of {number:d} is {last:d} and is greater than 5")
elif last < 6 and a % 10 != 0:
    print(f"Last digit of {number:d} is {last:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {last:d} and is 0")
