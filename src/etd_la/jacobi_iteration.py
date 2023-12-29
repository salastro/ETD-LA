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
    - iterations: a matrix with the temperatures at every iteration
    """
    
    iterations = np.array([])
    n = len(b)
    x = x0 if x0 is not None else np.zeros(n)

    for k in range(max_iter):
        x_new = np.zeros_like(x)

        for i in range(n):
            sigma = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i + 1 :], x[i + 1 :])
            x_new[i] = (b[i] - sigma) / A[i, i]
        
        iterations = np.append(iterations, x_new)
        
        if np.linalg.norm(x_new - x) < tol:
            return x_new, k + 1, iterations
        
        x = x_new

    raise ValueError(
        "Jacobi iteration did not converge within the specified number of iterations."
    )


def mesh(iterations, k):

    import matplotlib.pyplot as plt
    import numpy as np

    from matplotlib import cm
    from matplotlib.ticker import LinearLocator

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

    X = np.arange(0, k, 1)
    Y = np.arange(1, iterations.shape[0], 1) 
    X, Y = np.meshgrid(X, Y)
    Z = iterations

    # Plot the surface.
    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)

    # Customize the z axis.
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    # A StrMethodFormatter is used automatically
    ax.zaxis.set_major_formatter('{x:.02f}')

    # Add a color bar which maps values to colors.
    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()




if __name__ == "__main__":
    # Example usage:
    A = np.array([[4, -1, 0, 0], [-1, 4, -1, 0], [0, -1, 4, -1], [0, 0, -1, 3]])

    b = np.array([15, 10, 10, 10])

    initial_guess = np.zeros(len(b))
    solution, num_iterations, iterations = jacobi_iteration(A, b, x0=initial_guess)
    mesh(iterations, num_iterations) 
    print("Solution:", solution)
    print("Number of iterations:", num_iterations)
