# Quadratic equation 
# ax^2b^@  + bx + c = 0

# D = b^2-4*a*c

# x1 =-b+sqrt(D)/2*a
# x2 =-b-sqrt(D)/2*a
import math
a = int(input("type value of a: "))
b = int(input("type value of b: "))
c = int(input("type value of c: "))

d = math.pow(b,2) - 4*a*c
if d > 0:
    x1 = -b + math.sqrt(d)/2*a
    print(f"the X1:{x1}")
    x2 = -b - math.sqrt(d)/2*a
    print (f"x2 is :{x2}")
elif d == 0:
    x1 = -b/2*a
    print(f"x1 = x2 :{x1}")
else:
    print("Deleta is less than zero")