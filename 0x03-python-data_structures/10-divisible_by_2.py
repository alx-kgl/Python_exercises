# Write a function that finds all multiples of 2 in a list.


my_list = [0, 1, 2, 3, 4, 5, 6]

def divisible_by_2(my_list=[]):
    new_list = []
    for num in my_list:
        if num % 2 ==0:
            new_list.append(True)
        else:
            new_list.append(False)
    print(new_list)


divisible_by_2(my_list)