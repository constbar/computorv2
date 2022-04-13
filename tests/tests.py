from handler import Handler
hndl = Handler.handle_line

# complex_nums tests
# https://programforyou.ru/calculators/complex-calculator
# hndl('exp = (5i)^0')
# hndl('exp = -22i^3') # 22i
# hndl('exp = 12 / (2i^11)') # 6i
# hndl('exp = 12 / (2.0i^11)') # 6i
# hndl('exp = (12.3i)^2') # -151.29
# hndl('exp = 22.5i / 2i') # 11.25
# hndl('exp = 12.3 / 2.0i') # -6.15i
# hndl('exp = 20.3i / 23') # 0.8826i
# hndl('exp = 23 / 20.3i') # -1.133i
# hndl('exp = 22i / 22 / 22i / 22') # 0.0021
# hndl('exp = 20i^19 + 2 * 4i / 2 - 2.5') # -2.5-16i
# hndl('exp = (12 / (2.0i^11)) / (12 + 12i)') # 0.25+0.25i
# hndl('exp = (12.3 / (2.0i^11)) / (-123.343)') # -0.0499i
# hndl('exp = 20i^12 - 12 + 2 * 3i / 22 / 22.5') # 8+0.0121i
# hndl('exp = 123i - 12.3 + 2.55i^12 * 123') # 301.34999+123i
# hndl('exp = 12 / ((2.0i^11) / (12 + 12i))') # -72.2311+72.2311i
# hndl('exp = 122 * 12.3 / 2.0i^11 / -123.343 + 12i^2') # ok -12+6.08303i
# hndl('exp = 123i - 12.3 + 2.0i^14  + 2*12 * 3i / 2.7 / 22.1 * 123') # -14.3+271.4163i
# hndl('exp = 12 / ((2.0i^11) / 12) + 12i') # 83.9424i
# hndl('exp = 12 * 2.0i^11 / 12 + 12i') # 10i
# hndl('exp = 12 + 12i') # 12+12i
# hndl('exp = (123 - 12i) * (12i + 23)') # 2973+1200i
# hndl('exp = 12.5 / (23i^12)') # ok 0.54347
# hndl('exp = (12.5 / (23i^11)) / 111') # 0.0049i
# hndl('exp = (12.5 / (23i^11)) / -111') # -0.00489i
# hndl('exp = i + i * 20 + 123 + i^23 / 123') # 123+20.9919i
# hndl('exp = (20)^2 +(-20)^2 + 12^3 + 3i^2') # ok
# hndl('exp = -(20)^2 +(-20)^2 + 12^3 + 3i^2') # ok

# hndl('exp = 12i + 123-123+2+2^2')
# hndl('exp = 2123 + 12i')
# hndl('exp = 21.1i + 123-123i^12 -12^2 - 111^1 * 123^2 / 1^1 - (-12.2)^2 + (12.2)^2')

# hndl('exp = (3i^4)^1')
# hndl('exp = (3i^4)^2')
# hndl('exp = (3i^4)^3')
# hndl('exp = (3i^4)^4')

# hndl('exp = (3i^1)^1')
# hndl('exp = (3i^2)^2')
# hndl('exp = (3i^3)^3')
# hndl('exp = (3i^4)^4')

# hndl('exp = (4i^1)^4')
# hndl('exp = (3i^2)^3')
# hndl('exp = (2i^3)^2')
# hndl('exp = (1i^4)^1')

# hndl('exp = (4i^1 + 123)^4')
# hndl('exp = (3i^2 - 123)^3')
# hndl('exp = (2i^3 + 123 )^2')
# hndl('exp = (1i^4 - 123)^1')

# hndl('exp = 3i^2 - 123 + 122i') # -126+122i
# hndl('exp = 5.5^2 * 2i') # 60.5i
# hndl('exp = 5 + 3i + 312')
# hndl('exp = -4i^2')

# hndl('exp = 20 + 390.2i')
# hndl('exp = 21.1i + (-12)^2')

# test later
# "input": "a / b = ?", "output": "4 -4i"},
# hndl('exp = c + 5", "output": "10 + 3i"},
# #     {"input": "a * b = ?", "output": "535 + 324i"},
# #     {"input": "a * b = ?", "output": "535 + 324i"},
# hndl('exp = ?", "output": "5 + 3i"},
# #     {"input": "a = ?", "output": "10 + 3i"},
# #     {"input": "a * 5 = ?", "output": "50 + 15i"},
# input": "c + 5 = ?", "output": "10 + 3i"},


# complex_errors
# hndl('exp = 12i2123') # ok error shiould come








# matrices tests
# hndl('exp = [[1,2]]')
# hndl('exp = [[1,2]] + [[3,4]]')
# hndl('exp = [[1,2]] + [[3,4]]')
# hndl('exp = [[1,2]] - [[3,4]]')
# hndl('exp = [[1,2]] * [[3,4]]')
# hndl('exp = [[3,4]] + [[3.2,4]]')
# hndl('exp = [[1,2]] ** [[3];[2]]')

