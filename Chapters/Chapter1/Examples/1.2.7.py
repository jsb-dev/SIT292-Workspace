import numpy as np

# Define the coefficient matrix A
A = np.array([[3, 8, -3, -14], [2, 3, -1, -2], [1, -2, 1, 10], [1, 5, -2, -12]])

# Define the constant terms vector b
b = np.array([2, 1, 0, 1])

# Use NumPy's linear algebra solver
try:
    solution = np.linalg.solve(A, b)
    print("Unique solution found:")
    for i, val in enumerate(solution, start=1):
        print(f"x{i} = {val:.4f}")
except np.linalg.LinAlgError as e:
    print("No unique solution:", e)
