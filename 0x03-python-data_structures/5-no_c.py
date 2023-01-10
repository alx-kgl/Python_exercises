# Write a function that removes all characters c and C from a string.

def no_c(my_string):
    new_str = ''
    for s in my_string:
        if s == 'c' or s == 'C':
            continue
        else:
            new_str += s   
    return new_str


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))