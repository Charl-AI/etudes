import math

import matplotlib.pyplot as plt
import numpy as np

# %% 3.3


def likelihood(x, lam):
    k = 1.0 / (np.exp(-1.0 / lam) - np.exp(-20.0 / lam))
    prob = (k / lam) * np.exp(-x / lam)
    prob = np.where((x >= 1) & (x <= 20), prob, 0.0)
    return prob


def plot_likelihood():
    x = np.linspace(1, 1.5)
    lam = np.linspace(0.1, 1.5)
    X, L = np.meshgrid(x, lam)
    Z = likelihood(X, L)
    fig, ax = plt.subplots()
    c = ax.contourf(X, L, np.log(Z), levels=50, cmap="viridis")  # type: ignore
    # fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    # c = ax.plot_surface(X, L, np.log(Z), cmap="viridis")  # type: ignore
    cbar = fig.colorbar(c, ax=ax)
    cbar.set_label("Log Likelihood")

    ax.set_xlabel("Observation")
    ax.set_ylabel("Decay Constant")

    plt.tight_layout()
    # plt.savefig("chapter_3/assets/particle_surface.pdf")
    plt.show()


# Run the plot
plot_likelihood()
