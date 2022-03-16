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
        
    def __str__(self):
        return f'{self.re}+{self.im}i'

    def __add__(self, other):
        self.re += other.re
        self.im += other.im
        return self

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
    def pow_replacer(part: str, diction=False):
        part = part.group(0).replace('*', '')
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

    # def __pow__(self, power):
    #     if self.re and self.im:
    #         print(123)



# kek = Cmplx.simplify_expression('(3i^5+10*i^5) +3*2i-i+i-1*i+20')
# kek = Cmplx.clean_signs(kek)
# print(kek)

# # asn = r'(\d+\.\d+i|\w+|[^ 0-9])'
# asn = r'[-+]?(?:(?:\d+\.\d+)|(?:\d+)|(?:[iI]))[iI]?'
# # val_list = re.findall(re.compile(asn), kek)
# # print(val_list)

# lol = re.sub(asn, ' !!! ', kek)
# print(lol)

# заменяем все занчения на str(Cmplx(val))
# потом делаем эвал


q = Cmplx('20i') + Cmplx('30i') + Cmplx('31')
print(q)