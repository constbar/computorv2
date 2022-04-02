from cmd import Cmd
from handler import Handler
from handler import HandlerException
from termcolor import colored


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
        	print(colored(e, 'red'))

        self.HISTORY += line + ' -> ' + 'result\n' 

    do_EOF = do_exit
    help_EOF = help_exit
 
if __name__ == '__main__':
    Comp().cmdloop()
