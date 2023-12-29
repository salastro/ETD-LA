import numpy as np
from matrix_solvers import calculate_inverse_solution


def generate_coefficient_matrix(size, left_temp, up_temp, right_temp, down_temp):
    """Generate the coefficient matrix and right-hand side vector for the temperature problem.

    Parameters:
    - size: Size of the grid
    - left_temp: Temperature at the left boundary
    - up_temp: Temperature at the upper boundary
    - right_temp: Temperature at the right boundary
    - down_temp: Temperature at the lower boundary

    Returns:
    - matrix: Coefficient matrix
    - rhs_vector: Right-hand side vector
    """
    matrix = np.zeros((size * size, size * size))
    rhs_vector = np.zeros(size * size)

    for row in range(size):
        for col in range(size):
            point_num = size * row + col

            # Set coefficients for neighboring points
            if col - 1 >= 0:
                matrix[point_num][point_num - 1] = 1
            else:
                rhs_vector[point_num] += left_temp

            if row - 1 >= 0:
                matrix[point_num][point_num - size] = 1
            else:
                rhs_vector[point_num] += up_temp

            if col + 1 < size:
                matrix[point_num][point_num + 1] = 1
            else:
                rhs_vector[point_num] += right_temp

            if row + 1 < size:
                matrix[point_num][point_num + size] = 1
            else:
                rhs_vector[point_num] += down_temp

    return matrix, rhs_vector


def solve_temperature_equation(size, left_temp, up_temp, right_temp, down_temp):
    """Solve the temperature equation using Jacobi iteration.

    Parameters:
    - size: Size of the grid
    - left_temp: Temperature at the left boundary
    - up_temp: Temperature at the upper boundary
    - right_temp: Temperature at the right boundary
    - down_temp: Temperature at the lower boundary

    Returns:
    - temperature_solution: Solution vector
    """
    coefficient_matrix, rhs_vector = generate_coefficient_matrix(
        size, left_temp, up_temp, right_temp, down_temp
    )

    # Uncomment one of the following lines based on your preferred solver
    # temperature_solution, _ = jacobi_iteration(4 * np.identity(size * size) - coefficient_matrix, rhs_vector)
    temperature_solution = calculate_inverse_solution(
        4 * np.identity(size * size) - coefficient_matrix, rhs_vector
    )

    return temperature_solution
