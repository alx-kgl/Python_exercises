# Write a function that deletes the item at a specific position in a list.
my_list = [1, 2, 3, 4, 5]
idx = 3

def delete_at(my_list=[], idx=0):
    for i in range(0,len(my_list)):
        if(i == idx):
            my_list.remove(my_list[idx])
    print(my_list)
delete_at(my_list,idx)