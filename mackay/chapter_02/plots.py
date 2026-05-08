import math

import matplotlib.patches as patches

# %% 2.31
import matplotlib.pyplot as plt
import numpy as np


def buffons_coin(b=10, a=3, n_points=1000):
    _, ax = plt.subplots(figsize=(8, 8))
    r = a / 2

    outer = patches.Rectangle((0, 0), b, b, fill=False, edgecolor="black", linewidth=3)
    ax.add_patch(outer)

    inner = patches.Rectangle(
        (r, r),
        b - a,
        b - a,
        fill=True,
        color="lightblue",
        alpha=0.4,
        linestyle="--",
        linewidth=2,
    )
    ax.add_patch(inner)

    x = np.random.rand(n_points) * b
    y = np.random.rand(n_points) * b
    inside_x = (x >= r) & (x <= b - r)
    inside_y = (y >= r) & (y <= b - r)
    is_safe = inside_x & inside_y
    colors = np.where(is_safe, "teal", "coral")

    ax.scatter(
        x, y, c=colors, s=15, alpha=0.7, edgecolor="white", linewidth=0.5, zorder=0
    )

    corners = [(r, r), (b - r, r), (r, b - r), (b - r, b - r)]
    for _, center in enumerate(corners):
        coin = patches.Circle(
            center, r, fill=True, color="gray", alpha=0.3, linewidth=1.5
        )
        ax.add_patch(coin)
        ax.plot(center[0], center[1], marker="+", color="black", markersize=8)

    ax.set_xlim(-1, b + 1)
    ax.set_ylim(-1, b + 1)
    ax.set_aspect("equal")
    ax.set_axis_off()

    plt.tight_layout()
    # plt.savefig("assets/buffons_coin.pdf")
    plt.show()


buffons_coin()

# %% 2.32


def buffons_needle(b=1):
    y = np.linspace(0, b / 2, 400)
    theta = np.linspace(0.01, np.pi / 2, 400)
    Theta, Y = np.meshgrid(theta, y)
    critical_ratio = (2.0 * Y) / (b * np.sin(Theta))
    _, ax = plt.subplots(figsize=(6, 6))

    levels = [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
    cs = ax.contour(
        Theta, Y, critical_ratio, levels=levels, cmap="viridis", linewidths=2
    )
    ax.clabel(cs, inline=True, fontsize=10, fmt="a/b=%.1f")

    ax.set_xlabel(r"$\theta$")
    ax.set_ylabel("y")
    ax.grid(True, linestyle=":", alpha=0.5)

    plt.tight_layout()
    # plt.savefig("assets/buffons_needle.pdf")
    plt.show()


buffons_needle(b=1)


# %% 2.39


def english_pmf(x):
    """Zipf's law of word frequencies in English"""
    if 1 <= x <= 12_367:
        return 0.1 / x
    return 0.0


def english_entropy():
    support = range(1, 12_367 + 1)

    def inner(x):
        p = english_pmf(x)
        return p * -math.log2(p)

    return sum(map(inner, support))


print(english_entropy())
