import re
from utils import Utils
from copy import deepcopy

class ComplexException(Exception):
    pass

class Complex:
    """
    REG_WRG_INP_I - check the input sequence
    REG_POW_COMPL - search for all variables within an expression
    REG_CMPLX_VLS - search for all variables inside a sign-separated expression
    """

    REG_WRG_INP_I = r'[i]\d'
    REG_POW_COMPL = r'-?(?:(?:\d+)|(?:\d+\.\d+))?\*?[i]\^\d+'
    REG_CMPLX_VLS = r'(-?\d+\.\d+i|-?\d+i|-?\d*\.\d*|-?\d+|[^ 0-9])'

    C_ERR_D = {
        1: 'division by zero',
        2: 'exponent must be an integer',
        3: 'invalid syntax for complex expression'
    }

    def __init__(self, inpt):
        self.re = 0
        self.im = 0
        self.complex = False
        if '+' in inpt:
            inpt = inpt.replace('+', '')
        if 'i' in inpt:
            self.complex = True
            if inpt == '-i' or inpt == 'i':
                self.im = float(inpt.replace('i', '1'))
            else:
                self.im = float(inpt.strip('i'))
        else:
            self.re = float(inpt)

    def __add__(self, other):
        self.re = self.re + other.re
        self.im = self.im + other.im
        self.complex = True if self.im else False
        return self

    def __sub__(self, other):
        self.re = self.re - other.re
        self.im = self.im - other.im
        self.complex = True if self.im else False
        return self

    def __mul__(self, other):
        if self.complex is True and other.complex is False:
            self, other = other, self
        pair_1 = Complex(f'{self.re * other.re}')
        pair_2 = Complex(f'{self.re * other.im}i')
        pair_3 = Complex(f'{self.im * other.re}i')
        if self.complex:
            pair_4 = Complex.exponentiate_line(f'{self.im * other.im}i^2')
            pair_4 = Utils.clean_signs(pair_4)
        else:
            pair_4 = '0'
        pair_4 = Complex(pair_4)
        fin = pair_1 + pair_2 + pair_3 + pair_4
        fin.complex = True if fin.im else False
        return fin

    def __truediv__(self, other):
        if self.complex is True and not self.re \
            and other.complex is True and not other.re:
            self.re = self.im / other.im
            self.im = 0
            self.complex = False
            return self
        if not self.re and not other.re:
            raise ComplexException(Complex.C_ERR_D[1])

        conjugator = deepcopy(other)
        conjugator.im = conjugator.im * -1
        self = self * conjugator
        try:
            denominator = other * conjugator
        except ValueError:
            raise ComplexException(Complex.C_ERR_D[1])
        try:
            self.re = self.re / denominator.re
            self.im = self.im / denominator.re
        except ZeroDivisionError:
            raise ComplexException(Complex.C_ERR_D[1])
        self.complex = True if self.im else False
        return self

    def __pow__(self, power):
        if power.re == 0:
            self.re = 1
            self.im = 0
            return self
        elif power.complex is True:
            raise ComplexException(Complex.C_ERR_D[2])
        elif self.complex is False and power.complex is False:
            return Complex(str(self.re ** power.re))
        temp = deepcopy(self)
        if not self.re:
            self.im = self.im ** power.re
            pw = Complex.exponentiate_line(f'i^{int(power.re)}')
            return Complex(str(self.im)) * Complex(Utils.clean_signs(pw))
        for i in range(int(power.re) - 1):
            temp = temp * self
        temp.complex = True if temp.im else False
        return temp

    def __str__(self):
        return_dict = dict()
        return_dict['real'] = self.re
        return_dict['imag'] = self.im
        return Complex.make_str_output(return_dict)

    def make_str_output(res_dict):
        if not res_dict['real'] and not res_dict['imag']:
            return '0'
        return_str = ''
        if res_dict['real']:
            return_str += str(Utils.try_int(res_dict['real']))
        if res_dict['imag']:
            if res_dict['imag'] > 0 and res_dict['real']:
                return_str += '+'
            return_str += str(Utils.try_int(res_dict['imag'])) + 'i'
        return return_str

    @staticmethod
    def pow_replacer(part):
        part = part.group(0).replace('*', '')

        clx_dict = dict()
        clx_dict['real'] = 0
        clx_dict['imag'] = 0
        clx_dict['imag'], clx_dict['pwr'] = part.split('^')
        clx_dict['imag'] = clx_dict['imag'].replace('i', '')

        if clx_dict['imag']:
            clx_dict['imag'] = float(clx_dict['imag'])
        else:
            clx_dict['imag'] = 1

        clx_dict['pwr'] = int(clx_dict['pwr'])
        if clx_dict['pwr'] % 4 == 0:
            clx_dict['real'] = clx_dict['imag']
            clx_dict['imag'] = 0
        elif clx_dict['pwr'] % 4 == 3:
            clx_dict['imag'] *= -1
        elif clx_dict['pwr'] % 4 == 2:
            clx_dict['real'] = clx_dict['imag'] * -1
            clx_dict['imag'] = 0
        return '+' + Complex.make_str_output(clx_dict)

    @staticmethod
    def exponentiate_line(expression):
        result = re.sub(Complex.REG_POW_COMPL, Complex.pow_replacer, expression)
        return result

    @staticmethod
    def apply_complex_classes(values_list):
        exec_line = ''.join(f"Complex('{i}')" if i not in '-+*/^()' else i for i in values_list)
        exec_line = Utils.clean_signs(exec_line)        
        if exec_line[0] == '-':
            exec_line = "Complex('-1')*" + exec_line[1:]
        elif exec_line[0] == '+':
            exec_line = exec_line[1:]
        return exec_line.replace('^', '**')
