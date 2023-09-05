import pytest
from HW_14.HW_testing import matrix


class TestMatrixOperations:

    def test_not_equals(self):
        self.A = matrix.Matrix(2, 3)
        self.A.matrix = [[1, 2, 3], [4, 5, 6]]
        self.B = matrix.Matrix(3, 2)
        self.B.matrix = [[7, 8], [9, 10], [11, 12]]
        assert not str(self.A) == str(self.B)  # матрицы неравны

    def test_not_equals1(self):
        self.C = matrix.Matrix(2, 2)
        self.C.matrix = [[1, 2], [3, 4]]
        self.G = matrix.Matrix(2, 2)
        self.G.matrix = [[3, 4], [5, 2]]
        assert not str(self.C) == str(self.G)  # матрицы неравны

    def test_equals(self):
        self.A = matrix.Matrix(2, 3)
        self.A.matrix = [[1, 2, 3], [4, 5, 6]]
        self.H = matrix.Matrix(2, 3)
        self.H.matrix = [[1, 2, 3], [4, 5, 6]]
        assert str(self.A) == str(self.H)  # матрицы равны

    def test_add_matrices(self):
        self.C = matrix.Matrix(2, 2)
        self.C.matrix = [[1, 2], [3, 4]]
        self.G = matrix.Matrix(2, 2)
        self.G.matrix = [[3, 4], [5, 2]]
        result = "4 6\n8 6\n"
        assert str(self.C + self.G) == result  # сложение матриц

    def test_add_dif_matrices(self):
        self.A = matrix.Matrix(2, 3)
        self.A.matrix = [[1, 2, 3], [4, 5, 6]]
        self.B = matrix.Matrix(3, 2)
        self.B.matrix = [[7, 8], [9, 10], [11, 12]]
        with pytest.raises(ValueError, match="Matrices should have the same size for addition."):
            self.A + self.B  # выбрасывается исключение при сложении матриц разных размерностей

    def test_mult_matrices(self):
        self.A = matrix.Matrix(2, 3)
        self.A.matrix = [[1, 2, 3], [4, 5, 6]]
        self.B = matrix.Matrix(3, 2)
        self.B.matrix = [[7, 8], [9, 10], [11, 12]]
        result = "58 64\n139 154\n"
        assert str(self.A * self.B) == result  # умножение матриц

    def test_mult_dif_matrices(self):
        self.A = matrix.Matrix(2, 3)
        self.A.matrix = [[1, 2, 3], [4, 5, 6]]
        self.H = matrix.Matrix(2, 3)
        self.H.matrix = [[1, 2, 3], [4, 5, 6]]
        with pytest.raises(ValueError, match="Number of columns in the first matrix must match the number "
                                             "of rows in the second matrix for multiplication."):
            self.A * self.H  # выбрасывается исключение при сложении матриц разных размерностей

    def test_mult_matrices_on_number(self):
        result = "2 4 6\n8 10 12\n"
        self.H = matrix.Matrix(2, 3)
        self.H.matrix = [[1, 2, 3], [4, 5, 6]]
        assert str(self.H * 2) == result  # умножение матрицы на число


if __name__ == '__main__':
    pytest.main(['-v'])