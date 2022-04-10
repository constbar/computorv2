#!/usr/bin/python3

from cmd import Cmd
from termcolor import colored

from matrices import MatrixException
from complex_nums import ComplexException
from handler import HandlerException, Handler

# need i colored print here?


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
        except HandlerException as e:
            print(colored(e, 'cyan'))
        except ComplexException as e:
            print(colored(e, 'cyan'))

        except AttributeError:
            # print('attrib error')
            pass
        # add here syntax err

        # except ComplexException as e: # need i?
        #     print(e)
        except MatrixException as e: # for static exceptions
            print(colored(e, 'yellow'))
        # except TypeError:
            # print('asd')
            # FunctionException
        # except SyntaxError as e:
        #     print(e)
        #     print(colored('invalid syntax', 'yellow'))
        # except ZeroDivisionError

        # except:
        #     print('olololo invalid syntax in HAndle')
        line = '' # need i?

    def emptyline(self):
        pass

    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    Comp().cmdloop()
