import numpy as np

def calculate_inverse_solution(matrix_M, vector_B):
    """
    Calculate the solution vector 'm' for the linear system Ax = B,
    where A is the identity matrix minus matrix M.

    Parameters:
    - matrix_M: numpy.ndarray, the coefficient matrix M
    - vector_B: numpy.ndarray, the constant vector B

    Returns:
    - solution_vector_m: numpy.ndarray, the solution vector m
    """
    # Get the shape of matrix_M
    matrix_shape = matrix_M.shape

    # Create the identity matrix with the same size as matrix_M
    identity_matrix = np.identity(int(matrix_shape[0]))

    # Calculate the inverse of (I - M)
    inverse_matrix = np.linalg.inv(identity_matrix - matrix_M)

    # Solve for vector 'm' using the inverse and constant vector B
    solution_vector_m = np.dot(inverse_matrix, vector_B)

    return solution_vector_m
