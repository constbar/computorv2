# # @staticmethod
# def try_int(digit):
#     if digit == 0:
#         return 0
#     if -1 < digit < 1:
#         return digit
#     try:
#         is_int = digit % int(digit) == 0
#     # except OverflowError:
#         # sys.exit('number is too big. number should not be inf')
#     return int(digit) if is_int else digit