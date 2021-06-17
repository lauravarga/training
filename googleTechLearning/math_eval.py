# Useful links:
# https://docs.python.org/3/library/dataclasses.html

import re
from dataclasses import dataclass
@dataclass
class Operator:
  priority: int
  executor: callable

operators = { # Map of operators allows quick retrieval
  '+': Operator(1, lambda a, b: a + b),
  '-': Operator(1, lambda a, b: a - b),
  '*': Operator(2, lambda a, b: a * b),
  '/': Operator(2, lambda a, b: float(a) / b),
}

def parse_lexemes(string_input):
  result = []
  re_float = re.compile("""(?x)
   ^
      [+-]?\ *      # first, match an optional sign *and space*
      (             # then match integers or f.p. mantissas:
          \d+       # start out with a ...
          (
              \.\d* # mantissa of the form a.b or a.
          )?        # ? takes care of integers of the form a
         |\.\d+     # mantissa of the form .b
      )
      ([eE][+-]?\d+)?  # finally, optionally match an exponent
   $""")
  args = re.findall( r'\d+\.*\d*', string_input)
  float_args = []
  for arg in args:
      float_args.append(float(arg))
  
  for c in string_input:
    if not c in args:
      if c in operators or c in [')', '(']:
        result.append(c)
      elif not c.isspace():
        print("invalid expression: " + c)
  return result, float_args

def execute_ops(ops, args, condition):
  while ops and condition():
    val2, val1 = args.pop(), args.pop()
    args.append(operators[ops.pop()].executor(val1, val2))

def evaluate_expression(string_input):
  ops, args = parse_lexemes(string_input)
  for l in ops:
    if l == ')':
      execute_ops(ops, args, lambda: ops[-1] != '(')
      ops.pop()
    elif l in operators:
      priority = operators[l].priority
      execute_ops(ops, args, lambda: ops[-1] != '(' and operators[ops[-1]].priority >= priority)

  execute_ops(ops, args, lambda: True)
  return args[-1] if len(args) == 1 else None

# assert evaluate_expression('1 + 2 * (1 + 3)') == 9
print(evaluate_expression('(1 + 3 * (2 + 5)) * 6'))
