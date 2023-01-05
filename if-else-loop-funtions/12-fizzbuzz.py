#Write a function that prints the numbers from 1 to 100 separated by a space.
def fizzbuzz(num):
    if num%15:
        print("FizzBuzz")
    elif num%3:
        print("Fizz")
    elif num%5:
        print("Buzz")
    else:
        print("Is neither Multiple of 3 or 5")
