#!/usr/bin/python3

import re
import sys
from copy import deepcopy
from termcolor import colored


# make norm rouund in str

class Complex:
    REG_POW_COMPL = r'-?(?:(?:\d+)|(?:\d+\.\d+))?\*?[iI]\^\d+'
    def __init__(self, inpt):
        self.re = 0
        self.im = 0
        self.co = False
        if '+' in inpt:
            inpt = inpt.replace('+', '')
        if 'i' in inpt:  # or big I
            self.co = True
            if inpt == '-i' or inpt == 'i':
                self.im = float(inpt.replace('i', '1'))
            else:
                self.im = float(inpt.strip('i'))
        else:
            self.re = float(inpt)

    def __add__(self, other):
        self.re = self.re + other.re
        self.im = self.im + other.im
        self.co = True if self.im else False
        # if self.im:
        #     self.co = True
        return self

    def __sub__(self, other):
        self.re = self.re - other.re
        self.im = self.im - other.im
        self.co = True if self.im else False
        return self

    # make it cleaner
    def __mul__(self, other):
        if self.co is True and other.co is False:  # del not
            self, other = other, self

        fi1 = Complex(f'{self.re * other.re}') # means first and second -> rename it
        fi2 = Complex(f'{self.re * other.im}i')
        sc1 = Complex(f'{self.im * other.re}i')
        if self.co:
            sc2 = Complex.simplify_expression(f'{self.im * other.im}i^2')
            sc2 = Complex.clean_signs(sc2)  # make if more clever
        else:
            sc2 = '0'
        # ValueError
        sc2 = Complex(sc2)
        fin = fi1 + fi2 + sc1 + sc2
        fin.co = True if fin.im else False
        # matybe make self = deep.copy(fin) -> return self
        # if not fin.im: esli deep copy ok -> izmenit' yslovie
        #     fin.co = False
        return fin

    def __truediv__(self, other):
        if self.co is True and not self.re \
            and other.co is True and not other.re:
            self.re = self.im / other.im
            self.im = 0
            self.co = False
            return self
        if not self.re and not other.re:
            return 'dont devide asdfjkhasd 1'
        conjugator = deepcopy(other)
        conjugator.im = conjugator.im * -1
        self = self * conjugator
        try:
            denominator = other * conjugator
        except ValueError:
            return 'dont devide asdfjkhasd 3'
        try:
            self.re = self.re / denominator.re
            self.im = self.im / denominator.re
        except ZeroDivisionError:
            return 'dont devide asdfjkhasd 0'
        self.co = True if self.im else False
        return self

    def __pow__(self, power):
        if power.co is True:
            return 'exponent must be an integer'
        if self.co is False and power.co is False:
            return Complex(str(self.re ** power.re))

        temp = deepcopy(self)
        if not self.re:
            self.im = self.im ** power.re
            pw = Complex.simplify_expression(f'i^{int(power.re)}')
            return Complex(str(self.im)) * Complex(Complex.clean_signs(pw))
        for i in range(int(power.re) - 1):
            temp = temp * self
        temp.co = True if temp.im else False
        return temp

    def __str__(self):
        # if result of calculationsw is 0 -> return 0 and co make false
        # сделать округление до 6 знака # сделать try int
        return_dict = dict()
        return_dict['real'] = self.re
        return_dict['imag'] = self.im
        return Complex.make_str_output(return_dict)

    # make it better
    def make_str_output(res_dict):
        f = ''
        if res_dict['real']:
            f += str(res_dict['real'])
        if res_dict['imag']:
            if res_dict['imag'] > 0 and res_dict['real']:
                f += ' + '
            f += str(res_dict['imag']) + 'i'
        return f

    # this only for i's
    @staticmethod
    def pow_replacer(part, diction=False): # diction not used
        # или part is class regex <class 're.Match'>
        # if type(part).__name__ == 'Match': # need i?
        part = part.group(0).replace('*', '')
        # else: need i??
        # part = part.replace('*', '')

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
        # check if it real int func
        # print(clx_dict['real'], clx_dict['imag'], clx_dict['pwr'])
        if clx_dict['pwr'] % 4 == 0:
            clx_dict['real'] = clx_dict['imag']
            clx_dict['imag'] = 0
        elif clx_dict['pwr'] % 4 == 3:
            clx_dict['imag'] *= -1
        elif clx_dict['pwr'] % 4 == 2:
            clx_dict['real'] = clx_dict['imag'] * -1
            clx_dict['imag'] = 0

        # print(clx_dict['real'], clx_dict['imag'], clx_dict['pwr'])
        return '+' + Complex.make_str_output(clx_dict)

    @staticmethod
    def clean_signs(raw_str):
        raw_str = raw_str.replace('-+', '-')
        raw_str = raw_str.replace('++', '+')
        raw_str = raw_str.replace('+-', '-')
        raw_str = raw_str.replace('/+', '/') # is it neccesary?
        raw_str = raw_str.replace(')C', ')+C')
        raw_str = raw_str.replace('/(+C', '/(C')
        return raw_str

    @staticmethod
    def simplify_expression(expression):
        # для проверки валидности сделать еденичны и эвал чтобы понять ок . не ок,
        result = re.sub(Complex.REG_POW_COMPL, Complex.pow_replacer, expression)
        # print('result', result)
        return result

# kek = Complex.simplify_expression('3i^2 - 123 + 122i')
# print(kek)
# kek = Complex.clean_signs(kek)
# 1 этап заменяем все степени
# # 2 чистим знаки, можно чистить знаки прямо в функции pow replacer
# # сделать рег экс который забирает все переменные и делаем из них классы комплекс чисел parse expression func
# # вычисление
# print(kek)

# test = (Complex('i**2'))# / Complex('i')) / (Complex('222') + Complex('1') * Complex('i'))
# pr/int(test)
# test = (Complex('5i') * Complex('6i')) / (Complex('2i') - Complex('2i'))
# test = ((Complex('5i') * Complex('6i')) / Complex('0'))
# test = (Complex('5i') * Complex('6i')) / (Complex('2i') - Complex('2i'))  -eror here

# test = Complex('5i') * Complex('2i') / Complex('2i')
# test = (Complex('5i') / Complex('22i')) / ((Complex('5') - Complex('2i')))
# test = (Complex('52i') * Complex('52i')  / Complex('i')) - Complex('13')
# test = (Complex('5') / Complex('2i'))
# print(test.co)
# print(5/22)

# test = Complex('1') - Complex('2i') * Complex('2i') + Complex('2i') / Complex('2i') ** Complex('2')
# test = Complex('-4i') - Complex('4')
# # test = test * Complex('i')
# print(test)
# print(test.co)



# try: # need to handle it
#     # test = Complex('5i') ** Complex('2i')  * Complex('2i')
#     print(test)
# except TypeError:
#     print(123)