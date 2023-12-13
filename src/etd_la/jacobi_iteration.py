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
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sigma) / A[i, i]

        if np.linalg.norm(x_new - x) < tol:
            return x_new, k + 1

        x = x_new

    raise ValueError("Jacobi iteration did not converge within the specified number of iterations.")

if __name__ == "__main__":
# Example usage:
    A = np.array([[4, -1, 0, 0],
                  [-1, 4, -1, 0],
                  [0, -1, 4, -1],
                  [0, 0, -1, 3]])

    b = np.array([15, 10, 10, 10])

    initial_guess = np.zeros(len(b))
    solution, num_iterations = jacobi_iteration(A, b, x0=initial_guess)

    print("Solution:", solution)
    print("Number of iterations:", num_iterations)
