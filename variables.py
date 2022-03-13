# перед этим сделать парсинг по регексу по тому что к какому типу относится 

# сделать основной класс, от которого будут наследоваться
	# str - > raw string
	# обработка 
	# выдать результат
	# сделать перегрузки сложения и удаления
	# стр или репр сделать для рампечатки результата


# класс матрица(интерфейс от которого наследуются)
# класс вектор -"-
# класс полином 
# при инициализции класса давать порядковый номер по индексу

# типа которые надо сделать:
	# Rational numbers		Natural integers
	# Complex numbers (with rational coefﬁcients)
	# Matrices
	# polynomal

	# Polynomial equations of degree less than or equal to 2


# class VariableFactory:
#   @staticmethod
#   def build person:
# if person_type == 'matix':
#   return class matrix
#     def __init__(self):
#         pass


from abc import ABC, abstractmethod


# amaybe it should be called another
class IVariable(ABC):
    # def __init__(self, line):
    # self.line = line
    # print(line)
    # @abstractmethod
    # def prepare(self, data):
    #   """prepare smt"""

    @abstractmethod
    def do(self):
        """do smth"""


class Rational(IVariable):
    def __init__(self, line):
        self.line = line

    def do(self):
        print(self.line)
        # print('i do smth')


print(Parser.read_expression('2 - 2'))
# c = Rational('input line')
# c.do()


# import numpy as np

# class ComplexOrder(Object):
#     def __lt__(self, other):
#         return np.absolute(self) < np.absolute(other)
#     # ... keep want you want (including or not eq and ne)
#     def __ge__(self, other):
#         return np.absolute(self) >= np.absolute(other)

# class OrderedComplex(ComplexOrder, complex):
#     def __init__(self, real, imag = 0):
#         complex.__init__(self, real, imag)

# class NPOrderedComplex64(ComplexOrder, np.complex64):
#     def __init__(self, real = 0):
#         np.complex64.__init__(self, real)