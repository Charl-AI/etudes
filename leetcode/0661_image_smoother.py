# this is just a O(n*m) two loops problem. It can't get any
# faster than this because you have to write every element to the
# output anyway. The LeetCode editorial suggests space-saving tricks
# to avoid allocating an output array, but these are just cheaply exploiting
# the discrepancy between the problem input size being 8-bit and python ints being unbounded.

# NB, in O(n*m) you can also compute the integral image (summed area table)
# which can be used to compute any size convolution kernel as long as it has
# fixed weights. However that's overkill here

import itertools


def image_smoother(img: list[list[int]]) -> list[list[int]]:
    rows, cols = len(img), len(img[0])
    res = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            neighbours = []
            for a, b in itertools.product((-1, 0, 1), repeat=2):
                x, y = i + a, j + b
                if 0 <= x < rows and 0 <= y < cols:
                    neighbours.append(img[i + a][j + b])

            res[i][j] = int(sum(neighbours) / len(neighbours))
    return res


assert image_smoother(img=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]) == [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
assert image_smoother(img=[[100, 200, 100], [200, 50, 200], [100, 200, 100]]) == [
    [137, 141, 137],
    [141, 138, 141],
    [137, 141, 137],
]
