#!/usr/bin/python3

from cmd import Cmd
from termcolor import colored

from matrices import MatrixException
from complex_nums import ComplexException
from handler import HandlerException, Handler


class Comp(Cmd):
    INPUT_CONFIG = {
        # 1: ''
    }
    
    HISTORY = ''
    prompt = '> '
    handler = Handler() # not neccesary

    def do_exit(self, param):
        print('program closure')
        return True
    
    def help_exit(self):
        print('exit from the program. ctrl-d or \'exit\'')

    def do_history(self, param):
        if not len(self.HISTORY):
            print('history is empty')
        else:
            print(self.HISTORY[:-1])

    def help_history(self):
        print('show program history')


    def default(self, line):
        # print("Default: {}".format(line))
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
        except TypeError:
            print('asd')
            # FunctionException
        # except SyntaxError as e:
        #     print(e)
        #     print(colored('invalid syntax', 'yellow'))
        # except ZeroDivisionError

        # except:
        #     print('olololo invalid syntax in HAndle')
        line = ''
        self.HISTORY += line + ' -> ' + 'result\n'

    def emptyline(self):
        pass

    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    Comp().cmdloop()
