#!/usr/bin/python3

from cmd import Cmd
from termcolor import colored
from handler import HandlerException, Handler
from variable_types.matrices import MatrixException
from variable_types.functions import FunctionException
from variable_types.complex_nums import ComplexException
from variable_types.polynomials import PolynomialException


class Comp(Cmd):
    prompt = '> '

    def do_exit(self, param):
        print('program closure')
        return True
    
    def help_exit(self):
        print('exit from the program. ctrl-d or \'exit\'')

    def do_history(self, param):
        if Handler.hist:
            for i in Handler.hist:
                print(i)
        else:
            print('command history with results is empty')

    def help_history(self):
        print('show command history with results')

    def do_variables(self, param):
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
            
        # except TypeError:
        #     print('TypeError')
        # except ValueError:
        #     print('ValueError')
        # except SyntaxError:
        #     print('SyntaxError')
        # add all expcetinon 

    def emptyline(self):
        pass

    do_EOF = do_exit
    help_EOF = help_exit


if __name__ == '__main__':
    Comp().cmdloop()
