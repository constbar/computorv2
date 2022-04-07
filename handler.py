#!/usr/bin/python3

import re
import sys
from termcolor import colored

from complex_nums import ComplexException, Complex
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

    hist = list()
    vals = dict()
    key = None
    val = None
    pre_line = None
    res_line = None

    @classmethod
    def handle_line(cls, input_line):
        cls.read_expression(input_line)
        cls.substitute_vals_dict()
        cls.check_exponent()
        cls.exponentiation_rationals()
        cls.handle_expression()

    @classmethod
    def read_expression(cls, input_line):
        if input_line == 'LOL':# delete
            print(cls.vals)
            raise

        cls.pre_line = input_line.lower()
        cls.pre_line = cls.pre_line.replace('\t', '').replace(' ', '')

        if cls.pre_line.count('=') != 1:
            raise HandlerException(cls.ERR_DICT[1])

        elif cls.pre_line.endswith('=?') and not cls.pre_line.startswith('=?'):
            print('make instant computations')
            return
        elif not all(cls.pre_line.split('=')):
            raise HandlerException(cls.ERR_DICT[2])
            # maybe make here a flag or smth ..

        cls.key, cls.val = cls.pre_line.split('=') # was else here

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
                    val_list[i] = cls.vals[val_list[i]]
                except KeyError:
                    continue
        cls.res_line = ''.join(val_list)

    @classmethod
    def check_exponent(cls):
        if re.findall(cls.REG_FLT_EXP, cls.res_line):
            raise HandlerException(cls.ERR_DICT[33])
        elif re.findall(cls.REG_NEG_EXP, cls.res_line):
            raise HandlerException(cls.ERR_DICT[44])

    @classmethod
    def exponentiation_rationals(cls):
        REG_POW_RAT = r'\(?(?:(?:-?\d+\.?\d?))\)?\^[\d+]' # to the beg
        rat_pow_list = re.findall(REG_POW_RAT, cls.res_line)
        for i in sorted(list(set(rat_pow_list)), key=len, reverse=True):
            temp = i
            if not '(' in temp:
                temp = temp.replace('-', '')
            temp = eval(temp.replace('^', '**'))
            cls.res_line = cls.res_line.replace(i, '+' + str(temp))

        # print('old', cls.res_line)
        # print('new', Utils.clean_signs(cls.res_line))


    @classmethod
    def handle_expression(cls):
        is_complex = False 
        literal_vals = list(set(re.findall(r'[a-zA-Z]+', cls.res_line)))
        try:
            literal_vals.remove('i')
            is_complex = True
        except ValueError:
            pass

        if len(literal_vals) > 1:
            raise HandlerException(cls.ERR_DICT[99])
        elif len(literal_vals) == 0 and is_complex:
            cls.handle_complex()
        elif len(literal_vals) == 0:
            if '[[' in cls.res_line:
                cls.handle_matrices()
            else:
                cls.val = eval(cls.res_line)
                cls.prnt_hist_vals()
        elif len(literal_vals) == 1:
            cls.handle_functions()

    @classmethod
    def handle_complex(cls):
        cmplx_exp = Complex.exponentiate_line(cls.res_line)
        cmplx_exp = Utils.clean_signs(cmplx_exp)
        all_values = re.findall(Complex.REG_CMPLX_VLS, cmplx_exp)
        exec_line = Complex.apply_complex_classes(all_values)
        # cls.execute_expression(exec_line)
        cls.val = f'{eval(exec_line)}'
        cls.prnt_hist_vals()

    @classmethod
    def handle_matrices(cls):
        mtrx_exp = Matrix.check_full_line(cls.res_line)
        exec_line = Matrix.apply_matrix_classes(mtrx_exp)
        cls.val = f'{eval(exec_line)}'
        cls.val = cls.val.replace('\n', ';')
        cls.prnt_hist_vals()

    @classmethod
    def handle_functions(cls):
        exec_line = Function(cls.res_line)
        cls.prnt_hist_vals()

    @classmethod
    def prnt_hist_vals(cls):
        print(colored(cls.val, 'green'))
        cls.vals[cls.key] = cls.val

        # not shure that it needs work like this
        cls.hist.append(f'{cls.pre_line.split("=")[-1]} -> {cls.val}')
        print(cls.hist)



    # @classmethod
    # def execute_expression(cls, exec_line):
    #     # try:
    #     # print(eval(exec_line)) # make colored
    #     cls.val = f'{eval(exec_line)}'
    #     print(colored(cls.val, 'green'))
    #     if '[' in cls.val:
    #         cls.val = cls.val.replace('\n', ';')
    #     cls.vals[cls.key] = cls.val
    #     # except ComplexException as e: # need i?
    #     #     print(e)
    #     # except MatrixException as e:
    #     #     print(colored(e, 'yellow'))
    #     # except:
    #     #     print('olololo invalid syntax')



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
# Handler.handle_line('lol = 22^[[1,2];[2,3]]')
# 3i902342 error should be error
# > x = 11233x 1212 # error'



