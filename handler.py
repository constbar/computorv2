#!/usr/bin/python3

import re
import sys
from termcolor import colored

from complex_nums import Complex

# что если =? будет посередине? или их будет несколько?
# case sensetive should be turned off
# модет реплейс сделать на **
#
# bad_combos = {"()", ",,", "==", "[]",
#
#


class HandlerException(Exception):
    pass

class Handler:
    # HISTORY of all inputs -> cls.method
    ERR_D = {
        1: 'expression should have one equal sign',
        2: 'both sides of the expression must be',
        #        # 3: 'expression must have an integer exponent', -> for poly and complex
        #        # 4: 'expression must have a non-negative exponent', -> for poly and complex
        #        # 5: 'expression can only have allowed syntax',
        #        # 6: 'it\'s just a numerical equation. no solution',
        #        # 7: 'it\'s an incorrect numerical equation. no solution',
        #        # 8: 'each real number is a solution',
    }

    # allowed_symbols_natural
    asn = r'(\d+\.\d+|\w+|[^ 0-9])'

    # patt = re.compile(r'(\d+)|([\+-]?\d+)') expression only for digits
    EXP_D = {'a': '20', 'b': 'asd', 'varC': 'smth'}

    @classmethod
    # should return class of var
    def read_expression(cls, line: str):
        line = line.replace('\t', '').replace(' ', '')
        if line.count('=') != 1:
            raise HandlerException(Handler.ERR_D[1])
        elif line.endswith('=?') and not line.startswith('=?'):
            print('lets work with instant computations')
        elif not all(line.split('=')):
            raise HandlerException(Handler.ERR_D[2])
            # maybe make here a flag or smth ..
        else:
            key, val = line.split('=')

        print('line: ', line)
        print('key:  ', key)
        print('val:  ', val)

        # может сделать первую проверку на синтаксси с помощью ones
        val_list = re.findall(re.compile(cls.asn), val)
        print()
        print('val_list:         ', val_list)

        # подставление значение, которые уже есть в словаре
        for i in range(len(val_list)):
            if val_list[i].isalpha():
                try:
                    val_list[i] = cls.EXP_D[val_list[i]]
                except KeyError:
                    continue


        print('changed val_list: ', val_list) # not changed -> fullfilled
        changed_line = ''.join(val_list)
        print('changed_val:     ', changed_line)
        literal_variables = re.findall(r'[a-zA-Z]+', changed_line)
        literal_variables = list(set(literal_variables)) # make it in 1 str

        try:
            # list(map(str.lower, literal_variables)).remove('i')
            # one of them will not work
            # think about lower case in past
            literal_variables.remove('I')
            literal_variables.remove('i')
        except ValueError:
            pass

        # print(list(map(str.lower, literal_variables)))
        print(literal_variables)

        if len(literal_variables) > 1:
            print('to many unknown vars', len(literal_variables), literal_variables)
            # raise expression()s

        elif len(literal_variables) == 0:
            print('this rational expression')
            # make calc and add val to dict

        elif len(literal_variables) == 1:
            # может быть только i для комплексов
            print('one unkown var' , '      ', 'it could be func or poly')

        print('after chiking all unknown vars: ', changed_line)

        print('can parse conn complex and matrixes')
        exp = Complex.simplify_expression(changed_line)
        exp = Complex.clean_signs(exp)
        # make replace with something
        print(exp)
        # print(Complex(f'{exp}'))
        # kek = Complex.simplify_expression('3i^2 - 123 + 122i')
        # kek = Complex.clean_signs(kek)


Handler.read_expression('kek = 20i^23 * 2') # complex
# Handler.read_expression('kek = 123+231-we  +we + a ** a') # for func
# Handler.read_expression('kek = 123+231-we  +we + a ** a + I')
# Handler.read_expression('kek = 123+231-we  +we + a ** a + I')


# Handler.read_expression('kek = 123+231- a') # rational expresion
# Handler.read_expression('kek = 123+231-we') # 1 unknown var
# Handler.read_expression('kek = 123+231-we -  a  - qweqwe') # 2 > unknown vars