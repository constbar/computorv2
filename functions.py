import re
import sys
from copy import deepcopy
from termcolor import colored

from utils import Utils
from calculation import Calc
from equation import Eq
from itertools import product

# regex vinesti v nachalo
# unknow n var coul be any num
# REGs with upper case



class UnknownVar:
    # class specially made for working with vars in parentheses
    def __init__(self, inpt):
        self.inpt = inpt
        self.val = None
        self.factor = None
        self.power = None

        if not 'x' in self.inpt:
            self.factor = float(inpt)
            self.power = 0
        else:
            self.val = self.clean_inpt
            self.factor = self.get_factor
            self.power = self.get_power

    @property
    def clean_inpt(self):
        return self.inpt.replace('*', '')

    @property
    def get_factor(self):
        if self.val.startswith('-x'):
            return -1.0
        elif not self.val.startswith('x'):
            return float(self.val.split('x')[0])
        else:
            return 1.0

    @property
    def get_power(self):
        if not '^' in self.val:
            return 1.0
        else:
            return float(self.val.split('^')[-1])

    def __mul__(self, other):
        self.factor *= other.factor
        self.power += other.power
        return self

    def __str__(self):
        return f'{Utils.try_int(self.factor)}x^{Utils.try_int(self.power)}'
        # factor countd be 1 and power not be 0 1 при выводе


# k = UnknownVar('12') * UnknownVar('12x^23')
# k = UnknownVar('+3') 
# print(k)
# k = UnknownVar('2x^2') * UnknownVar('20*x^30')
# k = UnknownVar('2x^2') * 20
# k = 20 * UnknownVar('2x^2') * UnknownVar('x^3')
# k = 20 * UnknownVar('2x^2')
# k = UnknownVar('x^0')


class Function:
    reg_parentheses = r'\(.*?\)\^\d+'
    def __init__(self, inpt):
        self.inpt = inpt
        self.func_content = self.substitute_parentheses() # if it neccesary
        # self.func_content = self.count_rationals(self.func_content) # if count used 1 time -> make not static

    def substitute_parentheses(self):
        replaced_par = self.inpt
        parentheses_list = list(set(re.findall(Function.reg_parentheses, self.inpt)))
        
        for i in parentheses_list:
            replaced_par = replaced_par.replace(i, Function.open_parentheses(i))
            print(replaced_par)

!        # HERE START OPEN PARENTHESES V IN case of -+ or smth

        # check for minuses i meanr in parentheses

        # print(replaced_par.strip('()'))
        # replaced_par = replaced_par.strip('()')

        # # print(Calc(f'{replaced_par}=0'))
        # kek = Calc(f'{replaced_par}=0').get_clean_data()  # rework it
        # lol = Eq(kek).get_reduced_form()  # rework it
        # print(lol)
        sys.exit()

        return replaced_par

    @staticmethod
    def count_rationals(expression):
        cleaned_expression = expression
        # onlyu gets lower case
        reg_not_rat = r'[-+]?(?:(?:\d*\*?[a-z]+)|(?:\d*\.\d*\*?[a-z]+))' # what is it 
        literal_vals = re.findall(reg_not_rat, expression)

        for i in sorted(list(set(literal_vals)), key=len, reverse=True):
            cleaned_expression = cleaned_expression.replace(i, '')

        if not len(re.findall(r'[()*/%^]', cleaned_expression)):
            rational_result = eval(cleaned_expression)
            if rational_result < 0:
                return f"{''.join(literal_vals)}{rational_result}"
            else:
                return f"{''.join(literal_vals)}+{rational_result}"
        return expression

    @staticmethod
    def open_parentheses(expression):
        value, power = expression.split('^')

        # reg_not_rat = r'[-+]?(?:(?:\d+?[a-z]+)|(?:\d+)|(?:[a-z]))' # old
        reg_not_rat = r'[-+]?(?:(?:\d+\.\d*[a-z]?)|(?:\d+?[a-z]+)|(?:\d+)|(?:[a-z]))'
        literal_vals = re.findall(reg_not_rat, value)

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

        final_output = '(' + Utils.clean_signs(final_output) + ')' # no need )()
        return final_output
        # return final_output.replace('x^0', '').replace('x^1', 'x')

    def __add__(self, other):
        final_result = f'{self.func_content}+{other.func_content}'
        self.func_content = Utils.clean_signs(final_result)
        return self

    def substitute_operator(self, operator, other):
        final_result = f'{self.func_content}{operator}({other.func_content})'
        self.func_content = Utils.clean_signs(final_result)
        return self

    def __sub__(self, other):
        return self.substitute_operator('-', other)

    def __mul__(self, other):
        return self.substitute_operator('*', other)

    def __truediv__(self, other):
        return self.substitute_operator('/', other)

    def __mod__(self, other):
        return self.substitute_operator('%', other)

    def __pow__(self, other):
        return self.substitute_operator('**', other)

    def __str__(self):
        return self.func_content



# fa = Function.open_brackets('(2 + 5x)^4')
# fa = Function.('(2 + 5x)^4+20+123+312+123+3452345-(sdfsd)')
# fa = Function('(2 + 5x)^4+20+123+312+123+3452345+(123+2)^2')

# fa = Function('(2 + 5x)^2')
fa = Function('(2 + 5x)^2+(4+2x)^2+20-123')
# fa = Function('(2 + 5x)^2/(4+2x)^2+20x+123+22+21') % Function('(2 + 5x)^2/(4+2x)^3+20x+123+22+21')
print(fa)

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






