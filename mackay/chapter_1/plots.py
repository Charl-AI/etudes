import functools
import math

import matplotlib.pyplot as plt
import numpy as np

# %% 1.3


def binomial_pmf(x, n, f):
    c = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    return c * (f**x) * ((1 - f) ** (n - x))


def p_failure(N, f):
    """Probability of failure of an N-bit repetition code over
    symmetric noise channel with noise f."""
    assert N % 2 != 0, "N must be odd for majority-vote decoding."

    # decoding fails if more than N/2 bits are flipped
    bits_to_fail = range(math.ceil(N / 2), N + 1)
    fn = functools.partial(binomial_pmf, n=N, f=f)
    probs = map(fn, bits_to_fail)
    return sum(probs)


def approx_p_failure(N, f):
    """The approximation we derived analytically."""
    return (4 * f - 4 * (f**2)) ** (N / 2)


def find_n():
    """Computes N such that the probability of failure is <= 10^-15 when
    f = 0.1. We do this by starting with our upper bound of 69, then
    performing a local linear search."""
    res = 69
    fn = functools.partial(p_failure, f=0.1)
    while True:
        p = fn(N=res)
        if p >= 10**-15:
            return res + 2
        res -= 2


print(find_n())

N_vals = np.arange(1, 101, 2)
f_vals = np.linspace(0.01, 0.49, 30)
N_grid, f_grid = np.meshgrid(N_vals, f_vals)

Z_grid = np.zeros_like(N_grid, dtype=float)
for i in range(N_grid.shape[0]):
    for j in range(N_grid.shape[1]):
        Z_grid[i, j] = p_failure(N_grid[i, j], f_grid[i, j])
Z_grid_log = np.log10(np.clip(Z_grid, 1e-30, 1.0))


fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)
cf = ax.contourf(N_grid, f_grid, Z_grid_log, levels=30, cmap="viridis")
cl = ax.contour(
    N_grid, f_grid, Z_grid_log, levels=np.arange(-30, 1, 3), colors="white", alpha=0.5
)
ax.clabel(cl, inline=True, fontsize=10, fmt="%1.0f")
ax.set_xlabel("Repetition Bits (N)")
ax.set_ylabel("Noise Probability (f)")
fig.colorbar(cf, ax=ax, label="Log10(P_failure)")
plt.tight_layout()

# plt.savefig("chapter_1/assets/noise_contour.pdf")
plt.show()
