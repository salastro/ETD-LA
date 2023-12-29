import argparse

from plotting import plot_temperature_distribution_2d, plot_temperature_distribution_3d
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
    parser.add_argument(
        "graph_type",
        choices=["2d", "3d", "2d-animation", "3d-animation"],
        help="Type of graph to plot",
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
    if args.graph_type == "2d":
        plot_temperature_distribution_2d(args.grid_size, temperature_solution)
    elif args.graph_type == "3d":
        plot_temperature_distribution_3d(args.grid_size, temperature_solution)


if __name__ == "__main__":
    main()
