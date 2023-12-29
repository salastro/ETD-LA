import matplotlib.pyplot as plt


def plot_temperature_distribution(size, temperature):
    """Plot the temperature distribution on a 2D grid.

    Parameters:
    - size: Size of the grid
    - temperature: Solution vector

    Returns:
    - None
    """
    plt.imshow(temperature.reshape(size, size))
    plt.colorbar()
    plt.title("Temperature Distribution")
    plt.xlabel("Column Index")
    plt.ylabel("Row Index")
    plt.show()
