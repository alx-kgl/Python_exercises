# Write a function that prints a matrix of integers.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_matrix_integer(matrix=[[]]):
    for raw in matrix:
        print("{} {} {}$".format(*raw))


print_matrix_integer(matrix)