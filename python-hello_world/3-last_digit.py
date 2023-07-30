#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
#str("Last digit of")
#def "last_digit_of"(number):
#print(number)
last_digit_uns = abs(number) % 10
if number < 0:
        last_digit = -last_digit_uns 
else:
        last_digit = last_digit_uns
if last_digit > 5:
        print("Last digit of " + str(number)  + " is " + str(last_digit)  + " and is greater than 5")
if last_digit == 0:
        print("Last digit of " + str(number)  + " is " + str(last_digit)  + " and is 0")
elif (last_digit < 6)  & (last_digit!= 0):
        print("Last digit of " + str(number)  + " is " + str(last_digit)  + " and is less than 6 and not 0")

    
