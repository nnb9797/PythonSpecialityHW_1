import unittest
from HW14.HW_testing import matrix

class TestCaseName(unittest.TestCase):
    def setUp(self):
        self.A = matrix.Matrix(2, 3)
        self.A.matrix = [[1, 2, 3], [4, 5, 6]]
        self.B = matrix.Matrix(3, 2)
        self.B.matrix = [[7, 8], [9, 10], [11, 12]]
        self.C = matrix.Matrix(2, 2)
        self.C.matrix = [[1, 2], [3, 4]]
        self.G = matrix.Matrix(2, 2)
        self.G.matrix = [[3, 4], [5, 2]]
        self.H = matrix.Matrix(2, 3)
        self.H.matrix = [[1, 2, 3], [4, 5, 6]]

    def test1(self):
        self.assertFalse(self.A == self.B)  # матрицы неравны

    def test2(self):
        self.assertFalse(self.C == self.G)  # матрицы неравны

    def test3(self):
        self.assertTrue(self.A == self.H)  # матрицы равны

    def test4(self):
        result = "4 6\n8 6\n"
        self.assertEqual(str(self.C + self.G), result)  # сложение матриц

    def test5(self):
        with self.assertRaises(ValueError):  # выбрасывается исключение при сложении матриц разных размерностей
            self.A + self.B

    def test6(self):
        result = "58 64\n139 154\n"
        self.assertEqual(str(self.A * self.B), result)  # умножение матриц

    def test7(self):
        with self.assertRaises(ValueError):
            self.A * self.H  # выбрасывается исключение при умножении матриц разных размерностей

    def test8(self):
        result = "13 8\n29 20\n"
        self.assertEqual(str(self.C * self.G), result)  # умножение матриц

    def test9(self):
        result = "2 4 6\n8 10 12\n"
        self.assertEqual(str(self.H * 2), result)  # умножение матрицы на число


if __name__ == "__main__":
    unittest.main()
