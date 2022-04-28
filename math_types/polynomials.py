import re
from math_types.utils import Utils
from math_types.complex_nums import Complex


class PolynomialException(Exception):
    pass


class Polynomial:
    REGEX_AFTER_X = r'([xX][^\^\-\+\=])'
    REGEX_NEG_EXP = r'[xX]\^(?:(?:-\d))'
    REGEX_FLT_EXP = r'[xX]\^(?:(?:\d*\.))'
    REGEX_WRG_INP = r'[^xX\d*\d*\.\d*\^\=\*\-\+]'
    REGEX_HGH_EXP = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^(?:(?:\d{2,})|(?:[3-9]))'

    REGEX_00_POL = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^0'
    REGEX_01_POL = r'[-+]?(?:(?:\d*\.\d*)|(?:\d+))'
    REGEX_1_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX](?:\^1)?'
    REGEX_2_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^2'

    P_ERR_DICT = {
        1: 'wrong syntax on the left side of the polynomial expression',
        2: 'wrong syntax on the right side of the polynomial expression',
        3: 'polynomial expression must have an integer exponent',
        4: 'polynomial expression must have a non-negative exponent',
        5: 'polynomial expression can only have allowed syntax',
    }

    def __init__(self, equation, print_answer=False):
        self.orig = equation
        self.cin = self.cut_input
        self.clean_data = self.sort_variables
        self.check_errors()
        self.eq = PolyCalc(self.clean_data, print_answer)

    def get_clean_data(self):
        return self.clean_data

    @property
    def cut_input(self):
        cut_inp = self.orig
        cut_inp = cut_inp.replace('\t', '').replace(' ', '')
        return cut_inp

    @property
    def sort_variables(self):
        left_part, right_part = self.cin.split('=')
        left_dict = dict()
        right_dict = dict()
        pos_exps = list(set(int(i.split('^')[-1]) for i in
                            re.findall(self.REGEX_HGH_EXP, self.cin)))

        def handle_exps(left_input, right_input):
            for i in pos_exps:
                reg_pos = rf'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^{i}'
                left_dict[i] = re.findall(reg_pos, left_input)
                left_input = re.sub(reg_pos, '', left_input)
                right_dict[i] = re.findall(reg_pos, right_input)
                right_input = re.sub(reg_pos, '', right_input)

            reg_list = [(2, self.REGEX_2_POLY), (0, self.REGEX_00_POL),
                        (1, self.REGEX_1_POLY), (0, self.REGEX_01_POL)]
            for e, r in reg_list:
                if e in left_dict:
                    left_dict[e].extend(re.findall(r, left_input))
                else:
                    left_dict[e] = re.findall(r, left_input)
                if e in right_dict:
                    right_dict[e].extend(re.findall(r, right_input))
                else:
                    right_dict[e] = re.findall(r, right_input)
                left_input = re.sub(r, '', left_input)
                right_input = re.sub(r, '', right_input)
            return left_input, right_input

        left_part, right_part = handle_exps(left_part, right_part)
        if len(left_part + right_part):
            raise PolynomialException(self.P_ERR_DICT[5])

        def clear_vars(l_part: dict, r_part: dict):
            for k in {**l_part, **r_part}.keys():
                l_part[k] = [i.split('^')[0].lower() if '^' in i else i for i in l_part[k]]
                l_part[k] = [i.lower().replace('+', '') for i in l_part[k]]
                l_part[k] = ['1' if i == 'x' else '-1' if i == '-x' else i for i in l_part[k]]
                l_part[k] = sum(float(i.replace('*', '').replace('x', '')) for i in l_part[k])

                r_part[k] = [i.split('^')[0].lower() if '^' in i else i for i in r_part[k]]
                r_part[k] = [i.lower().replace('+', '') for i in r_part[k]]
                r_part[k] = ['1' if i == 'x' else '-1' if i == '-x' else i for i in r_part[k]]
                r_part[k] = sum(float(i.replace('*', '').replace('x', '')) for i in r_part[k])

        try:
            clear_vars(left_dict, right_dict)
        except ValueError:
            raise PolynomialException(self.P_ERR_DICT[5])
        return {key: left_dict.get(key, 0) - right_dict.get(key, 0)
                for key in set(left_dict) | set(right_dict)}

    def check_errors(self):
        if re.findall(self.REGEX_FLT_EXP, self.cin):
            raise PolynomialException(self.P_ERR_DICT[3])
        elif re.findall(self.REGEX_NEG_EXP, self.cin):
            raise PolynomialException(self.P_ERR_DICT[4])
        elif re.findall(self.REGEX_WRG_INP, self.cin):
            raise PolynomialException(self.P_ERR_DICT[5])
        elif re.findall(self.REGEX_AFTER_X, self.cin):
            raise PolynomialException(self.P_ERR_DICT[5])
        elif re.findall(r'\^\D', self.cin):
            raise PolynomialException(self.P_ERR_DICT[5])


