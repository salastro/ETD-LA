# Equilibrium Temperature Distributions using Linear Algebra in Python

## Overview

This Python project focuses on solving equilibrium temperature distributions on a 2D grid using linear algebraic techniques, specifically Jacobi iteration and matrix inversion. The project is structured into several modules to enhance readability, modularity, and ease of understanding.

## Project Structure

### 1. `main.py`

- The main script orchestrates the execution of the project. It sets up problem parameters, such as grid size and boundary temperatures, and then calls the `solve_temperature_equation` function. Finally, it visualizes the temperature distribution using the `plot_temperature_distribution` function.

### 2. `temperature_solver.py`

- Contains the core functions for solving linear systems and calculating solutions:
  - `jacobi_iteration`: Performs Jacobi iteration to solve a linear system.
  - `calculate_inverse_solution`: Computes the solution vector using matrix inversion.
  - Example usage of these functions is demonstrated with a sample linear system.

### 3. `plotting.py`

- Provides a function (`plot_temperature_distribution`) to visualize the temperature distribution on a 2D grid using matplotlib.

### 4. `matrix_solvers.py`

- Includes a function (`calculate_inverse_solution`) that calculates the solution vector using matrix inversion.

### 5. `temperature_solver.py`

- Defines functions to generate the coefficient matrix and right-hand side vector for the temperature problem:
  - `generate_coefficient_matrix`: Creates the coefficient matrix and right-hand side vector.
  - `solve_temperature_equation`: Solves the temperature equation using Jacobi iteration (or matrix inversion).

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/salastro/ETD-LA.git
   cd ETD-LA
   ```

2. Install dependencies:

   ```bash
   poetry install 
   ```

3. Run the `main.py` script:

   ```bash
   poetry run src/etd_la/main.py
   ```

   This will execute the example problem, solve the temperature equation, and display the resulting temperature distribution.

## Dependencies

- NumPy: For numerical operations and linear algebra.
- Matplotlib: For plotting the temperature distribution.

## Contribution Guidelines

If you wish to contribute to this project, please follow the guidelines outlined in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
