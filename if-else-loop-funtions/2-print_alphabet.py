# Write a program that prints the ASCII alphabet, in lowercase, not followed by a new line.

alphabetics = "abcdefghiklmnopqrstlmnxyz"

for letter in alphabetics:
    code = ord(letter)
    print(ord(letter),end='')
    