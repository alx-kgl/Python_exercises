#Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
my_list = [1, 2, 3, 4, 5]
idx = 3
element = 9
def new_in_list(my_list, idx, element):
    copyArr = []
    for i in range(0,len(my_list)):
        if(i == idx):
            copyArr.insert(i,element)
        else:
            copyArr.append(my_list[i])
    print(my_list)
    print(copyArr)



new_in_list(my_list,idx,element)
