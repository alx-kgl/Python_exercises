#Write a function that prints the last digit of a number.

def print_last_digit(number):
    if number > 0:
        print(number%10)
    else:
        print((number*-1)%10)

    


print_last_digit(98)
print_last_digit(0)
print_last_digit(-1024)

