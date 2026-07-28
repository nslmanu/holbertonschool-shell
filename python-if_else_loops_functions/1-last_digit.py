#!/usr/bin/python3
import random

#number = random.randint(-10000, 10000)
#lastdigit = int(repr(number)[-1])

#if nombre % 10 == 0: 

import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
print(f"Last digit of {number} is {last}", end="")
if last > 5:
    print(" and is greater than 5")
elif last == 0:
    print(" and is 0")
else:
    print(" and is less than 6 and not 0")


#if number < 0:
#    lastdigit2 = lastdigit * -1
#else:
#    lastdigit2 = lastdigit * 1
#if lastdigit2 > 5:
#    print(f"Last digit of {number} is {lastdigit2} and is greater than 5")
#elif lastdigit2 == 0:
#    print(f"Last digit of {number} is {lastdigit2} and is 0")
#else:
#    print(f"Last digit of {number} is {lastdigit2} and is less than 6 and not 0")

