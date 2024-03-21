import heapq


def precedence(operator):
    if operator in {'+', '-'}:
        return 1
    elif operator in {'*', '/', '%'}:
        return 2
    elif operator in {'&', '|', '^'}:
        return 3
    return 0


def infix_to_postfix(expression):
    output_queue = []
    operator_stack = []
    for token in expression:
        if token.isdigit():
            output_queue.append(token)
        elif token in {'+', '-', '*', '/', '&', '|', '^', '%'}:
            while operator_stack and precedence(operator_stack[-1]) >= precedence(token):
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
    infix_expression = "1 - 5 ^ 3 * 2"
    expected_postfix = ["1", "5", "3", "^", "2", "*", "-"]
    result = infix_to_postfix(infix_expression.split())
    assert result == expected_postfix, f"Expected: {expected_postfix}, but got: {result}"


if __name__ == "__main__":
    test_infix_to_postfix()
heapq.heappush()
