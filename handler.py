#!/usr/bin/python3

import re
import sys
from termcolor import colored

from complex_nums import Complex
from matrices import MatrixException, Matrix
from functions import Function


# check regex for *   means \d* not d+
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
        3: '\'i\' can\'t be used for variables',
        4: 'variables should only contain letters'
    }

    asn = r'(\d+\.\d+|\w+|[^ 0-9])'  # allowed_symbols_natural
    # patt = re.compile(r'(\d+)|([\+-]?\d+)') expression only for digits
    

    vals_dict = {'a': '20', 'b': 'asd', 'varC': 'smth'} # make 0 init
    line = None
    key = None
    val = None
    
    upd_line = None
    # can add cls.result

    @classmethod
    def handle_line(cls, input_line):
        # добавть может оригинальный инпут для добавления в словарь результатов
        cls.read_expression(input_line)
        cls.substitute_vals_dict()
        cls.check_literal_vals()

    @classmethod
    def read_expression(cls, input_line):
        cls.line = input_line.lower()
        cls.line = cls.line.replace('\t', '').replace(' ', '')

        if cls.line.count('=') != 1:
            raise HandlerException(cls.ERR_D[1])
        elif cls.line.endswith('=?') and not cls.line.startswith('=?'):
            print('make instant computations')
            return
        elif not all(cls.line.split('=')):
            raise HandlerException(cls.ERR_D[2])
            # maybe make here a flag or smth ..

        cls.key, cls.val = cls.line.split('=') # was else here

        if cls.key == 'i':
            raise HandlerException(cls.ERR_D[3])
        elif not cls.key.isalpha():
            raise HandlerException(cls.ERR_D[4])

        # может сделать первую проверку на синтаксси с помощью ones

    @classmethod
    def substitute_vals_dict(cls):
        val_list = re.findall(re.compile(cls.asn), cls.val)
        # подставление значение, которые уже есть в словаре
        for i in range(len(val_list)):
            if val_list[i].isalpha():
                try:
                    val_list[i] = cls.vals_dict[val_list[i]]
                except KeyError:
                    continue
        cls.upd_line = ''.join(val_list)
        # все натуральыне числа в степени может сразу умножить здесь?


    @classmethod
    def check_literal_vals(cls):
        is_complex = False 
        literal_vals = list(set(re.findall(r'[a-zA-Z]+', cls.upd_line)))
        try:
            literal_vals.remove('i')
            is_complex = True
        except ValueError:
            pass

        if len(literal_vals) > 1:
            print('to many unknown vars', len(literal_vals), literal_vals)
            sys.exit('to many unknown')
        elif len(literal_vals) == 0 and is_complex:
            print('its complex   think it could be with matrix')
            cls.handle_complex()
            # sys.exit('poly exit')
        elif len(literal_vals) == 0:
            if '[[' in cls.upd_line:
                print('this is matrix!')
                cls.handle_matrices()
            print('it could be matix or rational expression')
            sys.exit('matrix or rat express')
        elif len(literal_vals) == 1:
            cls.handle_functions()
            print('func')
            sys.exit('eeeexit')

        # what is it
        # cls.upd_line = cls.upd_line.replace('**', '^') # maybe make it earier


    @classmethod
    def handle_complex(cls):
        # print('its comoplex')
        # if '[[' -> means matrix and make complex to matrix
        # print(cls.upd_line)

        cmplx_exp = Complex.exponentiate_line(cls.upd_line) # перенести проверку внутрь класса
        cmplx_exp = Complex.clean_signs(cmplx_exp)
        all_values = re.findall(Complex.REG_CMPLX_VLS, cmplx_exp)
        exec_line = Complex.apply_complex_classes(all_values)

        try: # return val
            print(eval(exec_line))
        # except complex raise
        except:
            print('olololo invalid syntax')
        sys.exit('end of handle complex')

    @classmethod
    def handle_matrices(cls):
        mtrx_exp = Matrix.check_full_line(cls.upd_line)
        mtrx_exp = Matrix.apply_matrix_classes(mtrx_exp)
        try:
            print(eval(mtrx_exp))
        except MatrixException as e:
            print(e) # make it red color
        except: # try to catch it
            print('asdasdas syntax')
        sys.exit('end of matrix exp')

    @classmethod
    def handle_functions(cls):
        print('its func handle!    !!')
        func_exp = Function(cls.upd_line)
        try:
            print(func_exp)
        except: # try to chach this exception
            print('!!')
        # print(cls.upd_line)
        # print('lets rock funcs!')



Handler.handle_line('lol = 2i + 123 + 2i^12')


