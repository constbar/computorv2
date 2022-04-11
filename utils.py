import re
import sys

class Utils:
    @staticmethod
    def clean_signs(raw_str):
        raw_str = raw_str.replace('-+', '-')
        raw_str = raw_str.replace('++', '+')
        raw_str = raw_str.replace('+-', '-')
        raw_str = raw_str.replace('/+', '/')
        raw_str = raw_str.replace(')C', ')+C')
        raw_str = raw_str.replace('/(+C', '/(C')
        raw_str = raw_str.replace('(+Co', '(Co')
        raw_str = raw_str.replace('*+', '*')
        # raw_str = raw_str.replace('/+', '/') # not used yet
        raw_str = raw_str.replace('+*', '+') # new
        raw_str = raw_str.replace('(*', '(') # new
        return raw_str

    @staticmethod
    def try_int(num):
        if num % 1 == 0:
            return int(f'{num:.{0}f}')
        else:
            return f'{round(num, 4)}'
            # return f'{num:.{4}f}'
            # return num # . maybe 4 round . format



