#!/usr/bin/python3

from cmd import Cmd
from termcolor import colored
from handler import Handler, HandlerException
from math_types.matrices import MatrixException
from math_types.functions import FunctionException
from math_types.complex_nums import ComplexException
from math_types.polynomials import PolynomialException


class Comp(Cmd):
    prompt = '> '

    def do_exit(self, _):
        print('program closure')
        return True
    
    def help_exit(self):
        print('exit from the program. ctrl-d or \'exit\'')

    def do_history(self, _):
        if Handler.hist:
            for i in Handler.hist:
                print(i)
        else:
            print('command history with results is empty')

    def help_history(self):
        print('show command history with results')

    def do_variables(self, _):
        if Handler.vals.keys():
            for k, v in Handler.vals.items():
                print(k, ': ', v, sep='')
        else:
            print('list of saved variables is empty')

    def help_variables(self):
        print('display a list of saved variables and their values')

    def default(self, line):
        try:
            Handler.handle_line(line)
        except MatrixException as exc:
            print(colored(str(exc), 'cyan'))
        except HandlerException as exc:
            print(colored(str(exc), 'cyan'))
        except ComplexException as exc:
            print(colored(str(exc), 'cyan'))
        except FunctionException as exc:
            print(colored(str(exc), 'cyan'))
        except PolynomialException as exc:
            print(colored(str(exc), 'cyan'))
        except ZeroDivisionError:
            print(colored('division by zero is not allowed', 'cyan'))
        except AttributeError:
            pass
        except Exception:
            print(colored('invalid syntax', 'cyan'))

    def emptyline(self):
        pass

    do_EOF = do_exit
    help_EOF = help_exit


if __name__ == '__main__':
    Comp().cmdloop()
