#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
print(number)
if number > 0:
    print("is positive")
if number == 0:
    print("is  zero")
else:
    print("is negative")