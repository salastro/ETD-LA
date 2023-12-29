from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def plot_temperature_distribution_2d(size, temperature):
    """Plot the temperature distribution on a 2D grid.

    Parameters:
    - size: Size of the grid
    - temperature: Solution vector

    Returns:
    - None
    """
    plt.imshow(
        temperature.reshape(size, size), cmap="RdYlBu_r", interpolation="gaussian"
    )
    plt.colorbar()
    plt.contour(temperature.reshape(size, size), cmap="hot")
    plt.title("Temperature Distribution")
    plt.xlabel("Column Index")
    plt.ylabel("Row Index")
    plt.show()


def plot_temperature_distribution_3d(size, temperature):
    """Plot the temperature distribution on a 3D grid.

    Parameters:
    - size: Size of the grid
    - temperature: Solution vector

    Returns:
    - None
    """
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")
    x = np.arange(0, size, 1)
    y = np.arange(0, size, 1)
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, temperature.reshape(size, size), cmap="RdYlBu_r", alpha=0.75)
    ax.contour(X, Y, temperature.reshape(size, size), cmap="hot")
    ax.set_title("Temperature Distribution")
    ax.set_xlabel("Column Index")
    ax.set_ylabel("Row Index")
    ax.set_zlabel("Temperature")
    plt.show()


def plot_temperature_distribution_animation_2d(size, temperature_iterations):
    """Animation of the temperature distribution on a 2D grid."""
    fig = plt.figure()
    ims = []
    for i, temperature in enumerate(temperature_iterations):
        im = plt.imshow(
            temperature.reshape(size, size),
            cmap="RdYlBu_r",
            interpolation="gaussian",
            animated=True,
        )
        ims.append([im])
    plt.colorbar()
    # plt.contour(temperature.reshape(size, size), cmap="hot")
    plt.title("Temperature Distribution Animation")
    plt.xlabel("Column Index")
    plt.ylabel("Row Index")
    ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True)
    plt.show()


if __name__ == "__main__":
    from matrix_solvers import calculate_inverse_solution, jacobi_iteration
    from temperature_solver import generate_coefficient_matrix

    s, l, u, r, d = 10, 2, 2, 0, 1

    A, b = generate_coefficient_matrix(s, l, u, r, d)
    x_jacobi, n, iter = jacobi_iteration(
        4 * np.identity(s * s) - A,
        b,
    )
    # x_inverse = calculate_inverse_solution(
    #     4 * np.identity(s * s) - A,
    #     b,
    # )
    plot_temperature_distribution_animation_2d(s, iter)
