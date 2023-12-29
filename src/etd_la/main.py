from plotting import plot_temperature_distribution
from temperature_solver import solve_temperature_equation


def main():
    # Problem parameters
    grid_size = 10
    left_boundary_temp = 100
    up_boundary_temp = 0
    right_boundary_temp = 0
    down_boundary_temp = 0

    # Solve the temperature equation
    temperature_solution = solve_temperature_equation(
        grid_size,
        left_boundary_temp,
        up_boundary_temp,
        right_boundary_temp,
        down_boundary_temp,
    )

    # Plot the temperature distribution
    plot_temperature_distribution(grid_size, temperature_solution)


if __name__ == "__main__":
    main()
