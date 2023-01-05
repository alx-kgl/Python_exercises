letter = "A"

def islower(c):
    letter_code = ord(c)
    if(letter_code<122 and letter_code>97):
        print(f"{c} is Lower")
    else:
        print(f"{c} is Upper")


islower(letter)