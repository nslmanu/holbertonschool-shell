#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

lastdigit = int(repr(number)[-1])

if lastdigit > 5:
    print(f"Last digit of {number} is {lastdigit} and is greater than 5")
elif lastdigit == 0:
    print(f"Last digit of {number} is {lastdigit} and is 0")
else:
    print(f"Last digit of {number} is {lastdigit} and is less than 6 and not 0")




#print(f"Last digit of {number} is {lastdigit} and is")


#    if the last digit is greater than 5: the string and is greater than 5
#    if the last digit is 0: the string and is 0
#    if the last digit is less than 6 and not 0: the string and is less than 6 and not 0


#print number[:-1] 

#n = 56789
#lastdigit = int(repr(n)[-1])

#if number > 0:
#    print(f"{number} is positive")
#elif number == 0:
#    print(f"{number} is zero")
#else:
#    print(f"{number} is negative")

#Last digit of -9200 is 0 and is 0
#Last digit of 4205 is 5 and is less than 6 and not 0
