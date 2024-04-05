def precedence(operator=None):
    priority = {
        '||': 1,
        '&&': 2,
        '|': 3,
        '^': 4,
        '&': 5,
        ('==', '!='): 6,
        ('<', '<=', '>', '>='): 7,
        ('<<', '>>'): 8,
        ('+', '-'): 9,
        ('*', '/', '%'): 10,
        ('++', '--', '!', '*'): 11
    }

    for k, v in priority.items():
        if operator in k:
            return v

    return 0


def infix_to_postfix(expression):
    output_queue = []
    operator_stack = []
    for token in expression:
        if token.isdigit():
            output_queue.append(token)
        elif token in {'||', '&&', '|', '^', '&', '==', '!=', '<', '<=', '>', '>=', '<<', '>>', '+', '-',
                       '*', '/', '%', '++', '--', '!', '*'}:
            while (operator_stack and (precedence(operator_stack[-1]) >= precedence(token)) and not
                    (precedence(operator_stack[-1]) == 11 and precedence(token) == 11)):
                output_queue.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack[-1] != '(':
                output_queue.append(operator_stack.pop())
            operator_stack.pop()

    while operator_stack:
        output_queue.append(operator_stack.pop())

    return output_queue


def test_infix_to_postfix():
    infix_expression = "5 * ( ! 8 ++ - 3 )"
    expected_postfix = [""]
    result = infix_to_postfix(infix_expression.split())
    assert result == expected_postfix, f"Expected: {expected_postfix}, but got: {result}"


if __name__ == "__main__":
    test_infix_to_postfix()
