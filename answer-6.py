def is_operator(char):
    return char in ['+', '-', '*', '/']

def postfix_to_prefix(postfix_expr):
    stack = []

    for char in postfix_expr:
        if not is_operator(char):
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix_expr = char + operand1 + operand2
            stack.append(prefix_expr)

    return stack[0]


postfix_expr = input("Enter the postfix expression: ")


prefix_expr = postfix_to_prefix(postfix_expr)


print("Prefix expression:", prefix_expr)
