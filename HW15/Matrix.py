# Возьмите задачу из прошлых домашних заданий.
# Добавьте к ней логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging


logging.basicConfig(filename='Logger.log',
                    filemode='w',
                    encoding='utf-8',
                    format='{asctime} {levelname:<8} function "{funcName}()" line number{lineno:>3d} : {msg}',
                    style='{',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

class Matrix:

    def __init__(self, matr):
        self._matr = matr

    def get_matrix(self):
        return self._matr

    def __add__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(f'Addition operation is impossible! Matrices have different sizes!'
                         f'[{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}]')
            return 'Addition operation is impossible! Matrices have different sizes!'
            # raise ValFormatError

        else:
            new_matr = Matrix([[self._matr[i][j] + other._matr[i][j] for j in range(len(self._matr[0]))]
                               for i in range(len(self._matr))])
            logger.info(f'Addition:  {self._matr} + {other._matr} = {new_matr}  ')
            return new_matr

    def __mul__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(f'Multiplication operation is impossible! Matrices have different sizes!'
                         f'[{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}]')
            return 'Multiplication operation is impossible! Matrices have different sizes!'
            # raise ValFormatError
        else:
            new_matr = [[sum(i * j for i, j in zip(i_row, j_col)) for j_col in zip(*other._matr)]
                        for i_row in self._matr]
            logger.info(f'Multiplication:  {self._matr} * {other._matr} = {new_matr}  ')
            return Matrix(new_matr)

    def __eq__(self, other):
        if len(self._matr) != len(other._matr) or len(self._matr[0]) != len(other._matr[0]):
            logger.error(f'Comparison operation is impossible! Matrices have different sizes!'
                         f'[{len(self._matr)}][{len(self._matr[0])}] !=  [{len(other._matr)}][{len(other._matr[0])}]')
            return 'Comparison operation is impossible! Matrices have different sizes!'
        # raise ValFormatError
        else:
            for i in range(len(self._matr)):
                for j in range(len(self._matr[0])):
                    if self._matr[i][j] != other._matr[i][j]:
                        return f'Matrices are not equal {self._matr} != {other._matr}'
            logger.info(f'Comparison: Matrices are equal {self._matr} = {other._matr} ')
            return f'Matrices are equal {self._matr} = {other._matr}'

    def __str__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i]) + '\n'
        return s

    def __repr__(self):
        s = ''
        for i in range(len(self._matr)):
            s += str(self._matr[i])
        return s


if __name__ == '__main__':

    m_1 = [[1, 2, 4],
           [5, 6,  8],
           [2, 5, -2],
           [10, 5, 0]]

    m_2 = [[1, 2, 4],
           [5, 6,  3],
           [5, 6,  8],
           [-2, 2, 0]]

    m_3 = [[7, 2, 4, 5],
           [5, 1, 8, 0],
           [5, 5, -7, 1]]

    m_4 = [[1, 2, 4, 5, 0],
           [5, 6, 8, 0, 0],
           [5, 0, -7, 1, 0]]

    print("Addition_1:")
    print(Matrix(m_1) + Matrix(m_2))
    print("Addition_2:")
    print(Matrix(m_3) + Matrix(m_1))

    print("Comparison_1:")
    print(Matrix(m_1) == Matrix(m_1))
    print("Comparison_2:")
    print(Matrix(m_1) == Matrix(m_4))

    print("Multiplication_1:")
    print(Matrix(m_1) * Matrix(m_2))
    print("Multiplication_2:")
    print(Matrix(m_1) * Matrix(m_4))
