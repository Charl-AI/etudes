"""Evaluate reverse polish notation.

You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
"""

# stack solution, O(n) time and space


def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),  # int(a/b) rounds towards 0, not same as a//b
    }
    for token in tokens:
        if token in ops.keys():
            rhs = stack.pop()
            lhs = stack.pop()
            result = ops[token](lhs, rhs)
            stack.append(result)
        else:
            stack.append(int(token))

    result = int(stack.pop())
    assert not stack
    return result


assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
assert eval_rpn(["1", "2", "+", "3", "*", "4", "-"]) == 5
assert eval_rpn(["4", "3", "-"]) == 1
assert (
    eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
    == 22
)
