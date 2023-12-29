import numpy as np

def calculate_inverse_solution(A, b):
    """
    Calculate the solution vector x of the linear system Ax = b.

    Parameters:
    - A: numpy.ndarray, the coefficient matrix
    - b: numpy.ndarray, the constant vector

    Returns:
    - x: numpy.ndarray, the solution vector
    """
    # Calculate the inverse of A
    A_inverse = np.linalg.inv(A)

    # Calculate the solution vector x
    x = np.dot(A_inverse, b)

    return x


if __name__ == '__main__':
    # Define the coefficient matrix M
    matrix_M = np.array([[0.2, 0.3, 0.5],
                         [0.4, 0.3, 0.3],
                         [0.4, 0.4, 0.2]])

    # Define the constant vector B
    vector_B = np.array([1, 1, 1])

    # Calculate the solution vector m
    solution_vector_m = calculate_inverse_solution(matrix_M, vector_B)

    # Print the solution vector m
    print(solution_vector_m)
