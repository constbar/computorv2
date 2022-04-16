#!/usr/bin/python3

import re
import sys # delete it
from utils import Utils
from matrices import Matrix
from termcolor import colored
from functions import Function, FunctionException
from complex_nums import Complex, ComplexException
from polynomials import Polynomial, PolynomialException


class HandlerException(Exception):
    pass

# check complex + complex from dictionareis
# isinstance(cls.val[:-1], (int, float))
# make chmod ok
# split files to files

class Handler:
    """
    REG_DCT_VLS - substitute values from the internal dictionary
    REG_FLT_EXP - check for integer powers of a number
    REG_NEG_EXP - check for non-negative powers of a number
    REG_POW_RAT - substitute powers for rational numbers
    REG_POW_RAT_BRT - substitute powers for rational numbers in brackets
    REG_POLY_EXEC - validation of the right side for a polynomial
    """

    REG_DCT_VLS = r'(\d+\.\d+|\w+|[^ 0-9])'
    REG_FLT_EXP = r'\^(?:(?:\d*\.))'
    REG_NEG_EXP = r'\^(?:(?:-[2-9]))'
    REG_POW_RAT = r'(?:(?:-?\d+\.?\d?))\^[\d+]'
    REG_POW_RAT_BRT = r'\(-?\d+\.?\d+\)\^\d+'
    REG_POLY_EXEC = r'(?:(?:[a-z]+)|(?:-?\d+\.?\d+))\?'

    REG_ABS = r'abs\([-+]?(?:(?:\d+)|(?:\d+\.\d*))\)'
    REG_COS = r'cos\([-+]?(?:(?:\d+)|(?:\d+\.\d*))\)'
    REG_SIN = r'sin\([-+]?(?:(?:\d+)|(?:\d+\.\d*))\)'
    REG_TAN = r'tan\([-+]?(?:(?:\d+)|(?:\d+\.\d*))\)'
    REG_ATAN = r'atan\([-+]?(?:(?:\d+)|(?:\d+\.\d*))\)'
    REG_RAD = r'rad\([-+]?(?:(?:\d+)|(?:\d+\.\d*))\)'

    REG_MATH = [REG_ABS, REG_SIN, REG_COS, REG_ATAN, REG_TAN, REG_RAD]

    H_ERR_DICT = {
        1: 'expression should have one equal sign',
        2: 'both sides of the expression must be',
        3: '\'i\' can\'t be used for variables',
        4: 'variables should only contain letters',
        33: 'expression must have an integer exponent',
        44: 'expression must have a non-negative exponent',
        99: 'too many unknown vars for expression',
        77: 'variable should have allowed syntax'
    }

    hist = list()
    vals = dict()
    key = None
    val = None
    pre_line = None
    res_line = None
    inst_calc = None

    @classmethod
    def handle_line(cls, input_line):
        cls.null_variables()
        cls.read_expression(input_line)

        # remove it then
        cls.substitute_math_formulas()

        cls.substitute_vals_dict()
        cls.check_exponent()
        cls.exponentiation_rationals()


        cls.handle_expression()


    @classmethod
    def substitute_math_formulas(cls):
        print(cls.val)
        formulas_list = [Utils.make_abs, Utils.make_sin, Utils.make_cos, 
            Utils.make_atan, Utils.make_tan, Utils.make_radians]
        formulas_regs = list(zip(formulas_list, cls.REG_MATH))

        for form, reg in formulas_regs:
            match_list = re.findall(reg, cls.val)
            for repl in sorted(list(set(match_list)), key=len, reverse=True):
                cleared_value = repl[repl.find('(') + 1: repl.find(')')]
                cls.val = cls.val.replace(repl, str(form(float(cleared_value))))
            
        cls.val = Utils.clean_signs(cls.val)
        
        # make modulas for matirux and complex


    @classmethod
    def null_variables(cls):
        cls.key = None
        cls.val = None
        cls.pre_line = None
        cls.res_line = None
        cls.inst_calc = None

    @classmethod
    def read_expression(cls, input_line):
        cls.inst_calc = False
        cls.pre_line = input_line.lower()
        cls.pre_line = cls.pre_line.replace('\t', '').replace(' ', '')

        if cls.pre_line in cls.vals.keys():
            if '[[' in cls.vals[cls.pre_line]:
                print(cls.vals[cls.pre_line][1:-1].replace(';', '\n'))
            else:
                print(cls.vals[cls.pre_line])
            raise

        if cls.pre_line.count('=') != 1:
            raise HandlerException(cls.H_ERR_DICT[1])

        elif not all(cls.pre_line.split('=')):
            raise HandlerException(cls.H_ERR_DICT[2])
        elif cls.pre_line.endswith('=?') and not cls.pre_line.startswith('=?'):
            cls.inst_calc = True
            cls.val = cls.pre_line.split('=')[0]

        if cls.inst_calc is False:
            cls.key, cls.val = cls.pre_line.split('=')
            if cls.key == 'i':
                raise HandlerException(cls.H_ERR_DICT[3])
            elif 'fun' in cls.key:
                if re.sub(Handler.REG_POLY_EXEC, '', cls.val) == '': 
                    cls.prepare_polynomial_key_val()
                    cls.handle_polynomial(f'{cls.key}={cls.val}')
            elif re.search(r'\d', cls.key):
                raise HandlerException(cls.H_ERR_DICT[4])

    @classmethod
    def prepare_polynomial_key_val(cls):
        try:
            cls.key = cls.vals[cls.key]
        except KeyError:
            raise PolynomialException(Polynomial.P_ERR_DICT[1])
        is_num = False
        try:
            float(cls.val[:-1])
            cls.val = cls.val[:-1]
            is_num = True
        except ValueError:
            pass
        if not is_num:
            try:
                cls.val = cls.vals[cls.val[:-1]]
            except KeyError:
                raise PolynomialException(Polynomial.P_ERR_DICT[2])

    @classmethod
    def substitute_vals_dict(cls):
        """
        substitution of funcs that are in the dictionary
        substitution of funcs with parameters that are in the dictionary
        checking that all functions with parameters are substituted
        """
        reg_strd_funcs = r'fun[a-z]+\(.*?\)' # to the top
        reg_func = r'fun[a-z]+\(\d+\.?\d+\)' # with number in
        # print('cls.val   ', cls.val)

        stored_closed_funcs = re.findall(reg_strd_funcs, cls.val)
        for i in sorted(list(set(stored_closed_funcs)), key=len, reverse=True):
            try:
                cls.val = cls.val.replace(i, cls.vals[i])
            except KeyError:
                continue

        # print('before raspr', cls.val)
        stored_open_funcs = re.findall(reg_func, cls.val)
        for i in sorted(list(set(stored_closed_funcs)), key=len, reverse=True):
            stored_value = i[i.find('(') + 1:i.find(')')]
            look = i[:i.find('(') + 1]
            for s in cls.vals.keys():
                stored_letter = s[s.find('(') + 1:s.find(')')]
                if s.startswith(look):
                    try:
                        repl = cls.vals[s].replace(stored_letter, f'*{stored_value}')
                        if repl[0] == '*':
                            repl = repl[1:]
                        elif repl.startswith('-*'):
                            repl = f'{repl[0]}{repl[2:]}'
                        cls.val = cls.val.replace(i, repl)
                    except KeyError:
                        continue
            cls.val = Utils.clean_signs(cls.val)
            # print(cls.val)

        if re.findall(reg_func, cls.val):
            raise FunctionException(Function.F_ERR_D[6])
        
        # print('cls.val    ', cls.val)
        # sys.exit()

        val_list = re.findall(cls.REG_DCT_VLS, cls.val)
        for i in range(len(val_list)):
            if val_list[i].isalpha():
                try:
                    val_list[i] = str(cls.vals[val_list[i]])
                except KeyError:
                    continue
        cls.res_line = ''.join(val_list)

    @classmethod
    def check_exponent(cls):
        if re.findall(cls.REG_FLT_EXP, cls.res_line):
            raise HandlerException(cls.H_ERR_DICT[33])
        elif re.findall(cls.REG_NEG_EXP, cls.res_line):
            raise HandlerException(cls.H_ERR_DICT[44])

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
        # print('1', cls.res_line)
        cls.res_line = Utils.clean_signs(cls.res_line)
        # print('1', cls.res_line)

        rat_pow_brt_list = re.findall(Handler.REG_POW_RAT_BRT, cls.res_line)
        for i in sorted(list(set(rat_pow_brt_list)), key=len, reverse=True):
            temp = i
            temp = eval(temp.replace('^', '**'))
            cls.res_line = cls.res_line.replace(i, '+' + str(temp))
        # print('2', cls.res_line)
        cls.res_line = Utils.clean_signs(cls.res_line)
        # print('2', cls.res_line)

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
            raise HandlerException(cls.H_ERR_DICT[99])
        elif len(literal_vals) == 0 and is_complex:
            cls.handle_complex()
        elif len(literal_vals) == 0:
            if '[[' in cls.res_line:
                cls.handle_matrices()
            else:
                if '(' in str(cls.key) or ')' in str(cls.key):
                    if not cls.key.count('(') == cls.key.count(')'):
                        raise HandlerException(cls.H_ERR_DICT[77])
                cls.val = Utils.try_int(eval(cls.res_line))
                cls.prnt_hist_vals()
        elif len(literal_vals) == 1:
            cls.handle_functions(literal_vals)

    @classmethod
    def handle_complex(cls):
        if re.findall(Complex.REG_WRG_INP_I, cls.res_line):
            raise ComplexException(Complex.C_ERR_D[3])
        cmplx_exp = Complex.exponentiate_line(cls.res_line)
        cmplx_exp = Utils.clean_signs(cmplx_exp)
        cmplx_vals = re.findall(Complex.REG_CMPLX_VLS, cmplx_exp)
        exec_line = Complex.apply_complex_classes(cmplx_vals)
        exec_line = Utils.clean_signs(exec_line)
        cls.val = f'{eval(exec_line)}'
        cls.prnt_hist_vals()

    @classmethod
    def handle_matrices(cls):
        mtrx_exp = Matrix.check_full_line(cls.res_line)
        exec_line = Matrix.apply_matrix_classes(mtrx_exp)
        cls.val = f'{eval(exec_line)}'
        cls.prnt_hist_vals()

    @classmethod
    def handle_functions(cls, literal_vals):
        if not cls.key.startswith('fun'):
            raise FunctionException(Function.F_ERR_D[3])
        elif not '(' in cls.key and not ')' in cls.key:
            raise FunctionException(Function.F_ERR_D[4]) #
        key_var = cls.key[cls.key.find('(') + 1:cls.key.find(')')]
        if key_var != literal_vals[0]:
            raise FunctionException(Function.F_ERR_D[5])
        elif key_var in cls.vals.keys():
            raise FunctionException(Function.F_ERR_D[6])
        elif cls.res_line.count('(') != cls.res_line.count(')'):
            raise FunctionException(Function.F_ERR_D[7])
        cls.res_line = cls.res_line.replace(literal_vals[0], 'x')
        cls.val = str(Function(Function(cls.res_line).__str__()))
        cls.val = cls.val.replace('x', key_var)
        cls.prnt_hist_vals()

    @classmethod
    def handle_polynomial(cls, poly):
        literal_val = list(set(re.findall(r'[a-zA-Z]+', poly)))[0]
        poly = poly.replace(literal_val, 'x')
        print(poly.replace(' ', ''))
        Polynomial(poly, print_answer=True)
        raise

    @classmethod
    def prnt_hist_vals(cls):

        # print(colored(cls.val, 'green'))
        if '[[' in str(cls.val):
            print(cls.val[1:-1])
        else:
            print(cls.val)

        if cls.inst_calc is False:
            # if 'fun' in cls.key:
                # cls.key = cls.key[:cls.key.find('(')]
            if isinstance(cls.val, int) or isinstance(cls.val, float):
                cls.vals[cls.key] = str(cls.val)
            elif '[' in cls.val:
                cls.vals[cls.key] = '[' + cls.val.replace('\n', ';') + ']'
            else:
                cls.vals[cls.key] = str(cls.val)
        cls.hist.append(f'{cls.pre_line.split("=")[0]} -> {cls.val}')

        # print('slovar', cls.vals)

# poly doesnt work

Handler.handle_line('cos(0) =?')
# Handler.handle_line('x = cos(122) + atan(22) + abs(-2) + sin(-3) - tan(2) + rad(2)')
# Handler.handle_line('1+2=?') good
# Handler.handle_line('func(x)=c?')
# Handler.handle_line('func(x)=14?')

# Handler.handle_line('funA(x) = z?')
# Handler.handle_line('x+x= 2') # poly x = 0 # ne reshaetsya


# print('12.2'.isnumeric())
# Handler.handle_line("func(x) = 123123123x  - 2^3") #  good
