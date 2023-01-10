#Program allow user to enter number
#Python Program to Check if a Number is Positive, Negative or 0
def positiveNegativeZero():
    a = int(input("Plz enter a number: "))
    if a>0:
        print(f"Number is Positive: {a}")
    elif a<0:
        print(f"Number is Negative: {a}")
    else:
        print("Zero")



positiveNegativeZero()