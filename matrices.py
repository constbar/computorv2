# The matrix syntax is of the form [[A0,0 , A0,1 , ...]; [A1,0 , A1,1 , ...]; ...]
# The semicolon is used to separate the rows of a matrix, so it is not present in the as-
# signment of a matrix that has only one row. On the other hand, the comma is used to
# separate the columns of a matrix, which on the other hand will not be present in the
# assignment of a matrix that has only one column.

# write smth in return value when errors occures
# make anotations
# test moew cases with __rmul__
# если осталась только одна row -> make sum??
# rename clean
# try .2            1.   0.0     numbers, regex will catch them


# тест неравных матриц

import sys
from copy import deepcopy


class Matrix:
    def __init__(self, inp: str):
        self.raw_inp = inp[1:-1].split(';')
        self.clean_m = self.cleaned_input

        # # call exception if check_uniformity == 0
        # if not self.check_uniformity():
        #     return 'nan' -> call str ???

        self.rows = len(self.clean_m)
        self.cols = len(self.clean_m[0])

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
            print(123123)
            return '1234'
        for row in range(self.rows):
            self.clean_m[row] = list(zip(self.clean_m[row], other.clean_m[row]))
            self.clean_m[row] = list(map(sum, self.clean_m[row]))
        return self

    def __sub__(self, other):
        if not self.check_size_equality(other):
            print(123123)
            return '1234'
        for row in range(self.rows):
            other.clean_m[row] = [i * -1 for i in other.clean_m[row]]
            self.clean_m[row] = list(zip(self.clean_m[row], other.clean_m[row]))
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
                res_cell = list(zip(self.clean_m[self_row], rotated_other[rot_row]))
                res_cell = [eval(str(i).strip('()').replace(',', '*')) for i in res_cell]
                ret_matrix[self_row][rot_row] = sum(res_cell)
        self.__init__(str(ret_matrix).replace(' ', '').replace('],[', '];['))
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


    def __pow__(self, power):
        # pow -1 -> invewse matrix
            # dolzhna bit' pravil'naya matrica
            # 
        # pow shold be more 0
        # if power not int -> na vihod
        if self.rows != self.cols:
            print('matrix should be square')
            return # think about return vals
        
        temp = deepcopy(self)
        for i in range(power - 1):
            temp = temp * self
        return temp

    def __rpow__(self, power):
        return 'imposible' # make good describe
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

# разрбраться с модулем % - определитель?
# деление матриц?
# подумать о значках больше / меньше в компексах
# прочитаь сабж на предмет -[[]]
###             (?:(\[(?:(?:\[?\d+\.\d*,?\]?;?)|(?:\[?\d+,?\]?;?),?){1,}\])|\d*\.\d*|\d+) - fin

# m2 = Matrix('[[4,3,3];[3,3,5]]')

m3 = Matrix('[[4.5,3];[-4.3,2];[2,2]]') # 3x2
# print(m3)
m1 = Matrix('[[1];[2];[3]]') # 2x1
m4 = Matrix('[[3,4,2]]') # 2x1
# print(m1)
# print(m3 * m1)
# print(m4 * m1)
# print(m3)
# print(m3 * 10)
# print(10 * m3)
# print(m1 * 5)
m5 = Matrix('[[1,2,3];[6,-5,7];[2,3,4]]')
# print(m5 ** 3)
print(3 ** m5)


# сделать prohibited signs like int - Matix, > < == ^ 
# если что-то осталось после вывод всех данных -> return invalid syntax


# m1 = Matrix('[[1.1,2,3];[3,4,5]]')
# print(m1)
# m3 = Matrix('[[4,3];[3,3];[2,2]]')
# print(m3)
# print()
# print(m1 * m3)

# m3 = Matrix('[[4,3];[3,3]]')
# print()
# print(m1 - m2)
# print(m1 + m3)
# print(m2)
# print(m3)
# print()
# print(82/5)


# regex s
# # [[1,2];[3,2];[3,4]]
# # [[1,2]]


# [[1,2.123];[3,2];[3,4];[123,412,231.2];[2,2,2.2,2,2,123.2]]
# [[1,2.123,123,412,513.123,88.2];[3,2];[3,4]]
# [[];[];[];[]]
# [[]]
# [[1.2,2]]
# -[[1,2]]
# [5, [1.3,2.2]]
# [5.5, [1.3,2.2]]


#     # REG_POW_COMPL = r'-?(?:(?:\d+)|(?:\d+\.\d+))?\*?[iI]\^\d+'

# \[[\d+\.?\d+,]+[\d+\.?\d+]*\]
# -?\[(?:(?:\d+\.?\d+?)) - beggining
# -?\[(?:(?:\[\d+\.?\d?\,\d+\.?\d?\]))\] - for 1 repeat


# (?:(?:\d+\.\d+)|(?:\d+))  - all matches inside []
# (?:(?:\d+\.\d+\,?)|(?:\d+\,?)){1,} <- one piece inside []

# (?:(?:\d+\.\d+\,?)|(?:\d+\,?)){1,} <- final good


# \[\]{1,};


w
# -?\[(?:(?:\d+\.?\d+?)) - dont know what is it

#     # REG_POW_COMPL = r'-?(?:(?:\d+)|(?:\d+\.\d+))?\*?[iI]\^\d+'

# -?\[(?:(?:\d+\.?\d+?)) - beggining
# -?\[(?:(?:\[\d+\.?\d?\,\d+\.?\d?\]))\] - for 1 repeat

# \[(?:(?:\d+\.\d+\,?)|(?:\d+\,?)){1,}\] fin
# \[(?:(?:\d+\.\d+\,?)|(?:\d+\,?)){1,}\]\;? good
# \[\[(?:(?:\d+\.\d+)|(?:\d+)\,?){1,}\];?\] not that good
# \[(?:(?:(?:\d+\.\d*)|(?:\d+),?){1,})\];?
# (?:(?:(?:\[?\d+\.\d*\]?;?,?)|(?:\[?\d+\]?;?,?),?){1,}) so so
# \[(?:(?:\[?\d+\.\d*\]?;?,?)|(?:\[?\d+\]?;?,?),?){1,}\] - ok
# \[(?:(?:\[?\d+\.\d*,?]?;?)|(?:\[?\d+,?]?;?),?){1,}\] - very ok without /