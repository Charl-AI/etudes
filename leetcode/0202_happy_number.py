"""Happy number.

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

# O(log n), recursive. Not really any tricks here, just send it
# log n comes from the fact that summing the squares of the digits depends on
# the number of digits. This (obviously) increases logarithmically with n.

# Understanding the cycle length is a bit more involved. The key comes from realising
# that the largest sum of squares of digits also grows logarithmically, since going up an order
# of magnitude can, at most, increase the sum of squares by 9^2 = 81. E.g.
# 99 -> 162
# 999 -> 243
# 9999 -> 324
# 99999 -> 405
# Even very large numbers will fall into the range 243, from which point, cycle detection
# takes essentially O(1) time.


def is_happy(n: int) -> bool:
    seen = set()

    def inner(n):
        s = sum(int(d) ** 2 for d in str(n))
        print(s)
        if s == 1:
            return True
        if s in seen:
            return False
        seen.add(s)
        return inner(s)

    return inner(n)


assert is_happy(19)
assert not is_happy(2)