# hndl('exp = [[1,2];[2,3]] ** [[3,2];[2,1]]')
# hndl('exp = [[1,2];[2,3];[3,4.2]]')
# hndl('exp = [[1,2];[2,3];[3,4.2]] ** [[3,2];[2,1]]')
# hndl('exp = [[1,2];[2,3];[3,4.2]] ** [[3,2,3];[2,1,3]]')


# hndl('exp = [[2]]**2')
# hndl('exp = [[0]]**0')
# hndl('lol = [[1,2];[2,3]]^-1')
# hndl('exp = [[-1,2,2]]**0')
# hndl('exp = [[1,3];[4,6]]**-1')
# hndl('exp = [[3,3];[32,1];[2,4]]**0')
# hndl('exp = [[1.2,2,3]] + [[1.2,2,3]]')
# hndl('exp = [[1,2,3];[32,1,2];[4,5,6]]**-1')
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]]**0')
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]]**0')
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]] * 2')
# hndl('exp = 4 * [[3,3,4];[32,1,3];[4,5,6]]')

# hndl('exp = [[1,2,3]] ** [[2];[3];[9]]')
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]]**-1')
# hndl('exp = [[1,2,3];[32,1,2];[4,5,6]]^2+[[1,2,3];[32,1,2];[4,5,6]]')
# hndl('exp = [[-0.1579,0.0351,0.0877];[-3.1579,0.0351,2.0877];[2.7368,-0.0526,-1.6316]] ** -1')
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]] / [[22,3,4];[-1,-2,-3];[22,22,33]]')


# hndl('exp = [[-11,2,2]]')
# hndl('exp = [[1.2, -2, 3]] * 4')
# hndl('exp = [[1,2,3]]**[[1];[2];[3]]')
# hndl('exp = [[-11,2,2]] * [[2,10,5]]')
# hndl('exp = [[1];[2];[3]]**[[1.1,2,3]]')
# hndl('exp = [[-11,2,2];[1,2,3]] ** [[2];[3];[1]]')
# hndl('exp = [[-11,2,2];[1,2,3]] ** [[-11];[3];[123]]')


# matrix errors
# hndl('exp = [[]]**0')
# hndl('exp = [[-11,2,2]] ** [[2,10,5]]') # good err
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]]**-2')
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]]**-2.1')
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]]**-2.2')
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]]**2.2')
# hndl('exp = 2**[[3,3,4];[32,1,3];[4,5,6]]')
# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]] / [[22,3,4];[-1,-2,-3];[22,3,4]]') # zero deter
# hndl('exp = [[1,2,3]] * [[2];[3];[9]]') term to term
# hndl('x=[[1]]^[[2]]') # good error
# hndl('exp = [[1,2,3.3]]^[[1,2,3.3]]') # chekck it/




# functions tests
# hndl('func(x) = 20x + 123 + 1x^2')
# hndl('func(x) = (20x + 1x)^3')
# hndl('func(x) = -(20x + 1x)^3')
# hndl('func(x) = (-1x+2)')
# hndl('func(x) = (-1x+2)^2')
# hndl('func(x) = (-1x+2)^3')
# hndl('func(x) = (-1x+2)^4')
# hndl('func(x) = (-1x+2)^5')
# hndl('func(x) = (2 + 5x)^2')
# hndl('func(x) = 1x^11')
# hndl('func(x) = 2 * (10 + 2x)^2')
# hndl('func(y) = 2 * (10 + 2y)^2')
# hndl('func(y) = 1+1y^1')
# hndl('func(x) = x^2 * x^2')
# hndl('func(x) = (2 + x)^5')
# hndl('func(x) = -(2 + x)^3')
# hndl('func(x) = -(2 + 3x)^1')
# hndl('fund(b) = (1 + 23 + b)^2')
# hndl('fund(b) = (1b + 23 + b)^2')
# hndl('func(x) = 2 * 1 + 1 + 22 + 2x')
# hndl('func(x) = 2 / 10 + 1 * x + 2 + 2x^10')
# hndl('func(x) = (2 + 5x)^2+20-(12)^2')
# hndl('func(x) = (22 + 5.5x)^3')
# hndl('func(x) = (2.4 + 5.2*x)^2+20')
# hndl('func(x) = (2 + 5x)^2+(2 + 5x)^2-(2-2x)^3')
# hndl('func(x) = (2-2x)^3/123/(2-2x+2+2)^3')
# hndl('func(x) = (2-2x)^3/123/(2-2x+2/2)^3')
# hndl('func(x) = (2 + 5x)^2+(4+2x)^2+20-123')
# hndl('func(x) = 2x + (5x+2)^2')
# hndl('func(x) = 2x + (2-1.5x)^9')
# hndl('func(x) = +2+x+2-3+1-1-2+200')
# hndl('func(x) = +2+2x+2-3+1-1-2+200')
# hndl('func(x) = x+x+2x+3x+10x+23+23-10x-10*x/12')

# hndl('func(x) = (2+2)**2')
# hndl('func(x) = (4+10x^1+10x^1+25x^2)/(16+8x^1+8x^1+4x^2)+20x+123+22+21%((4+10x^1+10x^1+25x^2)/(64+32x^1+32x^1+16x^2+32x^1+16x^2+16x^2+8x^3)+20x+123+22+21)')


