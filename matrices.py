#!/usr/bin/python3

import re
import sys

from copy import deepcopy
import utils
from utils import Utils

class MatrixException(Exception):
    pass

class Matrix:
    REG_MTRX = r'\[(?:\[(?:-?\d+[.]?[d+]?,?)+\];?)+\]'
    M_ERR_D = {
        1: 'matrix could not be empty',
        2: 'the interior parts of the matrix must be equal',
        3: 'invalid content of matrix',
        4: 'both matrices must be the same size',
        5: 'matrices should be equal for term-to-term multiplication',
        6: 'the columns of the first matrix must be equal to the rows of the second',
        7: 'power of matrix must be an integer',
        8: 'matrix must be square',
        9: 'power of matrix should be greater than 0',
        10: 'determinant is equal 0. there is no clear solution',

        11: 'matrix couldn\'t be an exponent',
        12: 'invalid matrix syntax'
        # 11: 'matrix cannot be inverted', # not used

    }

    def __init__(self, inpt):
        if inpt == '[[]]':
            raise MatrixException(Matrix.M_ERR_D[1])

        self.raw_inp = inpt[1:-1].split(';')
        self.matrix_content = self.cleaned_input

        if not self.check_uniformity():
            raise MatrixException(Matrix.M_ERR_D[2])

        self.inversed = False
        self.rows = len(self.matrix_content)
        self.cols = len(self.matrix_content[0])

    @property
    def cleaned_input(self):
        try:
            return [list(map(float, i.strip('[]').split(','))) for i in self.raw_inp]
        except ValueError:
            raise MatrixException(Matrix.M_ERR_D[3])

    def check_uniformity(self):
        return len(set(map(len, self.matrix_content))) == 1

    def check_size_equality(self, other):
        return f'{self.rows}x{self.cols}' == f'{other.rows}x{other.cols}'

    def __add__(self, other):
        if not self.check_size_equality(other):
            raise MatrixException(Matrix.M_ERR_D[4])
        for row in range(self.rows):
            self.matrix_content[row] = list(
                zip(self.matrix_content[row], other.matrix_content[row]))
            self.matrix_content[row] = list(map(sum, self.matrix_content[row]))
        return self

    def __sub__(self, other):
        if not self.check_size_equality(other):
            raise MatrixException(Matrix.M_ERR_D[4])
        for row in range(self.rows):
            other.matrix_content[row] = [i * -1 for i in other.matrix_content[row]]
            self.matrix_content[row] = list(
                zip(self.matrix_content[row], other.matrix_content[row]))
            self.matrix_content[row] = list(map(sum, self.matrix_content[row]))
        return self

    def __mul__(self, other): # input can be int float or other what about Any?
        if isinstance(other, int) or isinstance(other, float):
            return self.__rmul__(other)
        elif type(self) == type(other):
            if self.rows == other.rows and self.cols == other.cols:
                for row in range(self.rows):
                    for col in range(self.cols):
                        self.matrix_content[row][col] *= other.matrix_content[row][col]
            else:
                raise MatrixException(Matrix.M_ERR_D[5])
        return self


    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for row in range(self.rows):
                for col in range(self.cols):
                    self.matrix_content[row][col] *= other
        return self

    def __truediv__(self, other):
        return self * other**(-1)

    def __pow__(self, power):
        other = deepcopy(power)
        if type(self) == type(other):
            if self.cols != other.rows:
                raise MatrixException(Matrix.M_ERR_D[6])
            ret_matrix = self.make_empty_matrix(self.rows, other.cols)
            rotated_other = self.rotate_matrix(other, other.rows, other.cols)

            for self_row in range(len(self.matrix_content)):
                for rot_row in range(len(rotated_other)):
                    res_cell = list(zip(self.matrix_content[self_row], rotated_other[rot_row]))
                    res_cell = [eval(str(i).strip('()').replace(',', '*')) for i in res_cell]
                    ret_matrix[self_row][rot_row] = sum(res_cell)
            self.matrix_content = ret_matrix

            if self.inversed or other.inversed:
                self.matrix_content = self.round_elems_matrix(self.matrix_content, 0)
                self.inversed = False
            return self

        elif not round(power) == power:
            raise MatrixException(Matrix.M_ERR_D[7])
        elif power == 0:
            m = max(self.rows, self.cols)
            identity_matrix = self.make_empty_matrix(m, m)
            for row in range(m):
                for col in range(m):
                    if row == col:
                        identity_matrix[row][col] = 1
            self.matrix_content = identity_matrix
            return self
        elif self.rows != self.cols:
            raise MatrixException(Matrix.M_ERR_D[8])
        elif power == -1:
            return Matrix.inverse_matrix(self)
        elif power < 0:
            raise MatrixException(Matrix.M_ERR_D[9])

        temp = deepcopy(self)
        for i in range(power - 1):
            temp = temp * self
        return temp

    def __rpow__(self, power):
        raise MatrixException(Matrix.M_ERR_D[11])

    def __str__(self):
        print('result')
        for row in range(self.rows):
            for col in range(self.cols):
                self.matrix_content[row][col] = \
                Utils.try_int(self.matrix_content[row][col])
        return_str= ''
        for i in self.matrix_content:
            return_str += str(i) + '\n'
        return return_str

    @staticmethod
    def make_empty_matrix(rows_num, cols_num):
        new_matrix = list()
        for row in range(rows_num):
            row_line = list()
            for col in range(cols_num):
                row_line.append(0)
            new_matrix.append(row_line)
        return new_matrix

    @staticmethod
    def rotate_matrix(inp_matrix, old_num_rows, old_num_cols):
        rotated = Matrix.make_empty_matrix(old_num_cols, old_num_rows)
        for col in range(old_num_cols):
            for row in range(old_num_rows):
                rotated[col][row] = inp_matrix.matrix_content[row][col]
        return rotated

    @staticmethod
    def round_elems_matrix(m_list, precision=4):
        for row in range(len(m_list)):
            for col in range(len(m_list)):
                m_list[row][col] = round(m_list[row][col], precision)
        return m_list

    @staticmethod
    def get_minor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    @staticmethod
    def get_determinant(matrix_list):
        rows_len = len(matrix_list)
        cols_len = len(matrix_list[0])
        if rows_len != cols_len:
            raise MatrixException(Matrix.M_ERR_D[8])
            # what if r and c == 0 ?? test it
        elif rows_len == 1:
            return matrix_list[0][0]
        elif rows_len == 2:
            return matrix_list[0][0] * matrix_list[1][1] \
                - matrix_list[0][1] * matrix_list[1][0]
        
        determinant = 0
        for col in range(cols_len):
            minor_det = Matrix.get_determinant(
                Matrix.get_minor(matrix_list, 0, col))
            determinant += (-1)**col * matrix_list[0][col] * minor_det
        return determinant

    @staticmethod
    def inverse_matrix(matrix_class):
        determinant = Matrix.get_determinant(matrix_class.matrix_content)
        if determinant == 0:
            raise MatrixException(Matrix.M_ERR_D[10])
        elif matrix_class.rows == 1:
            matrix_class.matrix_content[0][0] = 1 / matrix_class.matrix_content[0][0]
        elif matrix_class.rows == 2:
            matrix_class.matrix_content = [[matrix_class.matrix_content[1][1] / determinant,
                                -1 * matrix_class.matrix_content[0][1] / determinant],
                               [-1 * matrix_class.matrix_content[1][0] / determinant,
                                matrix_class.matrix_content[0][0] / determinant]]
        else:
            cofactors = []
            for row in range(matrix_class.rows):
                cofactor_row = []
                for col in range(matrix_class.cols):
                    minor = Matrix.get_minor(matrix_class.matrix_content, row, col)
                    cofactor_row.append(((-1)**(row + col)) * Matrix.get_determinant(minor))
                cofactors.append(cofactor_row)
            cofactors = list(map(list, zip(*cofactors)))
            for row in range(len(cofactors)):
                for col in range(len(cofactors)):
                    cofactors[row][col] = cofactors[row][col] / determinant
            matrix_class.matrix_content = cofactors

        matrix_class.matrix_content = Matrix.round_elems_matrix(matrix_class.matrix_content)        
        matrix_class.inversed = True
        return matrix_class

    @staticmethod
    def check_full_line(expression):
        expression = expression.replace('^', '**')
        try:
            temp = re.sub(Matrix.REG_MTRX, '1', expression)
            if temp == '1**1':
                raise MatrixException(Matrix.M_ERR_D[11])
            eval(temp)
        except SyntaxError:
            raise MatrixException(Matrix.M_ERR_D[12])
        return expression

    @staticmethod
    def apply_matrix_classes(expression):
        matches = list(set(re.findall(Matrix.REG_MTRX, expression)))
        for m in range(len(matches)):
            expression = expression.replace(matches[m], f"Matrix('{matches[m]}')")
        return expression     


# x =  Matrix('[1.2,-2,3]') * 4 # ok 
# x =  Matrix('[[-11,2,2];[1,2,3]]') * Matrix('[[-11];[3];[123]]')
# x =  Matrix('[[-11,2,2]]') * Matrix('[[2,10,5]]')
# x =  Matrix('[[-11,2,2]]') ** Matrix('[[2,10,5]]')
# x =  Matrix('[[-11,2,2];[1,2,3]]') ** Matrix('[[2];[3];[1]]')
# x =  Matrix('[[-11,2,2];[1,2,3];[2,3,4];[6.2,7,8]]') ** Matrix('[[2];[3];[1]]')


# x =  Matrix('[[-11,2.2.2,2]]')


# print(x)


# expression = Matrix('[[-1,2,2]]') ** 0
# expression = Matrix('[[]]') ** 0
# expression = Matrix('[[1,2,3,4];[2,3,4,5.2];[1,23,2,3]]')
# print(expression)