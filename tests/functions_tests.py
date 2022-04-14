import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from handler import Handler
hndl = Handler.handle_line


# functions tests

# hndl('func(x) = 1x^11')
# hndl('func(y) = 1+1y^1')
# hndl('func(x) = (-1x+2)')
# hndl('func(x) = (2+2)**2')
# hndl('func(x) = x^2 * x^2')
# hndl('func(x) = (2 + x)^5')
# hndl('func(x) = (-1x+2)^2')
# hndl('func(x) = (-1x+2)^3')
# hndl('func(x) = (-1x+2)^4')
# hndl('func(x) = (-1x+2)^5')
# hndl('func(x) = (2 + 5x)^2')
# hndl('func(x) = -(2 + x)^3')
# hndl('func(x) = (1x + 12)^2')
# hndl('func(x) = -(2 + 3x)^1')
# hndl('func(x) = (20x + 1x)^3')
# hndl('func(x) = -(20x + 1x)^3')
# hndl('func(x) = (22 + 5.5x)^3')
# hndl('func(x) = 2x + (5x+2)^2')
# hndl('fund(b) = (1 + 23 + b)^2')
# hndl('fund(b) = (1b + 23 + b)^2')
# hndl('func(x) = 2 * (10 + 2x)^2')
# hndl('func(y) = 2 * (10 + 2y)^2')
# hndl('func(x) = 2x + (2-1.5x)^9')
# hndl('func(x) = 20x + 123 + 1x^2')
# hndl('func(x) = (2.4 + 5.2*x)^2+20')
# hndl('func(x) = +2+x+2-3+1-1-2+200')
# hndl('func(x) = +2+2x+2-3+1-1-2+200')
# hndl('func(x) = 2 * 1 + 1 + 22 + 2x')
# hndl('func(x) = (2 + 5x)^2+20-(12)^2')
# hndl('func(x) = (2-2x)^3/123/(2-2x+2/2)^3')
# hndl('func(x) = (2-2x)^3/123/(2-2x+2+2)^3')
# hndl('func(x) = 2 / 10 + 1 * x + 2 + 2x^10')
# hndl('func(x) = (2 + 5x)^2+(4+2x)^2+20-123')
# hndl('func(x) = (2 + 5x)^2+(2 + 5x)^2-(2-2x)^3')
# hndl('func(x) = x+x+2x+3x+10x+23+23-10x-10*x/12')
# hndl('func(x) = (2 + 5x)^4+200+123+x^2 + (x)^2+1000')
# hndl('func(x) = (2 + 5x)^4+20+123+312+123+3452345+(123+2)^2')
# hndl('func(x) = (4+10x^1+10x^1+25x^2)/(16+8x^1+8x^1+4x^2)+20x+123+22+21%((4+10x^1+10x^1+25x^2)/(64+32x^1+32x^1+16x^2+32x^1+16x^2+16x^2+8x^3)+20x+123+22+21)')


# hndl('func(x) = 1 + x - 1') # wth
# hndl('func(x) = 1  - x - 1') # wth
# hndl('func(x) = 0 - x') # wth
# hndl('func(x) = 0 + x + 1 + 2x + 123x^2 + 123x')
# hndl(func(x) = x + 0",                         "x"],
# hndl(func(x) = x - 0",                         "x"],
# hndl(func(x) = -z * 2 + 1",                    "-z * 2 + 1"],
# hndl(func(x) = 2 * x - 5",                     "2 * x - 5"],
# hndl(func(x) = 4x^2 - 5*x^1 + 4x^0",           "4 * x^2 - 5x + 4"],
# hndl(func(x) = -4x^2 - 5*x^1 + 4x^0",          "-4 * x^2 - 5x + 4"],
# "f(x) = 2*x^5 + 4x^2 - 2x^5 - 5*x + 4", "4 * x^2 - 5x + 4"],
# "f(x) = 4x + 1",                        "4 * x + 1"],
# "f(x) = (x + 2) / 2",                   "(x + 2) / 2"],
# "f(x) = ?",                             "(x + 2) / 2"],
# hndl('func(x)",                                 "(x + 2) / 2"],
# hndl('func(x) = x * x",                         "x * x"],
# hndl('func(x) = 2 * x + 3",                     "2 * x + 3"],
# hndl('func(x) = f + b",                         "(x * x) + (2 * x + 3)"],
# hndl('func(2)",                                 "11"],
# hndl('func(x) = f + b",                         "(x * x) + (2 * x + 3)"],
# hndl('func(2)",                                 "11"],
# hndl('func(x) = x^2 + 2x + 1",                  "x^2 + 2x + 1"],
# hndl('func(x) = x^2 + 2x + 1",                  "x^2 + 2x + 1"],
# hndl('func(x) = f + b",                         "(x ^ 2 + 2 * x + 1) + (x ^ 2 + 2 * x + 1)"],
# hndl('func(x) = x^2 + 3x",                      "x^2 + 3x"],
# hndl('func(x) = x^2 + 1",                       "x^2 + 1"],
# hndl('func(x)(x) = x^2",                           "x^2"],
# hndl('func(x)(x) = x",                             "x"],
# hndl('func(x)(2)",                                 "2"],
# hndl('func(x)(x) = 3 + x - 2",                     "x + 1"],
# hndl('func(x)(x) = 3 + x - 3i",                    "x + (3 - 3i)"],
# hndl('func(x)(x) = -3i + x + 3",                   "x + (3 - 3i)"],
# hndl('func(x)(x) = 3 + x - (4 + 3i)",              "x + (-1 - 3i)"],
# hndl('func(x)(x) = -(4 + 3i) + x + 3",             "x + (-1 - 3i)"],
#     ["f(x) = 3 + x - [4,5]",                 "x + [ -1 , -2 ]"],
#     ["f(x) = -[4,5] + x + 3",                "x + [ -1 , -2 ]"],


# func good errs
# hndl('func(x) =2x + () + (5x+2)^2')
# hndl('func(x) =2x + ((()))(5x+2)^2')
# hndl('func(x) = 2 + 5x)^2/(4+2x)^2+20x+123+22+21')
# hndl('func(x) = ((2 + 5x)^2')
# Handler.handle_line('x=((1x + 12))^2') # good err
# Handler.handle_line('x=1x')
# hndl('func(x) = (2 + 5x)^4+20+123+312+123+3452345-(sdfsd)')



# to test funcs later
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
# Handler.handle_line('funA(10) =? ')
# Handler.handle_line('c = funa + funa ')