# print(fa)

# func good errs
# hndl('func(x) =2x + () + (5x+2)^2')
# hndl('func(x) =2x + ((()))(5x+2)^2')
# hndl('func(x) = 2 + 5x)^2/(4+2x)^2+20x+123+22+21')
# hndl('func(x) = ((2 + 5x)^2')

# to test funcs
# Handler.handle_line('a = func(x) + func(x)') # good
# Handler.handle_line('k = func(10) + func(2) + 20') # GOOD
# Handler.handle_line('2x = z?')
# Handler.handle_line('c = funca(10)')
# Handler.handle_line('funA(2) + funB(4) = ?')
# Handler.handle_line('try fucn a + fucn B')  #try it
# Handler.handle_line('funcs(x) = func(10) + 2x')
# Handler.handle_line('funcs(x) = x + 2x')
# Handler.handle_line('c = func(x)')
# Handler.handle_line('c = func(10) + func(10) + 20')
# Handler.handle_line('funC(c) = c')
# Handler.handle_line('c = funC(b) + funC(b)') # bad
# Handler.handle_line('c = funa + funa ')
# Handler.handle_line('funA(10) =? ')



# ////////////////////////
# Handler.handle_line('x=i1')
# Handler.handle_line('x=1x')
# Handler.handle_line('x=((1x + 12))^2') # good err
# Handler.handle_line('x=(1x + 12)^2')
# Handler.handle_line('x=(2 + 5x)^4+200+123+x^2 + (x)^2+1000')
# fa = Function.('(2 + 5x)^4+20+123+312+123+3452345-(sdfsd)')
# fa = Function('(2 + 5x)^4+20+123+312+123+3452345+(123+2)^2')

# rationals
# hndl('exp = 20 + 390')
# hndl('exp = (-12.2)^2 + (12.2)^2')







# tests = [

#     {"input": "desc", "output": "Bad syntax"},
#     {"input": "x == 5", "output": "\033[31m[SyntaxError]\033[0m Invalid input."},
#     {"input": "= 2", "output": "\033[31m[SyntaxError]\033[0m Invalid input."},
#     {"input": "funX(x = 2", "output": "\033[31m[SyntaxError]\033[0m Invalid input."},
#     {"input": "x = [[4,4];[2,2]", "output": "\033[31m[SyntaxError]\033[0m Invalid input."},
#     {"input": "x = --2", "output": "2"},
#     {"input": "3= 4", "output": "\033[31m[SyntaxError]\033[0m Invalid input."},
#     {"input": "x = 22e-+dd5-+", "output": "\033[31m[NameError]\033[0m The variable e is not assigned."},
#     {"input": "x = g", "output": "\033[31m[NameError]\033[0m The variable g is not assigned."},
#     {"input": "x = 5 = ?", "output": "\033[31m[SyntaxError]\033[0m Invalid input."},
#     {"input": "x = 3 + 5 ?", "output": "\033[31m[SyntaxError]\033[0m Invalid input."},
#     {"input": "x + 8 = 5", "output": "-3"},
#     {"input": "x = 10 / 0", "output": "\033[31m[ComputeError]\033[0m Division by 0."},
#     {"input": "x = 5", "output": "5"},
#     {"input": "x / 0 = ?", "output": "\033[31m[ComputeError]\033[0m Division by 0."},
#     {"input": "x / 0 ?", "output": "\033[31m[SyntaxError]\033[0m Invalid input."},
#     {"input": "i = 8", "output": "\033[31m[NameError]\033[0m Can't assign the variable i."},
#     {"input": "env", "output": ""},

#     {"input": "desc", "output": "Assignation et calculs de réels"},
#     {"input": "x = 5", "output": "5"},
#     {"input": "x = ?", "output": "5"},
#     {"input": "x = 5 + 8 * 2", "output": "21"},
#     {"input": "x + 2 = ?", "output": "23"},
#     {"input": "y = 10", "output": "10"},
#     {"input": "y + x = ?", "output": "31"},
#     {"input": "y = y + 2", "output": "12"},
#     {"input": "x = ?", "output": "21"},
#     {"input": "x = y - 13.80", "output": "-1.8"},
#     {"input": "8 + 2 = ?", "output": "10"},
#     {"input": "4^2 = ?", "output": "16"},
#     {"input": "2 * 5^2 = ?", "output": "50"},
#     {"input": "env", "output": ""},

#     {"input": "desc", "output": "Assignation et calculs de fonctions"},
#     {"input": "funX(x) = 5x^2", "output": "5x^2"},
#     {"input": "funX = ?", "output": "5x^2"},
#     {"input": "funX(2) = ?", "output": "20"},
#     {"input": "x = -3", "output": "-3"},
#     {"input": "funX(x) = ?", "output": "45"},
#     {"input": "x = -1.8", "output": "-1.8"},
#     {"input": "funX(x + 2) = ?", "output": "0.2"},
#     {"input": "funX(x) + y = ?", "output": "28.2"},
#     {"input": "funY(b)= b + 6", "output": "b + 6"},
#     {"input": "funX(2) + funY(5) = ?", "output": "31"},
#     {"input": "funA(q) = q + w", "output": "\033[31m[NameError]\033[0m Too many unknown variables."},
#     {"input": "z = funX(x) + 7 - funY(3)", "output": "14.2"},
#     {"input": "z*2 = ?", "output": "28.4"},
#     {"input": "funX(3) = ?", "output": "45"},
#     {"input": "env", "output": ""},

