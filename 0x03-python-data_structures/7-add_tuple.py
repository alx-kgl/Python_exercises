tuple_a = (1, 89)
tuple_b = (88, 11)
def add_tuple(tuple_a=(), tuple_b=()):
    value_a = tuple_a[0] + tuple_b[0]
    value_b = tuple_a[1] + tuple_b[1]
    print((value_a,value_b))




add_tuple(tuple_a, tuple_b)