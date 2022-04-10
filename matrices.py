import re
from utils import Utils
from copy import deepcopy

class MatrixException(Exception):
    pass

class Matrix:
    """
    REG_POW_MAT - checks if the matrix is raised to the power of the matrix
    REG_MTRX - finds all matrices in an expression
    """
    M_ERR_D = {
        1: 'matrix could not be empty',
        2: 'the interior parts of the matrix must be equal',
        3: 'invalid matrix content',
        4: 'both matrices must be the same size',
        5: 'matrices must be equal for termwise multiplication',
        6: 'the columns of the first matrix must be equal to the rows of the second',
        7: 'the degree of the matrix must be an integer',
        8: 'matrix must be square',
        9: 'matrix power must be greater than 0',
        10: 'the determinant is 0. there is no unique solution',
        11: 'matrix couldn\'t be an exponent',
        12: 'invalid syntax for matrix expression'
    }

    REG_POW_MAT = r'\]\^-?\['
    REG_MTRX = r'\[(?:\[(?:-?\d+[.]?[d+]?,?)+\];?)+\]'

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
        self.recalculate_matrix()
        return self

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            for row in range(self.rows):
                for col in range(self.cols):
                    self.matrix_content[row][col] *= other
        self.recalculate_matrix()
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
            self.recalculate_matrix()
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
            self.recalculate_matrix()
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
        temp.recalculate_matrix()
        return temp

    def __rpow__(self, power):
        raise MatrixException(Matrix.M_ERR_D[11])

    def __str__(self):
        return_str = ''
        for i in range(len(self.matrix_content)):
            return_str += str(list(map(Utils.try_int, self.matrix_content[i])))
            if i != len(self.matrix_content) - 1:
                return_str += '\n'
        return return_str.replace(' ','')

    def recalculate_matrix(self):
        self.rows = len(self.matrix_content)
        self.cols = len(self.matrix_content[0])

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
        matrix_class.recalculate_matrix()
        return matrix_class

    @staticmethod
    def check_full_line(expression):
        if re.findall(Matrix.REG_POW_MAT, expression):
            raise MatrixException(Matrix.M_ERR_D[11])
        expression = expression.replace('^', '**')
        try:
            temp = re.sub(Matrix.REG_MTRX, '1', expression)
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
