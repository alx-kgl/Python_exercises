arr = [1, 2, 3, 4, 5]  
idx = 20
def element_at(my_list, idx):
    if idx> len(my_list) or idx < 0:
        return None
    else:
        return my_list[idx]

print(element_at(arr,idx))