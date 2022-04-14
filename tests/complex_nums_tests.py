import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from handler import Handler
hndl = Handler.handle_line

# https://programforyou.ru/calculators/complex-calculator

# initial tests

# hndl('exp = -4i^2')
# hndl('exp = (5i)^0')
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
# hndl('exp = 2123 + 12i')
# hndl('exp = 20 + 390.2i')
# hndl('exp = 5 + 3i + 312')
# hndl('exp = -22i^3') # 22i
# hndl('exp = (1i^4 - 123)^1')
# hndl('exp = (4i^1 + 123)^4')
# hndl('exp = (3i^2 - 123)^3')
# hndl('exp = 21.1i + (-12)^2')
# hndl('exp = (2i^3 + 123 )^2')
# hndl('exp = 12 + 12i') # 12+12i
# hndl('exp = 12 / (2i^11)') # 6i
# hndl('exp = 12i + 123-123+2+2^2')
# hndl('exp = 22.5i / 2i') # 11.25
# hndl('exp = 5.5^2 * 2i') # 60.5i
# hndl('exp = 12 / (2.0i^11)') # 6i
# hndl('exp = (12.3i)^2') # -151.29
# hndl('exp = 12.3 / 2.0i') # -6.15i
# hndl('exp = 20.3i / 23') # 0.8826i
# hndl('exp = 23 / 20.3i') # -1.133i

# more difficult tests
# hndl('exp = 12.5 / (23i^12)') # ok 0.54347
# hndl('exp = 22i / 22 / 22i / 22') # 0.0021
# hndl('exp = 3i^2 - 123 + 122i') # -126+122i
# hndl('exp = 12 * 2.0i^11 / 12 + 12i') # 10i
# hndl('exp = (12.5 / (23i^11)) / 111') # 0.0049i
# hndl('exp = (20)^2 +(-20)^2 + 12^3 + 3i^2') # ok
# hndl('exp = -(20)^2 +(-20)^2 + 12^3 + 3i^2') # ok
# hndl('exp = (12.5 / (23i^11)) / -111') # -0.00489i
# hndl('exp = 20i^19 + 2 * 4i / 2 - 2.5') # -2.5-16i
# hndl('exp = (123 - 12i) * (12i + 23)') # 2973+1200i
# hndl('exp = 12 / ((2.0i^11) / 12) + 12i') # 83.9424i
# hndl('exp = (12 / (2.0i^11)) / (12 + 12i)') # 0.25+0.25i
# hndl('exp = (12.3 / (2.0i^11)) / (-123.343)') # -0.0499i
# hndl('exp = i + i * 20 + 123 + i^23 / 123') # 123+20.9919i
# hndl('exp = 20i^12 - 12 + 2 * 3i / 22 / 22.5') # 8+0.0121i
# hndl('exp = 123i - 12.3 + 2.55i^12 * 123') # 301.34999+123i
# hndl('exp = 12 / ((2.0i^11) / (12 + 12i))') # -72.2311+72.2311i
# hndl('exp = 122 * 12.3 / 2.0i^11 / -123.343 + 12i^2') # ok -12+6.08303i
# hndl('exp = 123i - 12.3 + 2.0i^14  + 2*12 * 3i / 2.7 / 22.1 * 123') # -14.3+271.4163i
# hndl('exp = 21.1i + 123-123i^12 -12^2 - 111^1 * 123^2 / 1^1 - (-12.2)^2 + (12.2)^2')




# test later !!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# "input": "a / b = ?", "output": "4 -4i"},
# hndl('exp = c + 5", "output": "10 + 3i"},
# #     {"input": "a * b = ?", "output": "535 + 324i"},
# #     {"input": "a * b = ?", "output": "535 + 324i"},
# hndl('exp = ?", "output": "5 + 3i"},
# #     {"input": "a = ?", "output": "10 + 3i"},
# #     {"input": "a * 5 = ?", "output": "50 + 15i"},
# input": "c + 5 = ?", "output": "10 + 3i"},

# complex_errors
# Handler.handle_line('x=i1')
# hndl('exp = 12i2123') # ok error shiould come
# hndl('exp = 12i21()23') # ok error shiould come
# hndl('exp = 12i21()23(') # ok error shiould come
# hndl('exp = 12[i21()23') # ok error shiould come