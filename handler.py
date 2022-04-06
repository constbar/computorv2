#!/usr/bin/python3

import re
import sys
from termcolor import colored

from complex_nums import Complex
from matrices import MatrixException, Matrix
from functions import Function
from utils import Utils

# case sensetive should be turned off

class HandlerException(Exception):
    pass

class Handler:
    # HISTORY of all inputs -> cls.method
    ERR_DICT = {
        1: 'expression should have one equal sign',
        2: 'both sides of the expression must be',
        3: '\'i\' can\'t be used for variables',
        4: 'variables should only contain letters',
        33: 'expression must have an integer exponent',
        44: 'expression must have a non-negative exponent',
        99: 'too many unknown vars for expression',
        #        # 5: 'expression can only have allowed syntax',
        #        # 6: 'it\'s just a numerical equation. no solution',
        #        # 7: 'it\'s an incorrect numerical equation. no solution',
        #        # 8: 'each real number is a solution',
    }

    REG_ALWD_SMBLS = r'(\d+\.\d+|\w+|[^ 0-9])'
    REG_FLT_EXP = r'\^(?:(?:\d*\.))'
    REG_NEG_EXP = r'\^(?:(?:-\d))'    

    vals_dict = {'a': '20', 'b': 'asd', 'varC': 'smth'} # make 0 init
    line = None
    key = None
    val = None
    upd_line = None

    @classmethod
    def handle_line(cls, input_line):
        cls.read_expression(input_line)
        cls.substitute_vals_dict()
        cls.check_exponent()

        cls.exponentiation_rationals()
        cls.execute_expression()

    @classmethod
    def read_expression(cls, input_line):
        cls.line = input_line.lower()
        cls.line = cls.line.replace('\t', '').replace(' ', '')

        if cls.line.count('=') != 1:
            raise HandlerException(cls.ERR_DICT[1])
        elif cls.line.endswith('=?') and not cls.line.startswith('=?'):
            print('make instant computations')
            return
        elif not all(cls.line.split('=')):
            raise HandlerException(cls.ERR_DICT[2])
            # maybe make here a flag or smth ..

        cls.key, cls.val = cls.line.split('=') # was else here

        if cls.key == 'i':
            raise HandlerException(cls.ERR_DICT[3])
        elif not cls.key.isalpha():
            raise HandlerException(cls.ERR_DICT[4])

    @classmethod
    def substitute_vals_dict(cls):
        val_list = re.findall(re.compile(cls.REG_ALWD_SMBLS), cls.val)
        for i in range(len(val_list)):
            if val_list[i].isalpha():
                try:
                    val_list[i] = cls.vals_dict[val_list[i]]
                except KeyError:
                    continue
        cls.upd_line = ''.join(val_list)

    @classmethod
    def check_exponent(cls):
        if re.findall(cls.REG_FLT_EXP, cls.upd_line):
            raise HandlerException(cls.ERR_DICT[33])
        elif re.findall(cls.REG_NEG_EXP, cls.upd_line):
            raise HandlerException(cls.ERR_DICT[44])

    @classmethod
    def exponentiation_rationals(cls):
        REG_POW_RAT = r'\(?(?:(?:-?\d+\.?\d?))\)?\^[\d+]' # to the beg
        rat_pow_list = re.findall(REG_POW_RAT, cls.upd_line)
        for i in sorted(list(set(rat_pow_list)), key=len, reverse=True):
            temp = i
            if not '(' in temp:
                temp = temp.replace('-', '')
            temp = eval(temp.replace('^', '**'))
            cls.upd_line = cls.upd_line.replace(i, '+' + str(temp))

        # print('old', cls.upd_line)
        # print('new', Utils.clean_signs(cls.upd_line))


    @classmethod
    def execute_expression(cls):
        is_complex = False 
        literal_vals = list(set(re.findall(r'[a-zA-Z]+', cls.upd_line)))
        try:
            literal_vals.remove('i')
            is_complex = True
        except ValueError:
            pass

        print('before execute', cls.upd_line)

        if len(literal_vals) > 1:
            raise HandlerException(cls.ERR_DICT[99])
        elif len(literal_vals) == 0 and is_complex:
            cls.handle_complex()
        elif len(literal_vals) == 0:
            if '[[' in cls.upd_line:
                cls.handle_matrices()
            else:
                try:
                    # !
                    print(eval(cls.upd_line))
                except:
                    print('except error!!')
        elif len(literal_vals) == 1:
            cls.handle_functions()
        print('end of execute')

    @classmethod
    def handle_complex(cls):
        # Complex.check_full_line(cls.upd_line) !
        cmplx_exp = Complex.exponentiate_line(cls.upd_line)
        cmplx_exp = Utils.clean_signs(cmplx_exp)
        all_values = re.findall(Complex.REG_CMPLX_VLS, cmplx_exp)
        exec_line = Complex.apply_complex_classes(all_values)

        try: # return val
            print(eval(exec_line))
        # except complex raise
        except:
            print('olololo invalid syntax')
        sys.exit()


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
        sys.exit()

    @classmethod
    def handle_functions(cls):
        print('its func handle!    !!')
        func_exp = Function(cls.upd_line)
        try:
            print(func_exp)
        except: # try to chach this exception
            print('!!')
        sys.exit()
        # print(cls.upd_line)
        # print('lets rock funcs!')



# Handler.handle_line('lol = 2123 + 12i')
# Handler.handle_line('lol = (-12.2)^2 + (12.2)^2')
# Handler.handle_line('lol = 21.1i + 123-123i^12 -12^2 - 111^1 * 123^2 / 1^1 - (-12.2)^2 + (12.2)^2') # make formating here 
# Handler.handle_line('lol = 21.1i + (-12)^2')
# Handler.handle_line('lol = [[1.2,2,3]] + [[1.2,2,3]]')
# Handler.handle_line('lol = 20 + 390')
# Handler.handle_line('lol = 20 + 390.2i')
# Handler.handle_line('lol = [[1,2,3.3]]^[[1,2,3.3]]') # chekck it/
# Handler.handle_line('lol = [[1,2];[2,3]] % [12]') # error
# Handler.handle_line('lol = [[1,2];[2,3]] % 2') # came to [[ and .. none..
Handler.handle_line('lol = 22^[[1,2];[2,3]]')


