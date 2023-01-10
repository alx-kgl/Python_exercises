#Write a function that prints all integers of a list, in reverse order.
# range(start, stop, -step) 
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list),0,-1):
        print("{}".format(i))


print_reversed_list_integer([1, 2, 3, 9, 5])

