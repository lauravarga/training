from dataclasses import dataclass
import re
import math

@dataclass
class Operator:
  priority: int
  executor: callable

operators = { # Map of operators allows quick retrieval
  '+': Operator(1, lambda a, b: a + b),
  '-': Operator(1, lambda a, b: a - b),
  '*': Operator(2, lambda a, b: a * b),
  '/': Operator(2, lambda a, b: float(a) / b),
  '^': Operator(3, lambda a, b: a ** b),
  'sqrt': Operator(3, lambda a: math.sqrt(a)),
  'abs': Operator(3, lambda a: abs(a)),
  'unary-': Operator(3, lambda a: float(-a)),
  'unary+': Operator(3, lambda a: float(a)),
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

  while string_input != '':
    m = re.match( r'\d+\.*\d*', string_input)
    if m:
        arg = m.group(0)
        result.append(float(arg))
        string_input = string_input[len(arg):]
    else:
        c = string_input[0]
        if not c.isspace():
            if c in operators or c in [')', '(']:
                result.append(c)
                string_input = string_input[1:]
            else:
                if string_input.startswith('sqrt'):
                    result.append('sqrt')
                    string_input = string_input[4:]
                if string_input.startswith('abs'):
                    result.append('abs')
                    string_input = string_input[3:]
        else:
          string_input = string_input[1:]
  return result

def execute_ops(ops, args, condition):
  while ops and condition():
    op = ops.pop()
    if op == 'abs' or op == 'sqrt':
        val = args.pop()
        args.append(operators[op].executor(val))
    elif (op == '+' or op == '-') and len(args) == 1:
        val = args.pop()
        unary_op = 'unary' + op
        args.append(operators[unary_op].executor(val))
    else:
        val2, val1 = args.pop(), args.pop()
        args.append(operators[op].executor(val1, val2))

def evaluate_expression(string_input):
  lexemes = parse_lexemes(string_input)
  ops = []
  args = []
  for l in lexemes:
    if isinstance(l, float):
      args.append(l)
    elif l == '(':
      ops.append(l)
    elif l == ')':
      execute_ops(ops, args, lambda: ops[-1] != '(')
      ops.pop()
    elif l in operators:
      priority = operators[l].priority
      execute_ops(ops, args, lambda: ops[-1] != '(' and operators[ops[-1]].priority >= priority)
      ops.append(l)
  execute_ops(ops, args, lambda: True)
  return args[-1] if len(args) == 1 else None

print("{:.2f}".format(evaluate_expression(sys.stdin.readline())))

# assert evaluate_expression('1 + 2 * (1 + 3)') == 9
# print("{:.2f}".format(evaluate_expression('abs(-1) + (1^6 + 3 * (2 + 5)) * 6 + sqrt(4)')))