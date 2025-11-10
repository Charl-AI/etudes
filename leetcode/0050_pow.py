"""Implement pow(x, n), which calculates x raised to the power n."""

# pow(x,n) is x * x * x ... n times. We can recursively apply each
# pairwise operation to do it in log n time.


def my_pow(x: float, n: float) -> float:
    if x == 0:
        return 0
    if n == 0:
        return 1
    inv = n < 0

    curr = 1
    res = x

    def square(x):
        return x * x

    while curr < abs(n) / 2:
        print("s")
        res = square(res)
        curr *= 2

    while curr < abs(n):
        print("t")
        res *= x
        curr += 1
    print(res)
    return res if not inv else 1 / res


assert my_pow(2, 5) == 32
