#!/usr/bin/python3

import re
import sys
from termcolor import colored


class Cmplx:
    def __init__(self, piece: str):
        self.re = 0
        self.im = 0
        self.co = False
        if '+' in piece:
            piece = piece.replace('+', '')
        if 'i' in piece: # or big I
            self.co = True
            if piece == '-i' or piece == 'i':
                self.im = float(piece.replace('i', '1'))
            else:
                self.im = float(piece.strip('i'))
        else:
            # print(piece)
            self.re = float(piece)
            # self.re = i/nt(piece)
        
    def __str__(self):
        return_dict = dict()
        return_dict['real'] = self.re
        return_dict['imag'] = self.im
        return Cmplx.make_str_output(return_dict)

        # return ''
        # return f'{self.re}+{self.im}i'

    def __add__(self, other):
        self.re = self.re + other.re
        self.im = self.im + other.im
        return self

    def __sub__(self, other):
        self.re = self.re - other.re
        self.im = self.im - other.im
        return self

    # make it cleaner
    def __mul__(self, other):
        # other conmplex else just mult
        # here an error when it called 
        fi1 = Cmplx(f'{self.re * other.re}')
        fi2 = Cmplx(f'{self.re * other.im}i')
        sc1 = Cmplx(f'{self.im * other.re}i')
        # sc2 = f'{self.im * other.im}i^2'
        sc2 = Cmplx.simplify_expression(f'{self.im * other.im}i^2')
        sc2 = Cmplx.clean_signs(sc2) # make if more clever
        sc2 = Cmplx(sc2)
        fin = fi1 + fi2 + sc1 + sc2
        # print(fin)
        # print(fi1)
        # print(fi2)
        # print(sc1)
        # print(sc2)
        print()
        # Cmplx.simplify_expression(sc2)
        return fin

    def __pow__(self, power):
        # не рабоает со степень больше 2
        if power.co is True:
            return 'exponent must be an integer'
        print(self)
        print(power)
        # сделатть перегрузку присваивания
        tmp = self
        print()
        for i in range(int(power.re) - 1):
            tmp = tmp * tmp
            # print(tmp)
        print(tmp)
        # self =
        print() 
        return 'a'

        # check it if it less than 0
        # print(type(self.re))
        # print()
        # self.re = self.re ** power.re
        # self.im = self.im ** power.re
        # print(f'{self.re} + {self.im}i^{power.re}')
        # exit()
        # return self


    REG_POW_COMPL = r'-?(?:(?:\d+)|(?:\d+\.\d+))\*?[iI]\^\d+'


    # make it better
    def make_str_output(res_dict: dict) -> str:
        f = ''
        if res_dict['real']:
            f += str(res_dict['real'])
        if res_dict['imag']:
            if res_dict['imag'] > 0 and res_dict['real']:
                f += ' + '
            f += str(res_dict['imag']) + 'i'
        return f

    # this only for i's
    # think about dict value = False
    @staticmethod
    def pow_replacer(part: str, diction=False): # или part is class regex <class 're.Match'>
        if type(part).__name__ == 'Match': # need i?
            part = part.group(0).replace('*', '')
        else:
            part = part.replace('*', '')

        clx_dict = dict()
        clx_dict['real'] = 0
        clx_dict['imag'] = 0
        clx_dict['imag'], clx_dict['pw'] = part.split('^')
        clx_dict['imag'] = clx_dict['imag'].replace('i', '')

        clx_dict['imag'] = float(clx_dict['imag'])
        clx_dict['pw'] = int(clx_dict['pw'])
        # check if it real int func
        if clx_dict['pw'] % 4 == 0:
            clx_dict['real'] = clx_dict['imag']
            clx_dict['imag'] = 0
        elif clx_dict['pw'] % 4 == 3:
            clx_dict['imag'] *= -1
        elif clx_dict['pw'] % 4 == 2:
            clx_dict['real'] = clx_dict['imag'] * -1
            clx_dict['imag'] = 0
        return '+' + Cmplx.make_str_output(clx_dict)

    @staticmethod
    def clean_signs(raw_str:str) -> str:
        raw_str = raw_str.replace('-+', '-')
        raw_str = raw_str.replace('++', '+')
        raw_str = raw_str.replace('+-', '-')
        return raw_str

    @staticmethod
    def simplify_expression(expression: str) -> str:
        result = re.sub(Cmplx.REG_POW_COMPL, Cmplx.pow_replacer, expression)
        return result




# kek = Cmplx.simplify_expression('(3i^5+10*i^5) +3*2i-i+i-1*i+20')
# kek = Cmplx.simplify_expression('i')
# kek = Cmplx.simplify_expression('20.0i^2')
# kek = Cmplx.clean_signs(kek)
# print(kek)
# print(kek)

# # asn = r'(\d+\.\d+i|\w+|[^ 0-9])'
# asn = r'[-+]?(?:(?:\d+\.\d+)|(?:\d+)|(?:[iI]))[iI]?'
# # val_list = re.findall(re.compile(asn), kek)
# # print(val_list)

# lol = re.sub(asn, ' !!! ', kek)
# print(lol)

# заменяем все занчения на str(Cmplx(val))
# потом делаем эвал


# q = Cmplx('30i') - (Cmplx('-12i') + Cmplx('12')) # + Cmplx('31')
# print((Cmplx('5') + Cmplx('2i')) ** Cmplx('3'))
# print(Cmplx('5') * Cmplx('3i'))

# print((Cmplx('2') + Cmplx('20i')) * (Cmplx('10') - Cmplx('i')))
# print(Cmplx('5i') * Cmplx('3')) # error
# print(Cmplx('5i') * Cmplx('3i'))
print(Cmplx('5i') ** Cmplx('2'))
# print(Cmplx('5i'))