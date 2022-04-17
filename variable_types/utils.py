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
        raw_str = raw_str.replace('+*', '+')
        raw_str = raw_str.replace('(*', '(')
        return raw_str

    @staticmethod
    def try_int(num):
        if num % 1 == 0:
            return int(f'{num:.{0}f}')
        else:
            return round(num, 4)

    @staticmethod
    def make_sqrt(num, temp=0.0):
        fin_sqrt = num / 2
        while fin_sqrt != temp:
            temp = fin_sqrt
            fin_sqrt = (num / temp + temp) / 2
        return fin_sqrt

    @staticmethod
    def make_abs(num):
        return num * -1 if num < 0 else num

    @staticmethod
    def make_sin(num):
        r = num * num
        s = 42.0
        i = 10
        while i >= 1:
            s = 4.0 * i - 2.0 + (-r) / s
            i -= 1
        return Utils.try_int(2.0 * num * s / (r + s * s))

    @staticmethod
    def make_cos(num):
        r = num * num
        s = 42.0
        i = 10
        while i >= 1:
            s = 4.0 * i - 2.0 + (-r) / s
            i -= 1
        s = s * s
        return Utils.try_int((s - r) / (s + r))

    @staticmethod
    def make_tan(num):
        return Utils.try_int(Utils.make_sin(num) / Utils.make_cos(num))

    @staticmethod
    def make_atan(num):
        a = 1.0 / Utils.make_sqrt(1.0 + (num * num))
        b = 1.0
        n = 1
        while n <= 11:
            a = (a + b) / 2.0
            b = Utils.make_sqrt(a * b)
            n += 1
        return Utils.try_int(num / (Utils.make_sqrt(1.0 + (num * num)) * a))

    @staticmethod
    def make_radians(n):
        return Utils.try_int(n * (3.1415 / 180))
