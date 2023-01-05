#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if (number%10)>5:
    print(f"{number} last digit is greater than 5")
elif number%10 == 0:
    print(f"{number} last number is equal to zero")
elif number%10<6:
    print(f"{number} last number is less than 6 and not equal to zero")
    