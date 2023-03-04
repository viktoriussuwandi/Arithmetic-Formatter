# --------------------------------------------------------------
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

def printNum(problems, solver=None):

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
    opt_space       = ''.join( [f'{opt_mark}' for i in range(1) ] )
    num_space       = ''.join( [f'{space_mark}' for i in range(space) ] )

     # prepare variables for calculate distance and longest number
    longest_len        = max(len(num1), len(num2))
    numSet_length      = opt_char + 1  + longest_len

    # prepare variable for dot mark
    dot_mark        = '-'
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

def arithmetic_arranger(problems, solver=None):
  err = check_Error(problems)
  if not (err == None): return err
  else: return printNum(problems, solver)