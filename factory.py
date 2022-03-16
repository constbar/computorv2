#!/usr/bin/python3

# change chmod

import re
import sys
from termcolor import colored


class Handler:
    """
    asn - allowed_symbols_natural
    """

    # REG_DEF_MATRIX = r''
    # HISTORY of all inputs -> cls.method
    # make singltone
    ERR_D = {
        1: 'expression should have only one equal sign',
        2: 'both sides of the equation must be',
        #        # 3: 'expression must have an integer exponent', -> for poly and complex
        #        # 4: 'expression must have a non-negative exponent', -> for poly and complex
        #        # 5: 'expression can only have allowed syntax',
        #        # 6: 'it\'s just a numerical equation. no solution',
        #        # 7: 'it\'s an incorrect numerical equation. no solution',
        #        # 8: 'each real number is a solution',
    }

    asn = r'(\d+\.\d+|\w+|[^ 0-9])'
    # win = r'[\d]*'

    # patt = re.compile(r'(\d+)|([\+-]?\d+)') expression only for digits
    EXP_D = {'a': '20', 'b': 'asd'}  # , 'varC': 'asd'}

    # bad_combos = {"()", ",,", "==", "[]", "[;]", "[;", ";]", \
    # "[,", ",]", "[[[", "]]]", ";[[", "]];"}

    @classmethod
    # should return class of var
    def read_expression(cls, line: str):
        """
        line = Handler.check_line(line)
        =? - без присвоения -> просто вычисление и вывод
        всегда обязательно должен быть знак = иначе не валидный ввод
        проверка ключа на валидность, только буквы без чисел
        проверка на разрешенные символы в выражении

        # 1. проверка на наличие текстовых переменных в тесксте
            # если неизвестных больше, чем 1 -> невалид
        """

        # может просто не обрабатывать таб?
        line = line.replace('\t', '').replace(' ', '')
        print(colored(line, 'cyan'))
        key, val = line.split('=')
        print(colored(val, 'red'))

        val_list = re.findall(re.compile(cls.asn), val)

        for i in range(len(val_list)):
            if val_list[i].isalpha():
                try:
                    val_list[i] = cls.EXP_D[val_list[i]]
                except KeyError:
                    continue

        print(colored(val_list, 'green'))
        changed_line = ''.join(val_list)

        # print('val list: ', val_list)

        kek = re.findall(r'[a-zA-Z]+', changed_line)
        if len(kek) > 1:
            print('to many unknown vars')
            print(colored(kek, 'red'))

        if len(kek) == 0:
            print(colored('this rational', 'green'))
            # make calc and add val to dict

        if len(kek) == 1:
            # может быть только i для комплексов
            print(colored(kek, 'red'))
            print('maybe its complex number or function(maybe inside will be polynomial)')
        print(colored(changed_line, 'cyan'))

        # print(eval(''.join(val_list)))

        # isalnum()   Returns True if all characters in the string are alphanumeric
        # isalpha()   Returns True if all characters in the string are in the alphabet
        # print(line)

        return line


# Handler.read_expression('kek = 2.22 + a  + a + 20i')
# Handler.read_expression('kek = 2.22 + a  + a + i')
# Handler.read_expression('kek = 2 * (2 - 44 / 3) + 4 + a')
# Handler.read_expression('kek = 2 * (2 - 44 / 3) + 4i + a')
# Handler.read_expression('kek = 2 * (2 + 4) + a + c')


# import re
# source = '((81.2 + 0 *  6) /42 + (3-1)) + varA + a'
# # number_or_symbol = re.compile(r'(\d+|[^ 0-9])')
# # (?# number_or_symbol = re.compile(r'(\w+|\d*\.\d*|[^ 0-9])'))
# number_or_symbol = re.compile(r'(\d+\.\d+|\w+|[^ 0-9])')
# kek = re.findall(number_or_symbol, source)
# print(''.join(kek))

    # @classmethod
    # def check_line(cls, line: str):
    #     if '=' in line and line.count('=') != 1:
    #         return cls.ERR_D[1]
    #     # elif not all(line.split('=')): # if = in line -> check
    #         # return Handler.ERR_D[2]
    #     return line


# border of bad inputs:
# 312asd13
# **i / **-1 / **1.2 -> wong coomplex power -> try another

# параметры для парсинга регексом
# i всегда сзади числа  3i
# 'i.1' - после i ничего не должно быть -> 0 + 0.1i

# re + b * im
# make try int
class Complex:
    def __init__(self, inp: str):
        self.re = 0
        self.im = 0
        self.co = False
        if '+' in inp:
            inp = inp.replace('+', '')
        if 'i' in inp:
            self.co = True
            if inp == '-i' or inp == 'i':
                self.im = float(inp.replace('i', '1'))
            else:
                self.im = float(inp.strip('i'))
        else:
            # print(inp)
            self.re = float(inp)

    def __pow__(self, power):

        if self.re and self.im:
            print(123)

        # maybe return not str but repr
        # if isinstance(int, type(power)):
        if self.co is True:
            simplify = power.re % 4
            if simplify == 0:
                self.re = self.im
                self.im = 0
                self.co = False
            elif simplify == 3:
                self.im *= -1
            elif simplify == 2:
                self.re = self.im * -1
                self.im = 0
                self.co = False
            # elif simplify == 1# and ?= -> :
                # print('i')
        else:
            self.re = self.re ** power.re

        return self
        # return Complex(str(self.__str__()))
        # print(f'{self.re} + {self.im}i')

    def __str__(self):
        f = ''
        if self.re != 0:
            f += str(self.re)
            if self.im > 0:
                f += ' + '
            elif self.im > 0 and self.im:
                f += ' - '
        if self.im:
            f += str(self.im) + 'i'
        return f
        # print(f'{self.re} + {self.im}i\t\t\t{self.co}')
        # return f'{self.re} + {self.im}i'

    # __pow__(self, other[, modulo])

    # def __add__(self, other):
    #     # if ohetr is instance of .. check if instance
    #     return self.n ** other.n

    # def __str__(self):
    #     return '1+2'


# print((Complex('7i') ** Complex('8')))

# print((Complex('7i') ** Complex('162')))
# print((Complex('7i') ** Complex('18')))
# print((Complex('7i') ** Complex('9')))
print(Complex('7i') ** Complex('9') ** Complex('2'))
print((Complex('7i') ** Complex('9')) ** Complex('2'))
# print((Complex('-7') ** Complex('2')))
# print(eval("(Complex('7i') ** Complex('9')) ** Complex('2')"))

# print(Complex('2i'))
# print(Complex('-20i') ** Complex('27'))
# print((Complex('7i') ** Complex('5')))
# print(Complex('6.3i') ** Complex('2'))
# print((Complex('3i') ** Complex('8')))
# print((Complex('3i') ** Complex('8')) ** Complex('3'))
# print((Complex('i') ** Complex('5')))
# print(Complex('3i') ** Complex('4'))
# print(Complex('3i') ** Complex('16'))
# print(Complex('-i') ** Complex('16'))
# kek = Complex('3i') ** Complex('2')
# print(typekek)
# print(Complex('3') ** Complex('2'))

# print(Complex('+3i'))
# print(Complex('+2.2'))
# print(Complex('-i'))
# print(Complex('+i'))
# print(Complex('1.1'))
# print(Complex('-2'))
# print(Complex('20i'))
# print(Complex('-20.2i'))
