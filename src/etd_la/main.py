import argparse

from plotting import plot_temperature_distribution
from temperature_solver import solve_temperature_equation


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Solve and plot temperature distribution."
    )
    parser.add_argument("grid_size", type=int, help="Grid size for the simulation")
    parser.add_argument(
        "left_boundary_temp", type=float, help="Temperature at the left boundary"
    )
    parser.add_argument(
        "up_boundary_temp", type=float, help="Temperature at the upper boundary"
    )
    parser.add_argument(
        "right_boundary_temp", type=float, help="Temperature at the right boundary"
    )
    parser.add_argument(
        "down_boundary_temp", type=float, help="Temperature at the lower boundary"
    )

    return parser.parse_args()


def main():
    # Parse command line arguments
    args = parse_arguments()

    # Solve the temperature equation
    temperature_solution = solve_temperature_equation(
        args.grid_size,
        args.left_boundary_temp,
        args.up_boundary_temp,
        args.right_boundary_temp,
        args.down_boundary_temp,
    )

    # Plot the temperature distribution
    plot_temperature_distribution(args.grid_size, temperature_solution)


if __name__ == "__main__":
    main()
