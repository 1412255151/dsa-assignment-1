def is_operator(char):
    return char in ['+', '-', '*', '/']

def prefix_to_infix(prefix_expr):
    stack = []

    for char in reversed(prefix_expr):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix_expr = operand1 + char + operand2
            stack.append(infix_expr)

    return stack[0]


prefix_expr = input("Enter the prefix expression: ")


infix_expr = prefix_to_infix(prefix_expr)


print("Infix expression:", infix_expr)
