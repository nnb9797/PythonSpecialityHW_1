# 1. Напишите функцию для транспонирования матрицы

matrix = [[1, 2, 3], [11, 12, 13], [21, 22, 23]]

"""Matrix printing function"""


def print_matrix(input_matrix):
    for column in input_matrix:
        for row in column:
            print(row, "\t", end="")
        print()

print_matrix(matrix)

print()

"""Matrix transposition function"""


def matrix_transpositions(input_matrix):
    new_matrix = []
    list_in_matrix = []
    count_start = 0
    count_stop = 1
    while count_start < len(matrix):
        for column in input_matrix:
            for row in column[count_start:count_stop:]:
                list_in_matrix.append(row)
        new_matrix.append(list_in_matrix)
        list_in_matrix = []
        count_start += 1
        count_stop += 1
    return new_matrix

print_matrix(matrix_transpositions(matrix))