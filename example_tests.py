# COMPLEX


# todo test:
# no kek vars


# COMPLEX
# try with ** in conmplex expression -> error
# Handler.handle_line('kek = (12.3i)**2') # error

# Handler.handle_line('kek = -22i^3') # ok 22i
# Handler.handle_line('kek = 12.3 / 2.0i') # ok -6.15i
# Handler.handle_line('kek = 22.5i / 2i') # ok 11.25
# Handler.handle_line('kek = 20.3i / 2') # ok 10.15i
# Handler.handle_line('kek = 20i^19 + 2 * 4i / 2 - 2.5') # ok -2.5-16i
# Handler.handle_line('kek = 20i^12 - 12 + 2 * 3i / 22 / 22.5') # ok 8+0.01212i
Handler.handle_line('kek = 123i - 12.3 + 2.0i^14  + 2*12 * 3i / 2.7 / 22.1 * 123') # ok -14.3+271.41628i
# Handler.handle_line('kek = 123i - 12.3 + 2.55i^12 * 123') # ok 301.34999+123i
# Handler.handle_line('kek = 22i / 22 / 22i / 22') # ok 0.00206
# Handler.handle_line('kek = 12.3 / 2.0i^11 / -123.343') # ok 0.04986i
# Handler.handle_line('kek = 122 * 12.3 / 2.0i^11 / -123.343 + 12i^2') # ok -12+6.08303i
# Handler.handle_line('kek = 12 / (2.0i^11)') # ok 6i
# Handler.handle_line('kek = 12 / (2i^11)') # 6i
# Handler.handle_line('kek = (12 / (2.0i^11)) / (12 + 12i)') # 0.25+0.25i
# Handler.handle_line('kek = 12 / ((2.0i^11) / (12 + 12i))') # ok -72+72i
# Handler.handle_line('kek = 12 / ((2.0i^11) / 12) + 12i') # ok 84i
# Handler.handle_line('kek = 12 * 2.0i^11 / 12 + 12i') # ok 10i
# Handler.handle_line('kek = 12 + 12i') # ok 12+12i
# Handler.handle_line('kek = (123 - 12i) * (12i + 23)') # ok 2973+1200i
# Handler.handle_line('kek = 12.5 / (23i^12)') # ok 0.54347
# Handler.handle_line('kek = (12.5 / (23i^11)) / 111') # ok 0.00489i
# Handler.handle_line('kek = (12.5 / (23i^11)) / -111') # ok -0.00489i




# MATRIX
# check powers
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**0'
# expression = '[[3,3];[32,1];[2,4]]**0'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**-2'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**-2.1'
# expression = '[[3,3,4];[32,1,3];[4,5,6]]**2.2'
# expression = '2**[[3,3,4];[32,1,3];[4,5,6]]'
# Handler.handle_line('lol = [[3,3,4];[32,1,3];[4,5,6]]**-2.2') # ok
# else: print('is it works???') return self.__mul__(other) # ?? try it




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



