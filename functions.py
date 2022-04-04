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
# проверка на вложенные (   ())

class UnknownVar:
    # class specially made for working with vars in parentheses
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
            return -1.0
        elif not self.value.startswith('x'):
            return float(self.value.split('x')[0])
        else:
            return 1.0

    @property
    def get_power(self):
        if not '^' in self.value:
            return 1.0
        else:
            return float(self.value.split('^')[-1])

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
    REG_IN_PW_PR = r'\(.*?\)\^\d+'
    REG_PAR_CONT = r'[-+]?(?:(?:\d+\.\d*[a-z]?)|(?:\d+?[a-z]+)|(?:\d+)|(?:[a-z]))'

    def __init__(self, inpt):
        self.func_content = self.substitute_parentheses(inpt)

    @staticmethod
    def substitute_parentheses(function):
        repl_par = function
        par_power_list = list(set(re.findall(Function.REG_IN_PW_PR, function)))
        if len(par_power_list):
            for i in sorted(list(set(par_power_list)), key=len, reverse=True):
                temp = Function.open_parentheses(i).strip('()')
                temp = Calc(f'{temp}=0').get_clean_data()  # rework it
                temp = Eq(temp).get_reduced_form()         # rework it
                repl_par = repl_par.replace(i, f'({temp})')

            if not len(re.findall(r'[*/%]', repl_par)):
                minus_par = re.findall(r'-\(.*?\)', repl_par)
                if len(minus_par):
                    for i in sorted(list(set(minus_par)), key=len, reverse=True):
                        temp = i.strip('-()').replace('-', '!').replace('+', '-')
                        temp = '-' + temp.replace('!', '+')
                        repl_par = repl_par.replace(i, temp)
                repl_par = '+' + repl_par.replace('(','').replace(')','')
                kek = Calc(f'{repl_par}=0').get_clean_data()  # rework it
                lol = Eq(kek).get_reduced_form()              # rework it
        else:
            repl_par = repl_par.replace('(', '').replace(')', '')
            repl_par = Calc(f'{repl_par}=0').get_clean_data()  # rework it
            repl_par = Eq(repl_par).get_reduced_form()         # rework it
        return repl_par

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



# fa = Function.open_brackets('(2 + 5x)^4')
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






