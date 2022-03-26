#!/usr/bin/python3

# % - eto opredelitel'
# сделать prohibited signs like int - Matix, > < == ^
# если что-то осталось после вывод всех данных -> return invalid syntax
# проверка на пустую матрицу. может ли она существовать?? если да, то сделать проверки в функициях, где это приемлимо

# сделать отдельный блок с разделом тестов из сабжа

# write smth in return value when errors occures
# make anotations
# test moew cases with __rmul__
# если осталась только одна row -> make sum??
# rename clean
# try .2            1.   0.0     numbers, regex will catch them

# rename all row to r and col to c in loops ili ne nado???

# тест неравных матриц
# where m -> make matrix in input to funcs

# Программа также должна управлять модулями с помощью оператора %, 
# а также умножением матриц, которое будет отмечено ∗∗. 
# Почленное умножение двух матриц или скаляра на матрицу отмечается знаком *. поэлементное умножение

import re
import sys

from copy import deepcopy


class Matrix:
    REG = r'\[(?:\[(?:\d+,?)+\];?)+\]'

    def __init__(self, inp: str):
        self.raw_inp = inp[1:-1].split(';')
        self.clean_m = self.cleaned_input

        # # call exception if check_uniformity == 0
        # if not self.check_uniformity():
        #     return 'nan' -> call str ???

        self.rows = len(self.clean_m)
        self.cols = len(self.clean_m[0])

        # проверка !!   check seze equality!! включить

        # print(self.clean_m)
        # print(self.rows)
        # print(self.cols)

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
            # print(123123)
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
                res_cell = list(
                    zip(self.clean_m[self_row], rotated_other[rot_row]))
                res_cell = [eval(str(i).strip('()').replace(',', '*'))
                            for i in res_cell]
                ret_matrix[self_row][rot_row] = sum(res_cell)
        self.__init__(str(ret_matrix).replace(' ', '').replace('],[', '];['))
        # возможно просто self matrix присвоить значение в clean-M?

        # if self.inv or other.inv
        # for r in range(len(self.clean_m)):
        #     for c in range(len(self.clean_m[0])):
        #         self.clean_m[r][c] = round(self.clean_m[r][c])

        return self

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for row in range(self.rows):
                for col in range(self.cols):
                    self.clean_m[row][col] *= other
        return self
        # else:
        #     print('is it works???')
        #     return self.__mul__(other) # ??

    def __truediv__(self, other):
        return self * other**(-1)

    def __pow__(self, power):
        # dolzhna bit' pravil'naya matrica
        #
        # pow shold be more 0
        # if power not int -> na vihod means float
        if self.rows != self.cols:
            print('matrix should be square')
            return  # think about return vals
        elif power == -1: # check it
            return Matrix.inverse_matrix(self)
        # elif

        temp = deepcopy(self)
        for i in range(power - 1):
            temp = temp * self
        return temp

    def __rpow__(self, power):
        return 'imposible'  # make good describe
        return

    def __str__(self):
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
        else:
            determinant = 0
            for col in range(cols_len):
                minor_det = Matrix.get_determinant(
                    Matrix.get_minor(m_list, 0, col))
                determinant += (-1)**col * m_list[0][col] * minor_det
        return determinant

    @staticmethod
    def inverse_matrix(m_class): # make matrix class
        # узнать условие инвертирования матриц
        determinant = Matrix.get_determinant(m_class.clean_m)
        # if determinant == 0 -> bad -> return
        #  if равен 0, запишите «однозначного решения нет». 
        # if == 1 
        # сделать функцию для возврата как в 102 строке
        if m_class.rows == 2:
            m_class.clean_m = [[m_class.clean_m[1][1] / determinant,
                                -1 * m_class.clean_m[0][1] / determinant],
                               [-1 * m_class.clean_m[1][0] / determinant,
                                m_class.clean_m[0][0] / determinant]]
            # return [[m_class.clean_m[1][1] / determinant,
            #     -1 * m_class.clean_m[0][1] / determinant],
            #     [-1 * m_class.clean_m[1][0] / determinant,
            #     m_class.clean_m[0][0] / determinant]] # return class here need round here??
        else:
            cofactors = []
            for row in range(m_class.rows):
                cofactor_row = []
                for col in range(m_class.cols):
                    minor = Matrix.get_minor(m_class.clean_m, row, col)
                    cofactor_row.append(((-1)**(row + col))
                                        * Matrix.get_determinant(minor))
                cofactors.append(cofactor_row)
            cofactors = list(map(list, zip(*cofactors)))
            for row in range(len(cofactors)):
                for col in range(len(cofactors)):
                    cofactors[row][col] = cofactors[row][col] / determinant
            m_class.clean_m = cofactors

        for r in range(len(m_class.clean_m)):
            for c in range(len(m_class.clean_m[0])):
                m_class.clean_m[r][c] = round(m_class.clean_m[r][c], 4)
        
        # add here property in class inverse
        return m_class

    @staticmethod # maybe it can be common func in utils
    def check_available_signs(expression: str):
        expression = expression.replace('^', '**')
        # +-/*% - availible signs
        try:
            temp = re.sub(Matrix.REG, '1', expression)
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


# matix with power 0 what gives?
expression = '[[1,2,3];[32,1,2];[4,5,6]]'



expression = Matrix.check_available_signs(expression)
print('original expression', expression)
expression = Matrix.add_classes(expression)
print(eval(expression))




# with pow
expression = '[[1,2,3];[32,1,2];[4,5,6]]^2+[[1,2,3];[32,1,2];[4,5,6]]'