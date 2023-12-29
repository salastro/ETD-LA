import numpy as np


def jacobi_iteration(A, b, x0=None, tol=1e-6, max_iter=1000):
    """
    Perform Jacobi iteration to solve the linear system Ax = b.

    Parameters:
    - A: Coefficient matrix
    - b: Right-hand side vector
    - x0: Initial guess for the solution
    - tol: Tolerance for convergence
    - max_iter: Maximum number of iterations

    Returns:
    - x: Solution vector
    - num_iter: Number of iterations performed
    """

    n = len(b)
    x = x0 if x0 is not None else np.zeros(n)

    for k in range(max_iter):
        x_new = np.zeros_like(x)

        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1 :], x[i + 1 :])
            x_new[i] = (b[i] - sigma) / A[i, i]

        if np.linalg.norm(x_new - x) < tol:
            return x_new, k + 1

        x = x_new

    raise ValueError(
        "Jacobi iteration did not converge within the specified number of iterations."
    )


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


if __name__ == "__main__":
    # Define the coefficient matrix M
    matrix_M = np.array([[0.2, 0.3, 0.5], [0.4, 0.3, 0.3], [0.4, 0.4, 0.2]])

    # Define the constant vector B
    vector_B = np.array([1, 1, 1])

    # Calculate the solution vector m
    solution_vector_m = calculate_inverse_solution(matrix_M, vector_B)

    # Print the solution vector m
    print(solution_vector_m)


if __name__ == "__main__":
    # Example usage:
    A = np.array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]])

    b = np.array([15, 10, 10, 10])

    initial_guess = np.zeros(len(b))
    solution, num_iterations = jacobi_iteration(A, b, x0=initial_guess)

    print("Solution:", solution)
    print("Number of iterations:", num_iterations)
