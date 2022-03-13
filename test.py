# d = dict('exit': 'call_func (sys.exit()) or qquit')


# history_list[] - make it reverse and add values to the begining maybe make pickle
# {a: {'index': 0, 'znachenie': 'kek'}}
# welcome prompt '>'
# argparse :show all types what can i calc 

# d[1] = 123
# print(d)
# del d[1]
# print(d)



# from cmd import Cmd
# from factory import Parser


# class Comp(Cmd):
#     INPUT_CONFIG = {
#         # 1: ''
#     }
    
#     HISTORY = ''
#     prompt = '> '
#     # parser = Parser()


#     def do_exit(self, param):
#         print('program closure')
#         return True
    
#     def help_exit(self):
#         print('exit from the program. ctrl-d or \'exit\'')

#     def do_history(self, param):
#         if not len(self.HISTORY):
#             print('history is empty')
#         else:
#             print(self.HISTORY[:-1])

#     def help_history(self):
#         print('show program history')
 
#     def default(self, line):
#         # print("Default: {}".format(line))
#         Parser.read_expression(line)
        
#         self.HISTORY += line + ' -> ' + 'result\n' 

#     do_EOF = do_exit
#     help_EOF = help_exit
 
# if __name__ == '__main__':
#     Comp().cmdloop()
