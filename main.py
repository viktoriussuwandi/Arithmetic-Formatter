# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(['-vv'])

# -----------------------------------------------------------------------------
# MY TESTER CODE
# -----------------------------------------------------------------------------
def check_Error(problems):
  
  import numpy as np
  import string
  input = problems

  output = {"Error": ''}

  num1 = [d.split(' ')[0] for d in input]
  num2 = [d.split(' ')[2] for d in input]
  num  = np.concatenate((num1, num2), axis=0)

  # (max 5 problems) Error: Too many problems
  check_len = len(input) <= 5

  # Error: Operator must be '+' or '-'
  opt = [d.split(' ')[1] for d in input]
  check_opt = not len([d for d in opt if (d != '+' and d != '-')]) > 0

  # Error: Numbers must only contain digits
  single_num = []
  for n in num:
    single_num[:] += n
  check_num = not len([d for d in single_num if d not in string.digits]) > 0

  # Error: Numbers cannot be more than four digits
  check_digits = not len([n for n in num if len(n) > 4]) > 0

  if not check_len: output["Error"] = "Too many problems."
  elif not check_opt: output["Error"] = "Operator must be '+' or '-'."
  elif not check_num: output["Error"] = "Numbers must only contain digits."
  elif not check_digits:
    output["Error"] = "Numbers cannot be more than four digits."

  err = f'Error: { output["Error"] }'
  if output["Error"]: return err

def printNum(problems, solver = False):
  
  # prepare variables for problems input
  input = problems
  
  # prepare variables for each lines
  line1 = ''; line2 = ''; line3 = ''; line4 = ''

  for index, value in enumerate(input) :
    # prepate main variables for numbers and characters of each problem
    p    = value.split(' ')
    num1 = p[0]
    opt  = p[1]
    num2 = p[2]
    num3 = str( int(num1) + int(num2) ) if (opt == '+') else str( int(num1) - int(num2) )

    # prepate additional variables for numbers and characters of each problem
    opt_char        = len(opt)
    space           = 0 if (index == len(input) - 1) else 4
    opt_mark        = ' '
    space_mark      = ' '
    dot_mark        = '-'
    opt_space       = ''.join( [f'{opt_mark}' for i in range(1) ] )
    num_space       = ''.join( [f'{space_mark}' for i in range(space) ] )

     # prepare variables for calculate distance and longest number
    longest_len        = max(len(num1), len(num2))
    numSet_length      = opt_char + 1  + longest_len

    # prepare variable for dot mark
    dots = ''.join( [f'{dot_mark}' for i in range(numSet_length) ] )
    
    #Fill lines for line 1, line 3, and line 4
    line1 += num1.rjust(numSet_length,opt_mark) + num_space
    line3 += dots.rjust(numSet_length,opt_mark)  + num_space 
    line4 += num3.rjust(numSet_length,opt_mark) + num_space

    #Fill line for line 2 (combine with math operator)
    num2_longest       = abs(len(num2) - longest_len)
    num2_longest_space = ''.join( [f'{space_mark}' for i in range(num2_longest) ] )
    # num2Set_length     = numSet_length - 2
    front_line2 = opt + opt_space
    mid_line2   = (num2_longest_space + num2).rjust(longest_len,opt_mark)
    end_line2   = num_space
    line2      += front_line2 + mid_line2 + end_line2
                   

  # Final format
  format1 = f'{line1}\n{line2}\n{line3}\n{line4}'
  format2 = f'{line1}\n{line2}\n{line3}'

  ret = format2 if solver == None else format1
  return ret


# --------------------------------------------------------------

def arithmetic_arranger1(problems, solver=None):
  err = check_Error(problems)
  if not (err == None): return err
  else: return printNum(problems, solver)

def test():
  p1 = [['3801 - 2', '123 + 49']]
  p2 = [['1 + 2', '1 - 9380']]
  p3 = [['3 + 855', '3801 - 2', '45 + 43', '123 + 49']]
  p4 = [['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']]
  p5 = [['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']]
  p6 = [['3 / 855', '3801 - 2', '45 + 43', '123 + 49']]
  p7 = [['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']]
  p8 = [['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']]
  p9 = [['3 + 855', '988 + 40'], True]
  p10 = [['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True]
# --------------------------------------------------------------
  a1 = '  3801      123\n-    2    +  49\n------    -----'
  a2 = '  1         1\n+ 2    - 9380\n---    ------'
  a3 = '    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----'
  a4 = '  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------'
  a5 = 'Error: Too many problems.'
  a6 = "Error: Operator must be '+' or '-'."
  a7 = 'Error: Numbers cannot be more than four digits.'
  a8 = 'Error: Numbers must only contain digits.'
  a9 = '    3      988\n+ 855    +  40\n-----    -----\n  858     1028'
  a10 = '   32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028'

  print('\n---------------------My Self Making Tester Code---------------------\n')
  print(arithmetic_arranger1(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
  checking = [
    {'checking 1': arithmetic_arranger1(p1[0])   == a1},
    {'checking 2': arithmetic_arranger1(p2[0])   == a2},
    {'checking 3': arithmetic_arranger1(p3[0])   == a3},
    {'checking 4': arithmetic_arranger1(p4[0])   == a4},
    {'checking 5': arithmetic_arranger1(p5[0])   == a5},
    {'checking 6': arithmetic_arranger1(p6[0])   == a6},
    {'checking 7': arithmetic_arranger1(p7[0])   == a7},
    {'checking 8': arithmetic_arranger1(p8[0])   == a8},
    {'checking 9': arithmetic_arranger1(p9[0],p9[1])   == a9},
    {'checking 10': arithmetic_arranger1(p10[0],p10[1]) == a10},
  ]

  
  for c in checking:
    print(f'{c}\n')
  
  
  # ----------------------------------------------------------------------


test()
