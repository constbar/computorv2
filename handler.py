#!/usr/bin/python3

import re
import sys
from termcolor import colored

from complex_nums import ComplexException, Complex
from matrices import MatrixException, Matrix
from functions import Function
from utils import Utils

# case sensetive should be turned off
# what to do with big I
# need dpu the in all exceptioons
# write here about all regex


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

        88: 'invalid syntax for complex expression'
        #        # 5: 'expression can only have allowed syntax',
        #        # 6: 'it\'s just a numerical equation. no solution',
        #        # 7: 'it\'s an incorrect numerical equation. no solution',
        #        # 8: 'each real number is a solution',
    }

    REG_ALWD_SMBLS = r'(\d+\.\d+|\w+|[^ 0-9])'
    REG_FLT_EXP = r'\^(?:(?:\d*\.))'
    REG_NEG_EXP = r'\^(?:(?:-[2-9]))'
    
    REG_POW_RAT = r'(?:(?:-?\d+\.?\d?))\^[\d+]'
    REG_RAT_POW_BRT = r'\(-?\d+\.?\d+\)\^\d+'

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
            print(cls.vals) # shiouild be in test.py
            raise

        cls.pre_line = input_line.lower()
        cls.pre_line = cls.pre_line.replace('\t', '').replace(' ', '')

        if cls.pre_line.count('=') != 1:
            raise HandlerException(cls.ERR_DICT[1])

        elif cls.pre_line.endswith('=?') and not cls.pre_line.startswith('=?'):
            print('make instant computations')
            return # 
        elif not all(cls.pre_line.split('=')):
            raise HandlerException(cls.ERR_DICT[2])
            # maybe make here a flag or smth ..

        cls.key, cls.val = cls.pre_line.split('=')


        if cls.key in cls.vals.keys():
            print(cls.vals[cls.key])
            raise

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
        """
        replacing all rational exponents without brackets
        replacing all rational exponents with brackets

        """
        rat_pow_list = re.findall(Handler.REG_POW_RAT, cls.res_line)
        for i in sorted(list(set(rat_pow_list)), key=len, reverse=True):
            temp = i
            temp = eval(temp.replace('^', '**'))
            cls.res_line = cls.res_line.replace(i, '+' + str(temp))

        rat_pow_brt_list = re.findall(Handler.REG_RAT_POW_BRT, cls.res_line)
        for i in sorted(list(set(rat_pow_brt_list)), key=len, reverse=True):
            temp = i
            temp = eval(temp.replace('^', '**'))
            cls.res_line = cls.res_line.replace(i, '+' + str(temp))

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
        if re.findall(Complex.REG_WRG_INP_I, cls.res_line):
            raise ComplexException(cls.ERR_DICT[88])
        cmplx_exp = Complex.exponentiate_line(cls.res_line)
        cmplx_exp = Utils.clean_signs(cmplx_exp)
        all_values = re.findall(Complex.REG_CMPLX_VLS, cmplx_exp)
        exec_line = Complex.apply_complex_classes(all_values)
        exec_line = Utils.clean_signs(exec_line)
        cls.val = f'{eval(exec_line)}'
        cls.prnt_hist_vals()

    @classmethod
    def handle_matrices(cls):
        mtrx_exp = Matrix.check_full_line(cls.res_line)
        exec_line = Matrix.apply_matrix_classes(mtrx_exp)
        cls.val = f'{eval(exec_line)}'
        # cls.val = cls.val.replace('\n', ';')  # printed val ot the same as stored
        cls.prnt_hist_vals()

    @classmethod
    def handle_functions(cls):
        cls.val = Function(Function(cls.res_line).__str__())
        cls.prnt_hist_vals()

    @classmethod
    def prnt_hist_vals(cls):
        # print(colored(cls.val, 'green'))
        print((cls.val))
        cls.vals[cls.key] = cls.val

        # not shure that it needs work like this
        # cls.hist.append(f'{cls.pre_line.split("=")[-1]} -> {cls.val}')
        # print(cls.hist)


# Handler.handle_line('lol = 3i + 23')
# Handler.handle_line('lol = [[1,2];[2,3]]^-1')
# Handler.handle_line('x=[[1]]^[[2]]') # good error


# Handler.handle_line('x= (5i)^0') # 1 good
# Handler.handle_line('x=i1')
# Handler.handle_line('x=x1x')
# Handler.handle_line('x=((1x + 12))^2') # good err
# Handler.handle_line('x=(1x + 12)^2')
# Handler.handle_line('x=(2 + 5x)^4+200+123+x^2 + (x)^2+1000')
# fa = Function.('(2 + 5x)^4+20+123+312+123+3452345-(sdfsd)')
# fa = Function('(2 + 5x)^4+20+123+312+123+3452345+(123+2)^2')

# fa = Function('(2 + 5x)^2+20-(12)^2')
# fa = Function('(22 + 5.5x)^3') + Function('(2 + 5x)^2')
# fa = Function('(2.4 + 5.2*x)^2+20')
# fa = Function('(2 + 5x)^2+(2 + 5x)^2-(2-2x)^3')
# fa = Function('(2-2x)^3/123/(2-2x+2+2)^3')
# fa = Function('(2-2x)^3/123/(2-2x+2/2)^3')
# fa = Function('(2 + 5x)^2+(4+2x)^2+20-123')
# fa = Function('(2 + 5x)^2/(4+2x)^2+20x+123+22+21') % Function('(2 + 5x)^2/(4+2x)^3+20x+123+22+21')

# fa = Function('(2x+(5x+2))^2') # break it !!!!!!!!!!!!! no ( inside ())
# fa = Function('(2+2)^2') # solve it solution can be  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(fa)

# kek = '(4+10x^1+10x^1+25x^2)/(16+8x^1+8x^1+4x^2)+20x+123+22+21%((4+10x^1+10x^1+25x^2)/(64+32x^1+32x^1+16x^2+32x^1+16x^2+16x^2+8x^3)+20x+123+22+21)'
# kek = kek.replace('x', '*2').replace('^', '**')
# print(eval(kek))

# fa = Function.open_brackets('(2-1.5x)^13')
# fa = Function('x+2+2xx+2-3+1-1-2-200-2.2x+x+123+12*x+12.2') + Function('+2+x+2-3+1-1-2+200')
# fa = Function('x+2+2xx+2-3+1-1-2-200-2.2x+x+123+12*x+12.2') ** Function('+2+x+2-3+1-1-2+200')
# fa = Function('+2+x+2-3+1-1-2+200')
# fa = Function('x+x+2x+3x+10x+23+23-10x-10*x/12')
# fa = Function('+2+2x+2-3+1-1-2+200')# + Function('+2+x+2-3+1-1-2+200')
# print(fa)
# need pow tests





# Handler.handle_line('lol = 12i2123') # ok error shiould come
# Handler.handle_line('lol = 12i + 123-123+2+2^2')

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



