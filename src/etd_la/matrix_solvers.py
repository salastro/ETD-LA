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
    z_iter = np.zeros((max_iter, n))

    for k in range(max_iter):
        x_new = np.zeros_like(x)

        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1 :], x[i + 1 :])
            x_new[i] = (b[i] - sigma) / A[i, i]
            z_iter[k] = x_new

        if np.linalg.norm(x_new - x) < tol:
            return x_new, k + 1, z_iter[:k + 1]

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
    # Example usage:
    A = np.array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]])
    b = np.array([15, 10, 10, 10])

    jacobi_solution, num_iterations, iterations_array = jacobi_iteration(A, b, tol=1e-8)
    inverse_solution = calculate_inverse_solution(A, b)

    print(f"Inverse solution:\t{inverse_solution}")
    print(
        f"Jacobi solution:\t{jacobi_solution}\t(found in {num_iterations} iterations)"
    )
    print(f"Iterations array:\t{iterations_array}")
