my_list = [1, 90, 2, 13, 34, 5, -13, 3]

def max_integer(my_list=[]):
    if len(my_list) ==0:
        print("None")
        return
    max = 0
    for num in my_list:
        if(num>max):
            max = num
    print("Max: {} ".format(max))


max_integer(my_list)
    
                   