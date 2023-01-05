letter = "A"

def islower(c):
    letter_code = ord(c)
    if(letter_code<90 and letter_code>65):
        print(f"{c} is Upper")
    else:
        print(f"{c} is Lower")


islower(letter) 