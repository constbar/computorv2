from handler import Handler
hndl = Handler.handle_line

# complex_nums tests
# https://programforyou.ru/calculators/complex-calculator
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

# matrices tests
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**0'
# expression = '[[3,3];[32,1];[2,4]]**0'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**-2'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**-2.1'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**2.2'
# expression = '2**[[3,3,4];[32,1,3];[4,5,6]]'
# Handler.handle_line('lol = [[3,3,4];[32,1,3];[4,5,6]]**-2.2') # ok
# else: print('is it works???') return self.__mul__(other) # ?? try it

# hndl('exp = [[3,3,4];[32,1,3];[4,5,6]]**0')



# mult
# expression = '[[1,2,3]]*[[2];[3];[9]]'

# with pow
# expression = '[[1,2,3];[32,1,2];[4,5,6]]^2+[[1,2,3];[32,1,2];[4,5,6]]'

# inversed
# expression = '[[1,2,3];[32,1,2];[4,5,6]]**-1'
# expression = '[[1,3];[4,6]]**-1'




# funcs
# Handler.handle_line('lol = [[2]]^2') # ok [4]
# Handler.handle_line('lol = [[1.2,3.3]] * [[1];[2];[10]]') # ok [4]
# Handler.handle_line('lol = (20x + 123 + 1x^2)^3')
# Handler.handle_line('lol = (-1x+2)')
# Handler.handle_line('lol = 1x^11')
# Handler.handle_line('lol = (2 + 5x)^2')


# complex
# Handler.handle_line('x=(20)^2 +(-20)^2 + 12^3 + 3i^2') # ok
# Handler.handle_line('x=(3i^4)^2') # good
# Handler.handle_line('x=(3i^2)^1') # good
# Handler.handle_line('x=(3i^3)^4') # good


# Handler.handle_line('x=3i^2 - 123 + 122i') # -126+122i
# Handler.handle_line('x=5.5^2 * 2i') # 60.5i

# matrix
# Handler.handle_line('x=[[1.2, -2, 3]] * 4') # ok [4.8, -8, 12]
# Handler.handle_line('x = [[-11,2,2];[1,2,3]] ** [[-11];[3];[123]]')
# Handler.handle_line('x=[[1];[2];[3]]**[[1.1,2,3]]')
# Handler.handle_line('x=[[1,2,3]]**[[1];[2];[3]]')

# Handler.handle_line('x=[[-11,2,2]] * [[2,10,5]]')
# Handler.handle_line('x=[[-11,2,2]] ** [[2,10,5]]') # good err
# Handler.handle_line('x=[[-11,2,2]]')
# Handler.handle_line('x=[[-11,2,2];[1,2,3]] ** [[2];[3];[1]]')

# Handler.handle_line('x=[[-1,2,2]]**0')
# Handler.handle_line('x=[[0]]**0')
# Handler.handle_line('x=[[]]**0')


# //////// unsorrted -> begin with this


# Handler.handle_line('2x = z?')
# Handler.handle_line('funA(2) + funB(4) = ?')
# Handler.handle_line('c = funca(10)')
# Handler.handle_line('func = 2 * (10 + 2x)^2')
# Handler.handle_line('func(b) = 2 * (10 + 2b)^2')
# Handler.handle_line('try fucn a + fucn B')  #try it

# unc(b)': '1+1b^1'
# Handler.handle_line('a = func(x) + func(x)') # good
# Handler.handle_line('k = func(10) + func(2) + 20') # GOOD
# Handler.handle_line('funcs(x) = 2 / 10 + 1 * x + 2 + 2x^10')
# Handler.handle_line('funcs(x) = 2 * 1 + 1 + 22 + 2x')
# Handler.handle_line('funcs(x) = (2 + x)^5')
# Handler.handle_line('funcs(x) = -(2 + x)^3') # -x^3 - 6 x^2 - 12 x - 8
# Handler.handle_line('funcs(x) = -(2 + 3x)^1') # ok

# Handler.handle_line('funcs(x) = func(10) + 2x')
# Handler.handle_line('funcs(x) = x + 2x')

# Handler.handle_line('c = func(x)')
# Handler.handle_line('c = func(10) + func(10) + 20')
# Handler.handle_line('funC(c) = c')
# Handler.handle_line('c = funC(b) + funC(b)') # bad
# Handler.handle_line('c = funa + funa ')

# Handler.handle_line('funA(10) =? ')
# Handler.handle_line('fund(b) = (1 + +23 + b)^2') # bad
# Handler.handle_line('fun(x) = (x + 2x)^2')
# Handler.handle_line('fun(x) = (x + x)^2')




# Handler.handle_line('lol = 3i + 23')
# Handler.handle_line('lol = [[1,2];[2,3]]^-1')
# Handler.handle_line('x=[[1]]^[[2]]') # good error


# Handler.handle_line('x= (5i)^0') # 1 good
# Handler.handle_line('x=i1')
# Handler.handle_line('x=1x')
# Handler.handle_line('x=((1x + 12))^2') # good err
# Handler.handle_line('x=(1x + 12)^2')
# Handler.handle_line('x=(2 + 5x)^4+200+123+x^2 + (x)^2+1000')
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





# Handler.handle_line('lol = 12i2123') # ok error shiould come
# Handler.handle_line('lol = 12i + 123-123+2+2^2')

# Handler.handle_line('lol = 2123 + 12i')
# Handler.handle_line('lol = (-12.2)^2 + (12.2)^2')
# Handler.handle_line('lol = 21.1i + 123-123i^12 -12^2 - 111^1 * 123^2 / 1^1 - (-12.2)^2 + (12.2)^2') # make formating here 
# Handler.handle_line('lol = 21.1i + (-12)^2')
# Handler.handle_line('lol = [[1.2,2,3]] + [[1.2,2,3]]')
# Handler.handle_line('lol = 20 + 390')
# Handler.handle_line('lol = 20 + 390.2i')
# Handler.handle_line('lol = [[1,2,3.3]]^[[1,2,3.3]]') # chekck it/
# Handler.handle_line('lol = [[1,2];[2,3]] % [12]') # error
# Handler.handle_line('lol = [[1,2];[2,3]] % 2') # came to [[ and .. none..
# Handler.handle_line('lol = 22^[[1,2];[2,3]]')
# 3i902342 error should be error
# > x = 11233x 1212 # error'
