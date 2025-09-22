"""Valid parentheses.

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
"""

# stack based solution: O(n) time, O(n) space


def valid_parentheses(s: str) -> bool:
    brackets = {"(": ")", "{": "}", "[": "]"}

    seen = []
    for char in s:
        if char in brackets.keys():  # opening bracket
            seen.append(char)
        elif char in brackets.values():  # closing bracket
            if seen == [] or brackets[seen.pop()] != char:
                return False
    return seen == []


assert valid_parentheses("()")
assert valid_parentheses("([])")
assert valid_parentheses("()[]{}")
assert not valid_parentheses("(]")
assert not valid_parentheses("([)]")
