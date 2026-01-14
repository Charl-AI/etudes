"""You are keeping the scores for a baseball game with strange rules.
At the beginning of the game, you start with an empty record.

You are given a list of strings operations, where operations[i] is the ith operation you must apply to the record and is one of the following:

An integer x.
Record a new score of x.
'+'.
Record a new score that is the sum of the previous two scores.
'D'.
Record a new score that is the double of the previous score.
'C'.
Invalidate the previous score, removing it from the record.
Return the sum of all the scores on the record after applying all the operations.
"""

# O(n) stack


def calculate_points(operations: list[str]) -> int:
    stack = []

    for op in operations:
        if op == "D":
            assert len(stack) >= 1
            stack.append(stack[-1] * 2)
        elif op == "C":
            _ = stack.pop()
        elif op == "+":
            assert len(stack) >= 2
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(int(op))
    return sum(stack)


assert calculate_points(operations=["5", "2", "C", "D", "+"]) == 30
assert calculate_points(operations=["5", "-2", "4", "C", "D", "9", "+", "+"]) == 27
