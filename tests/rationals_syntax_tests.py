import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from handler import Handler
hndl = Handler.handle_line


# rationals tests
# hndl('exp = "" ') # thru running script will be ok 
# hndl('exp = --2')
# hndl('exp = 42.')
# hndl('exp = +4')
# hndl('exp = asd')
# hndl('exp = 5 = ?')
# hndl('func(x) = asd')
# hndl('exp = 22e-+dd5-+')
# hndl('exp = 20 + 390')
# hndl('exp = (-12.2)^2 + (12.2)^2')
	
# hndl('exp = 3 + 5 ?') # strange thing
# hndl('x + 8 = 5')
# hndl('x = 10 / 0')
#     {'input': 'x / 0 = ?',)
#     {'input': 'x / 0 ?', )
#     {'input': 'i = 8', )
# hndl('exp = env') # what is?



# errors
# hndl('exp = x == 5')
# hndl('x == 5')
# hndl('desc')
# hndl('= 2')
# hndl('funX(x = 2')
# hndl('funXx) = 2')

# matrix !!!!!!!!!!!!
# hndl('exp = [[4,4];[2,2]')