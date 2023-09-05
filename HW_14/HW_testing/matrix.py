"""Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц"""
import doctest


class Matrix:

    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.matrix = [[0] * columns for _ in range(rows)]

    def __str__(self):
        result = ""
        for row in self.matrix:
            result += " ".join(str(element) for element in row) + "\n"
        return result

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        return False

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.rows == other.rows and self.columns == other.columns:
                result_matrix = Matrix(self.rows, self.columns)
                for i in range(self.rows):
                    for j in range(self.columns):
                        result_matrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
                return result_matrix
            else:
                raise ValueError("Matrices must have the same size for addition.")
        else:
            raise TypeError("You can only add matrices.")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.columns == other.rows:
                result_matrix = Matrix(self.rows, other.columns)
                for i in range(self.rows):
                    for j in range(other.columns):
                        for k in range(self.columns):
                            result_matrix.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
                return result_matrix
            else:
                raise ValueError("Number of columns in the first matrix must match the number of"
                                 " rows in the second matrix for multiplication.")
        elif isinstance(other, int) or isinstance(other, float):
            result_matrix = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result_matrix.matrix[i][j] = self.matrix[i][j] * other
            return result_matrix
        else:
            raise TypeError("Matrix can be multiplied either by another matrix or a scalar value.")


if __name__ == "__main__":
    doctest.testmod(verbose=True)