#    

#     {"input": "desc", "output": "Assignation et calcul de complexes"},
#     {"input": "c = 5 + 3i", "output": "5 + 3i"},
#     {"input": "y = -4i", "output": "-4i"},
#     {"input": "c = ?", "output": "5 + 3i"},
#     {"input": "c + 5 = ?", "output": "10 + 3i"},
#     {"input": "a = c + 5", "output": "10 + 3i"},
#     {"input": "a = ?", "output": "10 + 3i"},
#     {"input": "a * 5 = ?", "output": "50 + 15i"},
#     {"input": "b = a * 5 + 8", "output": "58 + 15i"},
#     {"input": "a * b = ?", "output": "535 + 324i"},
#     {"input": "a * b = ?", "output": "535 + 324i"},
#     {"input": "a = 20 - 4i", "output": "20 -4i"},
#     {"input": "b = 3 + 2i", "output": "3 + 2i"},
#     {"input": "a / b = ?", "output": "4 -4i"},

#     {"input": "env", "output": ""},

#     {"input": "desc", "output": "Complex x Matrices"},
#     {"input": " a * z = ?", "output": "[ 20 -4i, 40 -8i ]\n  [ 40 -8i, 60 -12i ]\n  "},

#     {"input": "desc", "output": "Fonctions x Matrices"},
#     {"input": "funX(z)=?", "output": "[ 25, 40 ]\n  [ 40, 65 ]\n  "},
#     {"input": "a = funX(z) - funX(2)", "output": "\033[31m[ComputeError]\033[0m Can't substract a rational " +
#                                                  "to a matrice."},
#     {"input": "a = funX(z) - z", "output": "[ 24, 38 ]\n  [ 38, 62 ]\n  "},
#     {"input": "a = ?", "output": "[ 24, 38 ]\n  [ 38, 62 ]\n  "},
#     {"input": "env", "output": ""},

#     {"input": "desc", "output": "Fonctions x Complexes"},
#     {"input": "funX(c) = ?", "output": "80 + 150i"},
#     {"input": "funA(s) = 5+6-8s^2", "output": "5+6-8s^2"},
#     {"input": "d = 5+3i", "output": "5 + 3i"},
#     {"input": "funA(d) = ?", "output": "-117 -240i"},
#     {"input": "funA(d) = 2*d*i", "output": "2*d*i"},
#     {"input": "funA(2) = ?", "output": "4i"},
#     {"input": "env", "output": ""},

