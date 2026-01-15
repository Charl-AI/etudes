"""We are given an array asteroids of integers representing asteroids in a row.
The indices of the asteroid in the array represent their relative position in space.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
"""


def asteroid_collision(asteroids: list[int]) -> list[int]:
    stack = []
    for a in asteroids:
        while stack and a is not None and a < 0 and stack[-1] > 0:
            diff = a + stack[-1]
            if diff > 0:  # stack[-1] is bigger than a
                a = None
            elif diff < 0:
                stack.pop()
            elif diff == 0:  # stack[-1] is same as a
                a = None
                stack.pop()
            else:
                raise ValueError(f"{diff=} is unknown")

        if a:
            stack.append(a)

    return stack


assert asteroid_collision(asteroids=[5, 10, -5]) == [5, 10]
assert asteroid_collision(asteroids=[8, -8]) == []
assert asteroid_collision(asteroids=[10, 2, -5]) == [10]
assert asteroid_collision(asteroids=[3, 5, -6, 2, -1, 4]) == [-6, 2, 4]
