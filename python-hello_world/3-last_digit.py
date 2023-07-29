#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
#str("Last digit of")
#def "last_digit_of"(number):
#print(number)
#last_digit = number % 10
s_num = str(number)
last_digit = s_num[-1]
last_digit = int(last_digit)
if last_digit > 5:
        print("Last digit of " + str(number)  + " is " + str(last_digit)  + " and is greater than 5")
if last_digit == 0:
        print("Last digit of " + str(number)  + " is " + str(last_digit)  + " and is 0")
elif (last_digit < 6)  & (last_digit!= 0):
        print("Last digit of " + str(number)  + " is " + str(last_digit)  + " and is less than 6 and not 0")

    
