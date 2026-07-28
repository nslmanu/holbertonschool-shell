#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
lastdigit = int(repr(number)[-1])

if number < 0:
    lastdigit2 = lastdigit * -1
else:
    lastdigit2 = lastdigit * 1
if lastdigit2 > 5:
    print(f"Last digit of {number} is {lastdigit2} and is greater than 5")
elif lastdigit2 == 0:
    print(f"Last digit of {number} is {lastdigit2} and is 0")
else:
    print(f"Last digit of {number} is {lastdigit2} and is less than 6 and not 0")

