import re
from utils import Utils
from equation import Eq
from copy import deepcopy
from calculation import Calc
from itertools import product

class UnknownVar:
    """
    special class for variables inside brackets
    """
    def __init__(self, inpt):
        self.inpt = inpt
        self.value = None
        self.factor = None
        self.power = None

        if not 'x' in self.inpt:
            self.factor = float(inpt)
            self.power = 0
        else:
            self.value = self.clean_inpt
            self.factor = self.get_factor
            self.power = self.get_power

    @property
    def clean_inpt(self):
        return self.inpt.replace('*', '')

    @property
    def get_factor(self):
        if self.value.startswith('-x'):
            return -1
        elif self.value.startswith('+x'):
            return 1
        elif not self.value.startswith('x'):
            return float(self.value.split('x')[0])
        else:
            return 1

    @property
    def get_power(self):
        if not '^' in self.value:
            return 1
        else:
            return float(self.value.split('^')[-1])

    def __mul__(self, other):
        self.factor *= other.factor
        self.power += other.power
        return self

    def __str__(self):
        return f'{Utils.try_int(self.factor)}x^{Utils.try_int(self.power)}'

class FunctionException(Exception):
    pass

class Function:
    """
    REG_WRG_INP_L - checks the input sequence
    REG_IN_PW_PR - finds all expressions in brackets
    REG_PAR_CONT - finds all variables in given expression
    """
    F_ERR_D = {
        1: 'invalid syntax for function expression',
        2: 'the program doesn\'t process nested brackets',
        3: 'the first part must contain the keyword \'fun\'',
        4: 'variable function must be the same as in the expression',
        5: 'unknown variable must not have been initialized before',
        6: 'the function cannot be opened because it is not in the variables'
    }

    REG_WRG_INP_L = r'[a-z]\d'
    REG_IN_PW_PR = r'\(.*?\)\^\d+'
    REG_PAR_CONT = r'[-+]?(?:(?:\d+\.\d*[a-z]?)|(?:\d+?[a-z]+)|(?:\d+)|(?:[a-z]))'

    def __init__(self, inpt):
        # print(inpt)
        if len(re.findall(Function.REG_WRG_INP_L, inpt)):
            raise FunctionException(Function.F_ERR_D[1])
        self.func_content = self.substitute_parentheses(inpt)

    @staticmethod
    def substitute_parentheses(function):
        """
        opens brackets in expression and outputs raw entry
        also correctly opens parentheses if the minus sign precedes the parentheses
        """
        repl_par = function
        par_power_list = list(set(re.findall(Function.REG_IN_PW_PR, function)))
        if len(par_power_list): # list(set repaats here 2 times
            for i in sorted(list(set(par_power_list)), key=len, reverse=True):
                if '(' in i[1:]:
                    raise FunctionException(Function.F_ERR_D[2])
                temp = Function.open_parentheses(i).strip('()')
                temp = Function.apply_reduced_form(temp)
                repl_par = repl_par.replace(i, f'({temp})')
            if not len(re.findall(r'[*/%]', repl_par)):
                minus_par = re.findall(r'-\(.*?\)', repl_par)
                if len(minus_par):
                    for i in sorted(list(set(minus_par)), key=len, reverse=True):
                        temp = i.strip('-()').replace('-', '!').replace('+', '-')
                        temp = '-' + temp.replace('!', '+')
                        repl_par = repl_par.replace(i, temp)
                repl_par = '+' + repl_par.replace('(','').replace(')','') # re.sub
                repl_par = Function.apply_reduced_form(repl_par)
        else:
            repl_par = repl_par.replace('(', '').replace(')', '')
            repl_par = Function.apply_reduced_form(repl_par)
        return repl_par

    @staticmethod
    def apply_reduced_form(piece):
        piece = Calc(f'{piece}=0').get_clean_data()
        piece = Eq(piece).get_reduced_form()
        return piece

    @staticmethod
    def open_parentheses(expression):
        value, power = expression.split('^')
        literal_vals = re.findall(Function.REG_PAR_CONT, value)
        fin = deepcopy(literal_vals)
        for i in range(int(power) - 1):
            prod = list(product(fin, literal_vals))
            fin = []
            for part in prod:
                part = '*'.join([f"UnknownVar('{p}')" for p in part])
                fin.append(eval(part))

        final_output = ''
        for i in range(len(fin)):
            if i == len(fin) - 1:
                final_output += fin[i].__str__()
            else:
                final_output += fin[i].__str__() + '+'

        final_output = '(' + Utils.clean_signs(final_output) + ')'
        return final_output

    def __add__(self, other):
        final_result = f'{self.func_content}+{other.func_content}'
        self.func_content = Utils.clean_signs(final_result)
        self.func_content = self.substitute_parentheses(self.func_content)
        return self

    def __sub__(self, other):
        final_result = f'{self.func_content}-{other.func_content}'
        self.func_content = Utils.clean_signs(final_result)
        self.func_content = self.substitute_parentheses(self.func_content)
        return self
    
    def substitute_operator(self, operator, other):
        final_result = f'({self.func_content}){operator}({other.func_content})'
        self.func_content = Utils.clean_signs(final_result)
        return self

    def __mul__(self, other):
        return self.substitute_operator('*', other)

    def __truediv__(self, other):
        return self.substitute_operator('/', other)

    def __mod__(self, other):
        return self.substitute_operator('%', other)

    def __pow__(self, other):
        return self.substitute_operator('**', other)

    def __str__(self):
        self.func_content = self.func_content.replace('(+', '(')
        if self.func_content[0] == '+':
            self.func_content = self.func_content[1:]
        return self.func_content
