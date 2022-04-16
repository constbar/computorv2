test_1 = [
    'func(x) = 2*x^5 + 4x^2 - 2x^5 - 5*x + 4',
    'func(x) = 0 + x + 1 + 2x + 123x^2 + 123x',
    'func(x) = x^2 + 2x + 1', 'func(x) = x - 0',
    'func(x) = (x + 2) / 2', 'func(x) = 4x + 1',
    'func(x) = 2 * x + 3', 'func(x) = 2 * x - 5',
    'func(x) = 2 + x - 1', 'func(x) = 1  - x - 1',
    'func(x) = 4x^2 - 5*x^1 + 4x^0', 'func(x) = 0 - x',
    'func(x) = -4x^2 - 5*x^1 + 4x^0', 'func(x) = x + 0']

test_2 = [
    'func(x) = (2.4 + 5.2 * x)^2 + 20', 'func(x) = (-1x + 2)^5',
    'func(x) = (2 + 5x)^2 + 20 - (12)^2', 'func(x) = (-1x + 2)^4',
    'func(x) = 2 / 10 + 1 * x + 2 + 2x^10', 'func(x) = (-1x + 2)^2',
    'func(x) = x + x + 2x + 3x + 10x + 23 + 23 - 10x - 10 * x / 12',
    'func(x) = +2 + 2x + 2 - 3 + 1 - 1 - 2 + 200', 'func(x) = (-1x + 2)',
    'func(x) = +2 + x + 2 - 3 + 1 - 1 - 2 + 200', 'func(x) = (2 + 2)**2',
    'func(x) = (2 - 2x)^3 / 123 / (2 - 2x + 2 + 2)^3', 'func(x) = 1x^11',
    'func(x) = (2 + 5x)^4 + 20 + 123 + 312 + 123 + 3452345 + (123 + 2)^2',
    'func(x) = (2 - 2x)^3 / 123 / (2 - 2x + 2 / 2)^2', 'func(y) = 1+1y^1',
    'func(x) = (2 + 5x)^2 + (4 + 2x)^2 + 20 - 123', 'func(x) = (-1x + 2)^3',
    'func(x) = (2 + 5x)^2 + (2 + 5x)^2 - (2 - 2x)^3', 'func(x) = x^2 * x^2',
    'func(x) = (2 + 5x)^4 + 2 + 123 + x^2 + (x)^2 + 10', 'func(x) = (2 + x)^5',
    'func(x) = 2 * 1 + 1 + 22 + 2x', 'func(x) = (2 + 5x)^2', 'func(x) = -(2 + x)^3',
    'func(x) = 2x + (2 - 1.5x)^9', 'func(x) = (1x + 12)^2', 'func(x) = -(2 + 3x)^1',
    'func(x) = (22 + 5.5x)^3', 'func(x) = 2x + (5x+2)^2', 'func(b) = (1 + 23 + b)^2',
    'func(x) = 20x + 123 + 1x^2', 'func(x) = (20x + 1x)^3', 'func(x) = -(20x + 1x)^3',
    'func(b) = (1b + 23 + b)^2', 'func(x) = 2 * (10 + 2x)^2', 'func(y) = 2 * (10 + 2y)^2',
    'func(x) = (4 + 10x + 101x + 25x^2) / (16 + 8x^1 + 8x^1 + 4x^2) + 20x + 22 + 21 % 200']
	
test_3 = [
    'c = funca(x) + funcb(x)', 'c = funca(x) + funcb(x) + funcc(x) + funcd(x)', 
    'funca(x) = 2x + 12', 'funcb(x) = x + 2', 'funcc(x) = x', 'funcd(x) = 2 + 1', 'f(x)=x',
    'funcd(x) = funca(x) + funca(x)', 'c = funca(x) * funca(x)', 'c = funca(x) * funca(x)',
    'c = funca(12) + funcb(2)', 'c = funca(3) + funcb(4) + funcc(5) + funcd(6) + funcd(7)']

test_errors = [
    'func(x) = 2 + 5x)^2/(4+2x)^2+20x+123+22+21', 'func(x) = -z * 2 + 1', 'x=1x',
    'func(x) = (2 + 5x)^4+20+123+312+123+3452345-(sdfsd)', 'func(x) =2x + () + (5x+2)^2',
    'func(x) = ((2 + 5x)^2', 'func(x) =2x + ((()))(5x+2)^2', 'x = ((1x + 12))^2', '2x = z?']


functions_tests = test_1 + test_2 + test_3 + test_errors
