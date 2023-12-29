import matplotlib.pyplot as plt


def plot_temperature_distribution(size, temperature):
    """Plot the temperature distribution on a 2D grid.

    Parameters:
    - size: Size of the grid
    - temperature: Solution vector

    Returns:
    - None
    """
    plt.imshow(temperature.reshape(size, size), cmap="RdYlBu_r", interpolation="gaussian")
    plt.colorbar()
    plt.contour(temperature.reshape(size, size), cmap="hot")
    plt.title("Temperature Distribution")
    plt.xlabel("Column Index")
    plt.ylabel("Row Index")
    plt.show()
