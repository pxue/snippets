import operator

ARITHMETIC_OPERATORS = {
    '+': operator.add,
    '*': operator.mul
}

def postfix(exp, opr=ARITHMETIC_OPERATORS):
    stack = []
    for val in exp:
        if val in opr:
            f = opr[val]
            stack[-2:] = [f(*stack[-2:])]
        else:
            stack.append(int(val))
    return stack.pop()


print postfix('523*+'), "= 11"
