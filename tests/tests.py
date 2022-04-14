
# hndl('func(x) =
# hndl('exp =

# ////////////////////////






    # def test_functions(self):
    #     self.do([
    #         ["f(x) = 0 + x",                         "x"],
    #         ["f(x) = 0 - x",                         "-x"],
    #         ["f(x) = x + 0",                         "x"],
    #         ["f(x) = x - 0",                         "x"],
    #         ["f(z) = -z * 2 + 1",                    "-z * 2 + 1"],
    #         ["f(x) = 2 * x - 5",                     "2 * x - 5"],
    #         ["f(x) = 4x^2 - 5*x^1 + 4x^0",           "4 * x^2 - 5x + 4"],
    #         ["f(x) = -4x^2 - 5*x^1 + 4x^0",          "-4 * x^2 - 5x + 4"],
    #         ["f(x) = 2*x^5 + 4x^2 - 2x^5 - 5*x + 4", "4 * x^2 - 5x + 4"],
    #         ["f(x) = 4x + 1",                        "4 * x + 1"],
    #         ["f(x) = (x + 2) / 2",                   "(x + 2) / 2"],
    #         ["f(x) = ?",                             "(x + 2) / 2"],
    #         ["f(x)",                                 "(x + 2) / 2"],
    #         ["f(x) = x * x",                         "x * x"],
    #         ["b(x) = 2 * x + 3",                     "2 * x + 3"],
    #         ["c(x) = f + b",                         "(x * x) + (2 * x + 3)"],
    #         ["c(2)",                                 "11"],
    #         ["c(x) = f + b",                         "(x * x) + (2 * x + 3)"],
    #         ["c(2)",                                 "11"],
    #         ["f(x) = x^2 + 2x + 1",                  "x^2 + 2x + 1"],
    #         ["b(x) = x^2 + 2x + 1",                  "x^2 + 2x + 1"],
    #         ["c(x) = f + b",                         "(x ^ 2 + 2 * x + 1) + (x ^ 2 + 2 * x + 1)"],
    #         ["f(x) = x^2 + 3x",                      "x^2 + 3x"],
    #         ["f(x) = x^2 + 1",                       "x^2 + 1"],
    #         ["f(x) = x^2",                           "x^2"],
    #         ["f(x) = x",                             "x"],
    #         ["f(2)",                                 "2"],
    #         ["f(x) = 3 + x - 2",                     "x + 1"],
    #         ["f(x) = 3 + x - 3i",                    "x + (3 - 3i)"],
    #         ["f(x) = -3i + x + 3",                   "x + (3 - 3i)"],
    #         ["f(x) = 3 + x - (4 + 3i)",              "x + (-1 - 3i)"],
    #         ["f(x) = -(4 + 3i) + x + 3",             "x + (-1 - 3i)"],
    #         ["f(x) = 3 + x - [4,5]",                 "x + [ -1 , -2 ]"],
    #         ["f(x) = -[4,5] + x + 3",                "x + [ -1 , -2 ]"],
    #     ])


    #   def test_variable(self):
    #     self.do([
    #         ["a = 1 + 2",                "3"],
    #         ["1 + 2 = ?",                "3"],
    #         ["1 + 2",                    "3"],
    #         ["a = 7 - 2",                "5"],
    #         ["7 - 2 = ?",                "5"],
    #         ["7 - 2",                    "5"],
    #         ["a = 4 / 2",                "2"],
    #         ["4 / 2 = ?",                "2"],
    #         ["4 / 2",                    "2"],
    #         ["a = 5 % 2",                "1"],
    #         ["5 % 2 = ?",                "1"],
    #         ["5 % 2",                    "1"],
    #         ["a = 4 * 2",                "8"],
    #         ["4 * 2 = ?",                "8"],
    #         ["4 * 2",                    "8"],
    #         ["a = 3^2-2",                "7"],
    #         ["3^2-2 = ?",                "7"],
    #         ["3^2-2",                    "7"],
    #         ["a = 3 / 2 + 3",            "4.5"],
    #         ["a = 2 * (4 + 5)",          "18"],
    #         ["a = 2 * (4 + 5) / 9",      "2"],
    #         ["a = (4 + 5) / 2 + 1",      "5.5"],
    #         ["a = (4 + 5) / (2 + 1) + 1","4"],
    #         ["a = 1 + (2 + (3 * 5))",    "18"],
    #         ["a = ((3 * 5) + 2) + 1",    "18"],
    #         ["a = (2 + (3 * 5)) + 1",    "18"],
    #     ])

    # def test_computation(self):
    #     self.do([
    #         ["a = 2",                         "2"],
    #         ["a + 2 = ?",                     "4"],
    #         ["a + 2 ?",                       "4"],
    #         ["a + 2",                         "4"],
    #         ["a * 0",                         "0"],
    #         ["fa(x) = 2 + x",                 "2 + x"],
    #         ["fb(x) = 3 + x",                 "3 + x"],
    #         ["v = 3",                         "3"],
    #         ["fa(2) + v + fb(4) + 2 = ?",     "16"],
    #         ["fa(2 * 3) = ?",                 "8"],
    #         ["fa(2 * 2) + fa(3 * 3) = ?",     "17"],
    #         ["f(x) = 1.2x",                   "1.2 * x"],
    #         ["f(1.2 * 4) = ?",                "5.76"],
    #         ["x = 4",                         "4"],
    #         ["f(x) = ?",                      "4.8"],
    #         ["f(x)",                          "4.8"],
    #         ["4 ^ 3.1",                       "73.51669471981025"],
    #         ["4 ^ -2",                        "0.0625"],
    #         ["4 * -2",                        "-8"],
    #         ["4 / -2",                        "-2"],
    #         ["5 % -2",                        "-1"],
    #         ["5%-2 + 3*-1 - 4/-2 + 2^-2",     "-1.75"],
    #         ["(-15) ^ 2",                     "225"],
    #         ["-15 ^ 2",                       "-225"],
    #     ])
    #     del Data.everything["x"]

    # def test_calculation_priority(self):
    #     self.do([
    #         ["3 * 5 ^ 2",                       "75"],
    #         ["2 - 3 * 5 ^ 2",                   "-73"],
    #         ["2 + 3 * 5 ^ 2 + 4 * 2 ^ 3 - 1",   "108"],
    #         ["2 - (3 * 5) ^ 2",                 "-223"],
    #         ["7 + 0 - 4 - 0 * 8",               "3"],
    #     ])

    #     ])

    # 

    # def test_image_computation(self):
    #     self.do([
    #         ["varA = 2 + 4 *2 - 5 %4 + 2 * (4 + 5)",         "27"],
    #         ["funA(x) = 2 * 4 + x",                          "8 + x"],
    #         ["v = (1 + 2)^2",                                "9"],
    #         ["funB(x) = 4 -5 + (x + 2)^2 - 4",               "(x + 2) ^ 2 - 5"],
    #         ["funB(x) = 4 -5 + (x + 2)^2 - 4 + (x * 2) + 7", "(x + 2) ^ 2 + (x * 2) + 2"],
    #         ["v = 2^2",                                      "4"],
    #     ])

    # def test_polynomials(self):
    #     self.do([
    #         ["f(x) = x^2 + 2x + 1", "x^2 + 2x + 1"],
    #         ["f(x) = ?",            "x^2 + 2x + 1"],
    #         ["f(x) = 2 ?",
    #             "x^2 + 2x - 1 = 0\n  The two R solutions are:\n  -2.414214\n  0.414214"],
    #         ["f(x) = 3x + 2 ?",
    #             "x^2 - x - 1 = 0\n  The two R solutions are:\n  -0.618034\n  1.618034"],

    #         ["b(x) = 3x + 2", "3 * x + 2"],
    #         ["f(x) = b ?",
    #             "x^2 - x - 1 = 0\n  The two R solutions are:\n  -0.618034\n  1.618034"],            
    #         ["f(x) = b(2) ?",
    #             "x^2 + 2x - 7 = 0\n  The two R solutions are:\n  -3.828427\n  1.828427"],
    #         ["f(x) = b(2) + 4x?",
    #             "x^2 - 2x - 7 = 0\n  The two R solutions are:\n  -1.828427\n  3.828427"],
    #         ["f(x) = b(2) + 4*x^2 + f(3)?",
    #             "-3 * x^2 + 2x - 23 = 0\n  The two C solutions are:\n  0.333333 - -2.748737i\n  0.333333 + -2.748737i"],
    #         ["f(x) = b(2) + 4*x^2 - f(3) + 2x - 2?",
    #             "-3 * x^2 + 11 = 0\n  The two R solutions are:\n  1.914854\n  -1.914854"],

    #         ["f(x) = 2x + 2 ?",
    #             "x^2 - 1 = 0\n  The two R solutions are:\n  -1.0\n  1.0"],
    #         ["f(x) = x^2 + 1 ?",   "2x = 0\n  The R solution is:\n  0"],
    #         ["f(2) = ?",           "9"],
    #         ["f(2) = 2 ?",         "7 = 0\n  The eqution has no solution"],
    #         ["f(2) = 9 ?",         "0 = 0\n  Every real number is a solution"],
    #         ["f(x) = -4*x^2 + 3x + 2 ?",
    #             "5 * x^2 - x - 1 = 0\n  The two R solutions are:\n  -0.358258\n  0.558258"],
    #         ["f(x) = x^2 + 2x + 1 ?",
    #             "0 = 0\n  Every real number is a solution"],
    #         ["a + 2 = 2 ?",
    #             "2 = 0\n  The eqution has no solution"],
            
    #         ["f(x) = 3^2 - 2",   "7"],
    #         ["f(x) = 0 ?",       "7 = 0\n  The eqution has no solution"],
    #         ["f(x) = 7 ?",       "0 = 0\n  Every real number is a solution"],
    #     ])

    # def test_polynomials_computorv1_subject_examples(self):
    #     self.do([
    #         ["f(x) = 5 * X^0 + 4 * X^1 - 9.3 * X^2",  "-9.3 * x^2 + 4x + 5"],
    #         ["f(x) = 1 * X^0 ?",
    #             "-9.3 * x^2 + 4x + 4 = 0\n  The two R solutions are:\n  0.905239\n  -0.475131"],

    #         ["f(x) = 5 * X^0 + 4 * X^1", "4x + 5"],
    #         ["f(x) = 4 * X^0 ?",         "4x + 1 = 0\n  The R solution is:\n  -0.25"],

    #         ["f(x) = 8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3",
    #             "-5.6 * x^3 - 6x + 8"],
    #         ["f(x) = 3 * X^0 ?",
    #             "-5.6 * x^3 - 6x + 5 = 0\n  The polynomial degree is strictly greater than 2, I can't solve."],

    #         ["f(x) = 42 * X^0",  "42"],
    #         ["f(x) = 42 * X^0 ?",  "0 = 0\n  Every real number is a solution"],

    #         ["f(x) = 5 + 4 * X + X^2",  "x^2 + 4x + 5"],
    #         ["f(x) = X^2 ?",  "4x + 5 = 0\n  The R solution is:\n  -1.25"],
    #     ])

    # def test_polynomials_computorv1_my_examples(self):
    #     self.do([
    #         ["f(x) = 1 * X^0 + 2 * X^1 + 1 * X^2",  "x^2 + 2x + 1"],
    #         ["f(x) = 0 ?",  "x^2 + 2x + 1 = 0\n  The R solution is:\n  -1.0"],
    #         # greater than 2, but 3 is 0, so can solve
    #         ["f(x) = 8 * X^0 - 6 * X^1 + 1 * X^2 - 0 * X^3",  "x^2 - 6x + 8"],
    #         ["f(x) = 3 * X^0 ?",  "x^2 - 6x + 5 = 0\n  The two R solutions are:\n  1.0\n  5.0"],

    #         ["f(x) = 1 * X^0 + 1 * X^1",    "x + 1"],
    #         ["f(x) = 0 ?",    "x + 1 = 0\n  The R solution is:\n  -1.0"],
    #         # non whole coefficients
    #         ["f(x) = 5.15 * X^0 + 0.4 * X^1 + 9.3 * X^2",    "9.3 * x^2 + 0.4x + 5.15"], 
    #         ["f(x) = 0.155 * X^0 + 0.2 * X^1 + 15.25345 * X^2 ?",
    #             "-5.95345 * x^2 + 0.2x + 4.995 = 0\n  The two R solutions are:\n  0.932925\n  -0.899332"],
    #         # every real number
    #         ["f(x) = 42 * X^0 + 2 * X^1",  "2x + 42"],
    #         ["f(x) = 42 * X^0 + 2 * X^1 ?",  "0 = 0\n  Every real number is a solution"],
    #         # every real number
    #         ["f(x) = 42 * X^0 + 2 * X^1 + 5 * X^2",  "5 * x^2 + 2x + 42"],
    #         ["f(x) = 42 * X^0 + 2 * X^1 + 5 * X^2 ?",
    #             "0 = 0\n  Every real number is a solution"],
    #         # complex solutions
    #         ["f(x) = 1 * X^0 + 2 * X^1 + 5 * X^2",  "5 * x^2 + 2x + 1"],
    #         ["f(x) = 0 ?",
    #             "5 * x^2 + 2x + 1 = 0\n  The two C solutions are:\n  -0.2 - 0.4i\n  -0.2 + 0.4i"],
    #         # complex solutions
    #         ["f(x) = 6.25 * X^0 + 4 * X^1 + 1 * X^2",   "x^2 + 4x + 6.25"],
    #         ["f(x) = 0 ?",
    #             "x^2 + 4x + 6.25 = 0\n  The two C solutions are:\n  -2.0 - 1.5i\n  -2.0 + 1.5i"],
    #         # complex solutions
    #         ["f(x) = 10 * X^0 - 3 * X^1 + 1 * X^2", "x^2 - 3x + 10"],
    #         ["f(x) = 0 ?",
    #             "x^2 - 3x + 10 = 0\n  The two C solutions are:\n  1.5 - 2.783882i\n  1.5 + 2.783882i"],
    #         # no solution
    #         ["f(x) = 42 * X^0",  "42"],
    #         ["f(x) = 24 * X^0 ?",  "18 = 0\n  The eqution has no solution"],
    #         # no solution
    #         ["f(x) = 1 * X^0 + 0 * X^1",    "1"],
    #         ["f(x) = 0 ?",    "1 = 0\n  The eqution has no solution"],
    #         # zero
    #         ["f(x) = 0 * X^0 + 1 * X^1",    "x"],
    #         ["f(x) = 0 ?",    "x = 0\n  The R solution is:\n  0"],
    #         # negative
    #         ["f(x) = -2 * X^0 - 1 * X^1",   "-x - 2"],
    #         ["f(x) = 0 ?",   "-x - 2 = 0\n  The R solution is:\n  -2.0"],
    #     ])


 # def test_variable_name(self):
 #        self.do([
 #            "v8 = 2",
 #            "f(x) = 2 * &",
 #            "f(x) = 2 * z + x - z",
 #            "i = 3",
 #            "f(i) = 4 * i",
 #            "f(x) = 3*x^-1",
 #            "a = 1 + 4(2+3)",
 #            "1 + 4(2+3)",
 #        ])

 #    def test_computation(self):
 #        process_input("a = 2")
 #        process_input("f(x) = 2 + 4x")
 #        self.do([
 #            "a + 2 &", "a + 2 !",
 #            "f(z) = ?",
 #            "d = 10 % 4i", "d = 10i % 3", "d = 10*i % 3", "d = 9*i % 3", 
 #            "10 % 4i", "10i % 3", "10*i % 3", "9*i % 3", 
 #            "4 % 0 = ?", "4 % 0", "4 / 0 = ?", "4 / 0",
 #            "2 ^ (2 + 3i)", "(2 + 3i) ^ (2 + 3i)",
 #            "(2 + 3i) ^ 3.1", "(2 + 3i) ^ -1",
 #            "plot", "plot()", "plot(a)", "plot(b)", "plot(2)", "plot + 2",
 #            "2 + plot", "plot(f) + 2", "2 + plot(f)",
 #            "(2+3i) - [1,2]",
    
 #    def test_syntax(self):
 #        self.do([
 #            "s == 4",
 #            "s = 4x3", "s = x4", "s = 4x",
 #            "s = 4-", "4+", "4*", "4/", "4%", "4^",
 #            "*4", "/4", "%4", "^4", "+4-"
 #            "s = 4--2", "2++3", "3+-4", "4+-5", "4*^5", "4%/5",
 #            "y = 4?", "s = 4,", "s = 4;",
 #            "s = ?4", "s = ,4", "s = ;4",
 #            "s = 4[", "s = 4[]", "s = 4]", "[;]", "[1;]", "[;1]",
 #            "s = [[4,4]",
 #            "s = [4,4]]",
 #            "s = 4(", "s = 4)", "s = 4()", "(.)",
 #            "s = (4", "s = )4", "s = ()4",
 #            "s = ",
 #            " = 4",
 #            "3 = 4",
 #            "s = y",
 #            "s = f(x)",
 #            "f( = 4", "f) = 4", "f(x = 4)", "f(=)",
 #            "m = [[[1,2];[2,1]];[[1,2];[2,1]]]",  "[[1,2];[2,1]];[[1,2];[2,1]]",
 #            "[1,2] + 2 = 2 ?",
 #            "sfhjsre srehj regjl",
 #            "sfhjsre srehji regjl",
 #            "i osdfg gfj",
 #            "fgh sduyre i",
 #            "dshjf i dshjf",
 #        ])
 #        process_input("f(x) = x * x")
 #        process_input("b(x) = 2 * x + 3")
 #        self.do([
 #            "c = f + b",
 #            "c = f(x) + b(x)",
 #            "c(x) = f(x) + b(x)",
 #            "f + b",
 #            "f(x) + b(x)",
 #            ])
 #        process_input("f(x) = x^2 + 2x + 1")
 #        process_input("b(x) = x^2 + 2x + 1")
 #        self.do([
 #            "c = f + b",
 #            "c = f(x) + b(x)",
 #            "c(x) = f(x) + b(x)",
 #            "f + b",
 #            "f(x) + b(x)",
 #            ])


 # def test_rational_numbers(self):
 #        self.do([
 #            ["varA = 2",     "2"],
 #            ["varB = 4.242", "4.242"],
 #            ["varC = -4.3",  "-4.3"],
 #        ])

 #    def test_imaginary_numbers(self):
 #        self.do([
 #            ["varA = 2*i + 3", "3 + 2i"],
 #            ["varB = -4i - 4", "-4 - 4i"],
 #        ])


 #    def test_matricies(self):
 #        self.do([
 #            ["varA = [[2,3];[4,3]]", "[ 2 , 3 ]\n  [ 4 , 3 ]"],
 #            ["varB = [[3,4]]",       "[ 3 , 4 ]"],
 #        ])

 #    def test_functions(self):
 #        self.do([
 #            ["funA(x) = 2*x^5 + 4x^2 - 5*x + 4", "2 * x^5 + 4 * x^2 - 5x + 4"],
 #            ["funB(y) = 43 * y / (4 % 2 * y)",   "43 * y / (0 * y)"],
 #            ["funC(z) = -2 * z - 5",             "-2 * z - 5"],
 #        ])

 #    def test_reassign_variable(self):
 #        self.do([
 #            ["x = 2",        "2"],
 #            ["y = x",        "2"],
 #            ["y = 7",        "7"],
 #            ["y = 2 * i - 4","-4 + 2i"],
 #        ])

 #    def test_reassign_the_result(self):
 #        self.do([
 #            ["varA = 2 + 4 *2 - 5 %4 + 2 * (4 + 5)",     "27"],
 #            ["varB = 2 * varA - 5 %4",                   "53"],
 #            ["funA(x) = varA + varB * 4 - 1 / 2 + x",    "238.5 + x"],
 #            ["varC = 2 * varA - varB",                   "1"],
 #            ["varD = funA(varC)",                        "239.5"],
 #        ])

 #    def test_computation(self):
 #        self.do([
 #            ["a = 2 * 4 + 4",    "12"],
 #            ["a + 2 = ?",        "14"],
 #        ])

 #    def test_image_computation(self):
 #        self.do([
 #            ["funA(x) = 2 * 4 + x",              "8 + x"],
 #            ["funB(x) = 4 -5 + (x + 2)^2 - 4",   "(x + 2) ^ 2 - 5"],
 #            ["funC(x) = 4x + 5 - 2",             "4 * x + 3"],
 #            ["funA(2) + funB(4) = ?",            "41"],
 #            ["funC(3) = ?",                      "15"],
 #        ])

 #    def test_polynomials(self):
 #        self.do([
 #            ["funA(x) = x^2 + 2x + 1",   "x^2 + 2x + 1"],
 #            ["y=0",                      "0"],
 #            ["funA(x) = y ?",            "x^2 + 2x + 1 = 0\n  The R solution is:\n  -1.0"],
 #        ])

 #    def test_syntax(self):
 #        self.do([
 #            ["varA = 2",                                "2"],
 #            ["varB= 2 * (4 + varA + 3)",                "18"],
 #            ["varC =2 * varB",                          "36"],
 #            ["varD    =      2 *(2 + 4 *varC -4 /3)",   "289.3333333333333"],
 #            ["matA = [[1,2];[3,2];[3,4]]",
 #                "[ 1 , 2 ]\n  [ 3 , 2 ]\n  [ 3 , 4 ]"],
 #            ["matB= [[1,2]]",                           "[ 1 , 2 ]"],
 #            ["funA(b) = 2*b+b",                         "2 * b + b"],
 #            ["funB(a)   =2 * a",                        "2 * a"],
 #            ["funC(y) =2* y + 4 -2 * 4+1/3",            "2 * y - 3.6666666666666665"],
 #            ["funD(x)   =   2 *x",                      "2 * x"],
 #        ])