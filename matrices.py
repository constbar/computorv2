#!/usr/bin/python3

# rename clean
# try .2            1.   0.0     numbers, regex will catch them
# rename all row to r and col to c in loops ili ne nado??? make oposite
# where m -> make matrix in input to funcs
# self.clean_m -> value?

import re
import sys

from copy import deepcopy


class Matrix:
    REG = r'\[(?:\[(?:\d+,?)+\];?)+\]'

    def __init__(self, inp: str):
        self.raw_inp = inp[1:-1].split(';')
        self.clean_m = self.cleaned_input

        if not self.check_uniformity():
            sys.exit('parts of matrix should be equal')
            return 'parts of matrix should be equal'

        self.inversed = False
        self.rows = len(self.clean_m)
        self.cols = len(self.clean_m[0])

    @property
    def cleaned_input(self):
        return [list(map(float, i.strip('[]').split(','))) for i in self.raw_inp]

    def check_uniformity(self):
        return len(set(map(len, self.clean_m))) == 1

    def check_size_equality(self, other):
        # возможно сразу сделать эксепшн
        return f'{self.rows}x{self.cols}' == f'{other.rows}x{other.cols}'

    @staticmethod
    def make_empty_matrix(rows_num, cols_num):
        new_matrix = list()
        for row in range(rows_num):
            row_line = list()
            for col in range(cols_num):
                row_line.append(0)
            new_matrix.append(row_line)
        return new_matrix

    def __add__(self, other):
        if not self.check_size_equality(other):
            print('not the same sizes of matixes')
            return 'ALARAM in add'
        for row in range(self.rows):
            self.clean_m[row] = list(
                zip(self.clean_m[row], other.clean_m[row]))
            self.clean_m[row] = list(map(sum, self.clean_m[row]))
        return self

    def __sub__(self, other):
        if not self.check_size_equality(other):
            print(123123)
            return '1234'
        for row in range(self.rows):
            other.clean_m[row] = [i * -1 for i in other.clean_m[row]]
            self.clean_m[row] = list(
                zip(self.clean_m[row], other.clean_m[row]))
            self.clean_m[row] = list(map(sum, self.clean_m[row]))
        return self

    @staticmethod
    def rotate_matrix(inp_matrix, old_num_rows, old_num_cols):
        rotated = Matrix.make_empty_matrix(old_num_cols, old_num_rows)
        for col in range(old_num_cols):
            for row in range(old_num_rows):
                rotated[col][row] = inp_matrix.clean_m[row][col]
        return rotated

    @staticmethod
    def round_elems_matrix(m_list :list, precision=4):
        for row in range(len(m_list)):
            for col in range(len(m_list)):
                m_list[row][col] = round(m_list[row][col], precision)
        return m_list


    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__rmul__(other)
        elif self.cols != other.rows:
            print('cant make mult')
            return

        ret_matrix = self.make_empty_matrix(self.rows, other.cols)
        rotated_other = self.rotate_matrix(other, other.rows, other.cols)

        for self_row in range(len(self.clean_m)):
            for rot_row in range(len(rotated_other)):
                res_cell = list(zip(self.clean_m[self_row], rotated_other[rot_row]))
                res_cell = [eval(str(i).strip('()').replace(',', '*')) for i in res_cell]
                ret_matrix[self_row][rot_row] = sum(res_cell)
        self.clean_m = ret_matrix

        if self.inversed or other.inversed:
            self.clean_m = self.round_elems_matrix(self.clean_m, 0)
            self.inversed = False # think about it
        return self

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for row in range(self.rows):
                for col in range(self.cols):
                    self.clean_m[row][col] *= other
        return self
        # else: print('is it works???') return self.__mul__(other) # ??

    def __truediv__(self, other):
        return self * other**(-1)

    def __pow__(self, power):
        if not round(power) == power:
            print('ne oki')
            return 'power should be an integer number'
        elif power == 0:
            m = max(self.rows, self.cols)
            identity_matrix = self.make_empty_matrix(m, m)
            for row in range(m):
                for col in range(m):
                    if row == col:
                        identity_matrix[row][col] = 1
            self.clean_m = identity_matrix
            return self
        elif self.rows != self.cols:
            print('matrix should be square')
            return  # think about return vals
        elif power == -1:
            return Matrix.inverse_matrix(self)
        elif power < 0:
            print('power should be greater than 0')
            return 'power should be greater than 0'

        temp = deepcopy(self)
        for i in range(power - 1):
            temp = temp * self
        return temp

    def __rpow__(self, power):
        return 'imposible'  # make good describe
        return

    def __str__(self):
        if not len(self.clean_m):
            return 'error happend' # del it
        # add try int
        # if not self.rows and not self.cols:
        #     return '[]'
        # sdelat' pechat' po index
        f = ''
        for i in self.clean_m:
            f += str(i) + '\n'
        return f
        # if now rows and no cols -> []
        #       def print_matrix(mat):
        # for i in range( len(mat) ):
        #   for j in range( len(mat[i]) ):
        #     print( mat[i][j] , end = ' ')
        #   print()

    @staticmethod
    def get_minor(m, i, j):
        return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]

    @staticmethod
    def get_determinant(m_list):
        # print('det func')
        rows_len = len(m_list)
        cols_len = len(m_list[0])
        if rows_len != cols_len:
            print('matrix should be square!')
            return  # need test
            # what if r and c == 0 ??
        elif rows_len == 1:
            return m_list[0][0]
        elif rows_len == 2:
            return m_list[0][0] * m_list[1][1] \
                - m_list[0][1] * m_list[1][0]
        
        determinant = 0
        for col in range(cols_len):
            minor_det = Matrix.get_determinant(
                Matrix.get_minor(m_list, 0, col))
            determinant += (-1)**col * m_list[0][col] * minor_det
        # print('deter', determinant)
        return determinant

    @staticmethod
    def inverse_matrix(matrix_class):
        # узнать условие инвертирования матриц
        # print('ivn func')
        determinant = Matrix.get_determinant(matrix_class.clean_m)
        # print('det', determinant)
        if determinant == 0:
            print('determinant is equal 0. there is no clear solution')
            return
        elif matrix_class.rows == 1:
            print('single matrix')
            sys.exit()
            # matrix_class.clean_m[0][0] = 1 / matrix_class.clean_m[0][0]
        # сделать функцию для возврата как в 102 строке
        elif matrix_class.rows == 2:
            matrix_class.clean_m = [[matrix_class.clean_m[1][1] / determinant,
                                -1 * matrix_class.clean_m[0][1] / determinant],
                               [-1 * matrix_class.clean_m[1][0] / determinant,
                                matrix_class.clean_m[0][0] / determinant]]
        else:
            cofactors = []
            for row in range(matrix_class.rows):
                cofactor_row = []
                for col in range(matrix_class.cols):
                    minor = Matrix.get_minor(matrix_class.clean_m, row, col)
                    cofactor_row.append(((-1)**(row + col)) * Matrix.get_determinant(minor))
                cofactors.append(cofactor_row)
            cofactors = list(map(list, zip(*cofactors)))
            for row in range(len(cofactors)):
                for col in range(len(cofactors)):
                    cofactors[row][col] = cofactors[row][col] / determinant
            matrix_class.clean_m = cofactors

        matrix_class.clean_m = Matrix.round_elems_matrix(matrix_class.clean_m)        
        matrix_class.inversed = True
        return matrix_class

    @staticmethod # maybe it can be common func in utils
    def check_available_signs(expression: str):
        expression = expression.replace('^', '**')
        # +-/*% - availible signs
        try:
            temp = re.sub(Matrix.REG, '1', expression)
            print('temp', temp)
            eval(temp)
        except SyntaxError:
            print('invalid syntax with 1')
            return 'ALARM at check'
        return expression


    @staticmethod
    def add_classes(expression: str) -> str:
        # use sub for cheeck with ones
        matches = list(set(re.findall(Matrix.REG, expression)))
        for m in range(len(matches)):
            expression = expression.replace(matches[m], f"Matrix('{matches[m]}')")
        return expression

    def __mod__(self, other):
        pass        


# expression = '[[1]]**-1'
# expression = '[[2]]**-1'
# expression = '[[882]]**-1'
# expression = '[[-999]]**-1' //!!!!!!!!!!!!!!
# не парсятся цифры с запятой и с минусом
# между типами сделать операции


expression = Matrix.check_available_signs(expression)
print('original expression', expression)
print()
expression = Matrix.add_classes(expression)
try:
    kek = eval(expression)
    print(kek)
    print('inversed', kek.inversed)
except:
    print('eval err')
# print('inversed', kek.inversed)






# mult
# expression = '[[1,2,3]]*[[2];[3];[9]]'

# with pow
# expression = '[[1,2,3];[32,1,2];[4,5,6]]^2+[[1,2,3];[32,1,2];[4,5,6]]'

# inversed
# expression = '[[1,2,3];[32,1,2];[4,5,6]]**-1'
# expression = '[[1,3];[4,6]]**-1'

# check powers
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**-2.2'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**0'
# expression = '[[3,3];[32,1];[2,4]]**0'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**-2'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**-2.1'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**2.2'
# expression = '2**[[3,3,4];[32,1,3];[4,5,6]]'