class PolyCalc:
    def __init__(self, data: dict, print_answer=False):
        self.data = data
        self.prec = 4
        self.disc = None
        self.results = list()
        self.i_data = self.try_int_data
        self.pol_dgr = self.get_poly_degree
        if print_answer:
            if len(self.data) > 3:
                if self.check_high_poly:
                    self.print_final_result()
            self.make_calculations()
            self.print_final_result()

    @property
    def check_high_poly(self):
        h_vals = list(filter(lambda i: i > 2, self.data.keys()))
        for v in h_vals:
            if self.data[v]:
                return True
        return False

    @property
    def try_int_data(self):
        return {k: Utils.try_int(v) for k, v in self.data.items()}

    @property
    def get_poly_degree(self):
        degree = 0
        for k, v in self.data.items():
            if v and degree < k:
                degree = k
        return degree

    def get_reduced_form(self):
        if all(value == 0 for value in self.data.values()):
            return '0'

        max_len_of_input = max(map(len, map(str, map(int, (self.data.values())))))
        if max_len_of_input > self.prec:
            self.prec = max_len_of_input

        red_form = ''
        for i in self.data.keys():
            if self.data[i]:
                if i == 0:
                    if self.data[i] == 1:
                        red_form += f'1+'
                    elif self.data[i] == -1:
                        red_form += f'-1+'
                    else:
                        red_form += f'{Utils.try_int(self.data[i])}+'
                elif i == 1:
                    if self.data[i] == 1:
                        red_form += f'x+'
                    elif self.data[i] == -1:
                        red_form += f'-x+'
                    else:
                        red_form += f'{Utils.try_int(self.data[i])}x+'
                else:
                    if self.data[i] == 1:
                        red_form += f'x^{i}+'
                    elif self.data[i] == 1:
                        red_form += f'-x^{i}+'
                    else:
                        red_form += f'{Utils.try_int(self.data[i])}x^{i}+'

        red_form = red_form.replace('+-', ' - ').replace('+', ' + ')
        red_form = '- ' + red_form[1:] if red_form[0] == '-' else red_form
        return red_form[:-2].replace(' ', '')

    def print_final_result(self):
        max_len_of_input = max(map(len, map(str, map(int, (self.data.values())))))
        if max_len_of_input > self.prec:
            self.prec = max_len_of_input

        if self.check_high_poly:
            raise PolynomialException(
                'the polynomial degree is strictly greater than 2. could not be solved')
        elif self.pol_dgr == 0:
            raise PolynomialException('no solution')

        if self.disc is not None and self.disc != 0:
            print('there are two solutions:')
        else:
            print('the solution is:')

        if self.pol_dgr == 2 and self.disc < 0:
            for i in self.results:
                print(i)
            return
        for i in self.results:
            if isinstance(Utils.try_int(i), float):
                print(format(i, f'.{self.prec}f').rstrip('0'))
            elif 'e+' in str(i):
                print(i)
            else:
                print(Utils.try_int(i))

    def make_calculations(self):
        if self.pol_dgr == 2:
            self.calc_quadratic_func()
        elif self.pol_dgr == 1:
            self.results.append(-1.0 * self.data[0] / self.data[1])
        else:
            self.print_final_result()

    def calc_quadratic_func(self):
        self.disc = self.data[1]**2 - 4 * self.data[2] * self.data[0]
        if self.disc == 0:
            self.results.append((-1.0 * self.data[1]) / (2 * self.data[2]))
        elif self.disc > 0:
            def find_rational_solutions(sign_type):
                sign = 1.0 if sign_type == '+' else -1.0
                numerator = -1 * self.data[1] + sign * self.disc ** .5
                denominator = 2 * self.data[2]
                return numerator / denominator
            self.results.append(find_rational_solutions('+'))
            self.results.append(find_rational_solutions('-'))
        elif self.disc < 0:
            def find_complex_solutions(sign_type):
                numerator = f'{-1 * self.data[1]} {sign_type} {(-1 * self.disc) ** .5}i'
                denominator = 2 * self.data[2]
                cmplx_vals = re.findall(Complex.REGEX_CMPLX_VLS, numerator)
                exec_line = Complex.apply_complex_classes(cmplx_vals)
                exec_line = f"({Utils.clean_signs(exec_line)})/Complex('{denominator}')"
                return f'{eval(exec_line)}'
            self.results.append(find_complex_solutions('+'))
            self.results.append(find_complex_solutions('-'))
        else:
            self.print_final_result()