# ]



    # def test_variable(self):
    #     self.do([
    #         ["v = 42.", "42.0"],
    #         ["v = ?",   "42.0"],
    #         ["v",       "42.0"],
    #         ["s = +4",  "4"],
    #     ])


    # def test_functions(self):
    #     self.do([
    #         ["f(x) = 0 + x",                         "x"],
    #         ["f(x) = 0 - x",                         "-x"],
    #         ["f(x) = x + 0",                         "x"],
    #         ["f(x) = x - 0",                         "x"],
    #         ["f(z) = -z * 2 + 1",                    "-z * 2 + 1"],
    #         ["f(x) = 2 * x - 5",                     "2 * x - 5"],
    #         ["f(x) = 4x^2 - 5*x^1 + 4x^0",           "4 * x^2 - 5x + 4"],
    #         ["f(x) = -4x^2 - 5*x^1 + 4x^0",          "-4 * x^2 - 5x + 4"],
    #         ["f(x) = 2*x^5 + 4x^2 - 2x^5 - 5*x + 4", "4 * x^2 - 5x + 4"],
    #         ["f(x) = 4x + 1",                        "4 * x + 1"],
    #         ["f(x) = (x + 2) / 2",                   "(x + 2) / 2"],
    #         ["f(x) = ?",                             "(x + 2) / 2"],
    #         ["f(x)",                                 "(x + 2) / 2"],
    #         ["f(x) = x * x",                         "x * x"],
    #         ["b(x) = 2 * x + 3",                     "2 * x + 3"],
    #         ["c(x) = f + b",                         "(x * x) + (2 * x + 3)"],
    #         ["c(2)",                                 "11"],
    #         ["c(x) = f + b",                         "(x * x) + (2 * x + 3)"],
    #         ["c(2)",                                 "11"],
    #         ["f(x) = x^2 + 2x + 1",                  "x^2 + 2x + 1"],
    #         ["b(x) = x^2 + 2x + 1",                  "x^2 + 2x + 1"],
    #         ["c(x) = f + b",                         "(x ^ 2 + 2 * x + 1) + (x ^ 2 + 2 * x + 1)"],
    #         ["f(x) = x^2 + 3x",                      "x^2 + 3x"],
    #         ["f(x) = x^2 + 1",                       "x^2 + 1"],
    #         ["f(x) = x^2",                           "x^2"],
    #         ["f(x) = x",                             "x"],
    #         ["f(2)",                                 "2"],
    #         ["f(x) = 3 + x - 2",                     "x + 1"],
    #         ["f(x) = 3 + x - 3i",                    "x + (3 - 3i)"],
    #         ["f(x) = -3i + x + 3",                   "x + (3 - 3i)"],
    #         ["f(x) = 3 + x - (4 + 3i)",              "x + (-1 - 3i)"],
    #         ["f(x) = -(4 + 3i) + x + 3",             "x + (-1 - 3i)"],
    #         ["f(x) = 3 + x - [4,5]",                 "x + [ -1 , -2 ]"],
    #         ["f(x) = -[4,5] + x + 3",                "x + [ -1 , -2 ]"],
    #     ])


    #   def test_variable(self):
    #     self.do([
    #         ["a = 1 + 2",                "3"],
    #         ["1 + 2 = ?",                "3"],
    #         ["1 + 2",                    "3"],
    #         ["a = 7 - 2",                "5"],
    #         ["7 - 2 = ?",                "5"],
    #         ["7 - 2",                    "5"],
    #         ["a = 4 / 2",                "2"],
    #         ["4 / 2 = ?",                "2"],
    #         ["4 / 2",                    "2"],
    #         ["a = 5 % 2",                "1"],
    #         ["5 % 2 = ?",                "1"],
    #         ["5 % 2",                    "1"],
    #         ["a = 4 * 2",                "8"],
    #         ["4 * 2 = ?",                "8"],
    #         ["4 * 2",                    "8"],
    #         ["a = 3^2-2",                "7"],
    #         ["3^2-2 = ?",                "7"],
    #         ["3^2-2",                    "7"],
    #         ["a = 3 / 2 + 3",            "4.5"],
    #         ["a = 2 * (4 + 5)",          "18"],
    #         ["a = 2 * (4 + 5) / 9",      "2"],
    #         ["a = (4 + 5) / 2 + 1",      "5.5"],
    #         ["a = (4 + 5) / (2 + 1) + 1","4"],
    #         ["a = 1 + (2 + (3 * 5))",    "18"],
    #         ["a = ((3 * 5) + 2) + 1",    "18"],
    #         ["a = (2 + (3 * 5)) + 1",    "18"],
    #     ])

    # def test_computation(self):
    #     self.do([
    #         ["a = 2",                         "2"],
    #         ["a + 2 = ?",                     "4"],
    #         ["a + 2 ?",                       "4"],
    #         ["a + 2",                         "4"],
    #         ["a * 0",                         "0"],
    #         ["fa(x) = 2 + x",                 "2 + x"],
    #         ["fb(x) = 3 + x",                 "3 + x"],
    #         ["v = 3",                         "3"],
    #         ["fa(2) + v + fb(4) + 2 = ?",     "16"],
    #         ["fa(2 * 3) = ?",                 "8"],
    #         ["fa(2 * 2) + fa(3 * 3) = ?",     "17"],
    #         ["f(x) = 1.2x",                   "1.2 * x"],
    #         ["f(1.2 * 4) = ?",                "5.76"],
    #         ["x = 4",                         "4"],
    #         ["f(x) = ?",                      "4.8"],
    #         ["f(x)",                          "4.8"],
    #         ["4 ^ 3.1",                       "73.51669471981025"],
    #         ["4 ^ -2",                        "0.0625"],
    #         ["4 * -2",                        "-8"],
    #         ["4 / -2",                        "-2"],
    #         ["5 % -2",                        "-1"],
    #         ["5%-2 + 3*-1 - 4/-2 + 2^-2",     "-1.75"],
    #         ["(-15) ^ 2",                     "225"],
    #         ["-15 ^ 2",                       "-225"],
    #     ])
    #     del Data.everything["x"]

    # def test_calculation_priority(self):
    #     self.do([
    #         ["3 * 5 ^ 2",                       "75"],
    #         ["2 - 3 * 5 ^ 2",                   "-73"],
    #         ["2 + 3 * 5 ^ 2 + 4 * 2 ^ 3 - 1",   "108"],
    #         ["2 - (3 * 5) ^ 2",                 "-223"],
    #         ["7 + 0 - 4 - 0 * 8",               "3"],
    #     ])

    #     ])

    # 

    # def test_image_computation(self):
    #     self.do([
    #         ["varA = 2 + 4 *2 - 5 %4 + 2 * (4 + 5)",         "27"],
    #         ["funA(x) = 2 * 4 + x",                          "8 + x"],
    #         ["v = (1 + 2)^2",                                "9"],
    #         ["funB(x) = 4 -5 + (x + 2)^2 - 4",               "(x + 2) ^ 2 - 5"],
    #         ["funB(x) = 4 -5 + (x + 2)^2 - 4 + (x * 2) + 7", "(x + 2) ^ 2 + (x * 2) + 2"],
    #         ["v = 2^2",                                      "4"],
    #     ])

    # def test_polynomials(self):
    #     self.do([
    #         ["f(x) = x^2 + 2x + 1", "x^2 + 2x + 1"],
    #         ["f(x) = ?",            "x^2 + 2x + 1"],
    #         ["f(x) = 2 ?",
    #             "x^2 + 2x - 1 = 0\n  The two R solutions are:\n  -2.414214\n  0.414214"],
    #         ["f(x) = 3x + 2 ?",
    #             "x^2 - x - 1 = 0\n  The two R solutions are:\n  -0.618034\n  1.618034"],

    #         ["b(x) = 3x + 2", "3 * x + 2"],
    #         ["f(x) = b ?",
    #             "x^2 - x - 1 = 0\n  The two R solutions are:\n  -0.618034\n  1.618034"],            
    #         ["f(x) = b(2) ?",
    #             "x^2 + 2x - 7 = 0\n  The two R solutions are:\n  -3.828427\n  1.828427"],
    #         ["f(x) = b(2) + 4x?",
    #             "x^2 - 2x - 7 = 0\n  The two R solutions are:\n  -1.828427\n  3.828427"],
    #         ["f(x) = b(2) + 4*x^2 + f(3)?",
    #             "-3 * x^2 + 2x - 23 = 0\n  The two C solutions are:\n  0.333333 - -2.748737i\n  0.333333 + -2.748737i"],
    #         ["f(x) = b(2) + 4*x^2 - f(3) + 2x - 2?",
    #             "-3 * x^2 + 11 = 0\n  The two R solutions are:\n  1.914854\n  -1.914854"],

    #         ["f(x) = 2x + 2 ?",
    #             "x^2 - 1 = 0\n  The two R solutions are:\n  -1.0\n  1.0"],
    #         ["f(x) = x^2 + 1 ?",   "2x = 0\n  The R solution is:\n  0"],
    #         ["f(2) = ?",           "9"],
    #         ["f(2) = 2 ?",         "7 = 0\n  The eqution has no solution"],
    #         ["f(2) = 9 ?",         "0 = 0\n  Every real number is a solution"],
    #         ["f(x) = -4*x^2 + 3x + 2 ?",
    #             "5 * x^2 - x - 1 = 0\n  The two R solutions are:\n  -0.358258\n  0.558258"],
    #         ["f(x) = x^2 + 2x + 1 ?",
    #             "0 = 0\n  Every real number is a solution"],
    #         ["a + 2 = 2 ?",
    #             "2 = 0\n  The eqution has no solution"],
            
    #         ["f(x) = 3^2 - 2",   "7"],
    #         ["f(x) = 0 ?",       "7 = 0\n  The eqution has no solution"],
    #         ["f(x) = 7 ?",       "0 = 0\n  Every real number is a solution"],
    #     ])

    # def test_polynomials_computorv1_subject_examples(self):
    #     self.do([
    #         ["f(x) = 5 * X^0 + 4 * X^1 - 9.3 * X^2",  "-9.3 * x^2 + 4x + 5"],
    #         ["f(x) = 1 * X^0 ?",
    #             "-9.3 * x^2 + 4x + 4 = 0\n  The two R solutions are:\n  0.905239\n  -0.475131"],

    #         ["f(x) = 5 * X^0 + 4 * X^1", "4x + 5"],
    #         ["f(x) = 4 * X^0 ?",         "4x + 1 = 0\n  The R solution is:\n  -0.25"],

    #         ["f(x) = 8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3",
    #             "-5.6 * x^3 - 6x + 8"],
    #         ["f(x) = 3 * X^0 ?",
    #             "-5.6 * x^3 - 6x + 5 = 0\n  The polynomial degree is strictly greater than 2, I can't solve."],

    #         ["f(x) = 42 * X^0",  "42"],
    #         ["f(x) = 42 * X^0 ?",  "0 = 0\n  Every real number is a solution"],

    #         ["f(x) = 5 + 4 * X + X^2",  "x^2 + 4x + 5"],
    #         ["f(x) = X^2 ?",  "4x + 5 = 0\n  The R solution is:\n  -1.25"],
    #     ])

    # def test_polynomials_computorv1_my_examples(self):
    #     self.do([
    #         ["f(x) = 1 * X^0 + 2 * X^1 + 1 * X^2",  "x^2 + 2x + 1"],
    #         ["f(x) = 0 ?",  "x^2 + 2x + 1 = 0\n  The R solution is:\n  -1.0"],
    #         # greater than 2, but 3 is 0, so can solve
    #         ["f(x) = 8 * X^0 - 6 * X^1 + 1 * X^2 - 0 * X^3",  "x^2 - 6x + 8"],
    #         ["f(x) = 3 * X^0 ?",  "x^2 - 6x + 5 = 0\n  The two R solutions are:\n  1.0\n  5.0"],

    #         ["f(x) = 1 * X^0 + 1 * X^1",    "x + 1"],
    #         ["f(x) = 0 ?",    "x + 1 = 0\n  The R solution is:\n  -1.0"],
    #         # non whole coefficients
    #         ["f(x) = 5.15 * X^0 + 0.4 * X^1 + 9.3 * X^2",    "9.3 * x^2 + 0.4x + 5.15"], 
    #         ["f(x) = 0.155 * X^0 + 0.2 * X^1 + 15.25345 * X^2 ?",
    #             "-5.95345 * x^2 + 0.2x + 4.995 = 0\n  The two R solutions are:\n  0.932925\n  -0.899332"],
    #         # every real number
    #         ["f(x) = 42 * X^0 + 2 * X^1",  "2x + 42"],
    #         ["f(x) = 42 * X^0 + 2 * X^1 ?",  "0 = 0\n  Every real number is a solution"],
    #         # every real number
    #         ["f(x) = 42 * X^0 + 2 * X^1 + 5 * X^2",  "5 * x^2 + 2x + 42"],
    #         ["f(x) = 42 * X^0 + 2 * X^1 + 5 * X^2 ?",
    #             "0 = 0\n  Every real number is a solution"],
    #         # complex solutions
    #         ["f(x) = 1 * X^0 + 2 * X^1 + 5 * X^2",  "5 * x^2 + 2x + 1"],
    #         ["f(x) = 0 ?",
    #             "5 * x^2 + 2x + 1 = 0\n  The two C solutions are:\n  -0.2 - 0.4i\n  -0.2 + 0.4i"],
    #         # complex solutions
    #         ["f(x) = 6.25 * X^0 + 4 * X^1 + 1 * X^2",   "x^2 + 4x + 6.25"],
    #         ["f(x) = 0 ?",
    #             "x^2 + 4x + 6.25 = 0\n  The two C solutions are:\n  -2.0 - 1.5i\n  -2.0 + 1.5i"],
    #         # complex solutions
    #         ["f(x) = 10 * X^0 - 3 * X^1 + 1 * X^2", "x^2 - 3x + 10"],
    #         ["f(x) = 0 ?",
    #             "x^2 - 3x + 10 = 0\n  The two C solutions are:\n  1.5 - 2.783882i\n  1.5 + 2.783882i"],
    #         # no solution
    #         ["f(x) = 42 * X^0",  "42"],
    #         ["f(x) = 24 * X^0 ?",  "18 = 0\n  The eqution has no solution"],
    #         # no solution
    #         ["f(x) = 1 * X^0 + 0 * X^1",    "1"],
    #         ["f(x) = 0 ?",    "1 = 0\n  The eqution has no solution"],
    #         # zero
    #         ["f(x) = 0 * X^0 + 1 * X^1",    "x"],
    #         ["f(x) = 0 ?",    "x = 0\n  The R solution is:\n  0"],
    #         # negative
    #         ["f(x) = -2 * X^0 - 1 * X^1",   "-x - 2"],
    #         ["f(x) = 0 ?",   "-x - 2 = 0\n  The R solution is:\n  -2.0"],
    #     ])


 # def test_variable_name(self):
 #        self.do([
 #            "v8 = 2",
 #            "f(x) = 2 * &",
 #            "f(x) = 2 * z + x - z",
 #            "i = 3",
 #            "f(i) = 4 * i",
 #            "f(x) = 3*x^-1",
 #            "a = 1 + 4(2+3)",
 #            "1 + 4(2+3)",
 #        ])

 #    def test_computation(self):
 #        process_input("a = 2")
 #        process_input("f(x) = 2 + 4x")
 #        self.do([
 #            "a + 2 &", "a + 2 !",
 #            "f(z) = ?",
 #            "d = 10 % 4i", "d = 10i % 3", "d = 10*i % 3", "d = 9*i % 3", 
 #            "10 % 4i", "10i % 3", "10*i % 3", "9*i % 3", 
 #            "4 % 0 = ?", "4 % 0", "4 / 0 = ?", "4 / 0",
 #            "2 ^ (2 + 3i)", "(2 + 3i) ^ (2 + 3i)",
 #            "(2 + 3i) ^ 3.1", "(2 + 3i) ^ -1",
 #            "plot", "plot()", "plot(a)", "plot(b)", "plot(2)", "plot + 2",
 #            "2 + plot", "plot(f) + 2", "2 + plot(f)",
 #            "(2+3i) - [1,2]",
    
 #    def test_syntax(self):
 #        self.do([
 #            "s == 4",
 #            "s = 4x3", "s = x4", "s = 4x",
 #            "s = 4-", "4+", "4*", "4/", "4%", "4^",
 #            "*4", "/4", "%4", "^4", "+4-"
 #            "s = 4--2", "2++3", "3+-4", "4+-5", "4*^5", "4%/5",
 #            "y = 4?", "s = 4,", "s = 4;",
 #            "s = ?4", "s = ,4", "s = ;4",
 #            "s = 4[", "s = 4[]", "s = 4]", "[;]", "[1;]", "[;1]",
 #            "s = [[4,4]",
 #            "s = [4,4]]",
 #            "s = 4(", "s = 4)", "s = 4()", "(.)",
 #            "s = (4", "s = )4", "s = ()4",
 #            "s = ",
 #            " = 4",
 #            "3 = 4",
 #            "s = y",
 #            "s = f(x)",
 #            "f( = 4", "f) = 4", "f(x = 4)", "f(=)",
 #            "m = [[[1,2];[2,1]];[[1,2];[2,1]]]",  "[[1,2];[2,1]];[[1,2];[2,1]]",
 #            "[1,2] + 2 = 2 ?",
 #            "sfhjsre srehj regjl",
 #            "sfhjsre srehji regjl",
 #            "i osdfg gfj",
 #            "fgh sduyre i",
 #            "dshjf i dshjf",
 #        ])
 #        process_input("f(x) = x * x")
 #        process_input("b(x) = 2 * x + 3")
 #        self.do([
 #            "c = f + b",
 #            "c = f(x) + b(x)",
 #            "c(x) = f(x) + b(x)",
 #            "f + b",
 #            "f(x) + b(x)",
 #            ])
 #        process_input("f(x) = x^2 + 2x + 1")
 #        process_input("b(x) = x^2 + 2x + 1")
 #        self.do([
 #            "c = f + b",
 #            "c = f(x) + b(x)",
 #            "c(x) = f(x) + b(x)",
 #            "f + b",
 #            "f(x) + b(x)",
 #            ])


 # def test_rational_numbers(self):
 #        self.do([
 #            ["varA = 2",     "2"],
 #            ["varB = 4.242", "4.242"],
 #            ["varC = -4.3",  "-4.3"],
 #        ])

 #    def test_imaginary_numbers(self):
 #        self.do([
 #            ["varA = 2*i + 3", "3 + 2i"],
 #            ["varB = -4i - 4", "-4 - 4i"],
 #        ])


 #    def test_matricies(self):
 #        self.do([
 #            ["varA = [[2,3];[4,3]]", "[ 2 , 3 ]\n  [ 4 , 3 ]"],
 #            ["varB = [[3,4]]",       "[ 3 , 4 ]"],
 #        ])

 #    def test_functions(self):
 #        self.do([
 #            ["funA(x) = 2*x^5 + 4x^2 - 5*x + 4", "2 * x^5 + 4 * x^2 - 5x + 4"],
 #            ["funB(y) = 43 * y / (4 % 2 * y)",   "43 * y / (0 * y)"],
 #            ["funC(z) = -2 * z - 5",             "-2 * z - 5"],
 #        ])

 #    def test_reassign_variable(self):
 #        self.do([
 #            ["x = 2",        "2"],
 #            ["y = x",        "2"],
 #            ["y = 7",        "7"],
 #            ["y = 2 * i - 4","-4 + 2i"],
 #        ])

 #    def test_reassign_the_result(self):
 #        self.do([
 #            ["varA = 2 + 4 *2 - 5 %4 + 2 * (4 + 5)",     "27"],
 #            ["varB = 2 * varA - 5 %4",                   "53"],
 #            ["funA(x) = varA + varB * 4 - 1 / 2 + x",    "238.5 + x"],
 #            ["varC = 2 * varA - varB",                   "1"],
 #            ["varD = funA(varC)",                        "239.5"],
 #        ])

 #    def test_computation(self):
 #        self.do([
 #            ["a = 2 * 4 + 4",    "12"],
 #            ["a + 2 = ?",        "14"],
 #        ])

 #    def test_image_computation(self):
 #        self.do([
 #            ["funA(x) = 2 * 4 + x",              "8 + x"],
 #            ["funB(x) = 4 -5 + (x + 2)^2 - 4",   "(x + 2) ^ 2 - 5"],
 #            ["funC(x) = 4x + 5 - 2",             "4 * x + 3"],
 #            ["funA(2) + funB(4) = ?",            "41"],
 #            ["funC(3) = ?",                      "15"],
 #        ])

 #    def test_polynomials(self):
 #        self.do([
 #            ["funA(x) = x^2 + 2x + 1",   "x^2 + 2x + 1"],
 #            ["y=0",                      "0"],
 #            ["funA(x) = y ?",            "x^2 + 2x + 1 = 0\n  The R solution is:\n  -1.0"],
 #        ])

 #    def test_syntax(self):
 #        self.do([
 #            ["varA = 2",                                "2"],
 #            ["varB= 2 * (4 + varA + 3)",                "18"],
 #            ["varC =2 * varB",                          "36"],
 #            ["varD    =      2 *(2 + 4 *varC -4 /3)",   "289.3333333333333"],
 #            ["matA = [[1,2];[3,2];[3,4]]",
 #                "[ 1 , 2 ]\n  [ 3 , 2 ]\n  [ 3 , 4 ]"],
 #            ["matB= [[1,2]]",                           "[ 1 , 2 ]"],
 #            ["funA(b) = 2*b+b",                         "2 * b + b"],
 #            ["funB(a)   =2 * a",                        "2 * a"],
 #            ["funC(y) =2* y + 4 -2 * 4+1/3",            "2 * y - 3.6666666666666665"],
 #            ["funD(x)   =   2 *x",                      "2 * x"],
 #        ])