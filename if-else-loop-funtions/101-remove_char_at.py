# Write a function that creates a copy of the string, removing the character at the position n (not the Python way, the “C array index”).

def remove_char_at(str, n):
     arr=  [*str]
     print(arr)
     arr.pop(n)
     newString = "".join(arr)
     return newString

   

