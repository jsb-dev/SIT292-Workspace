import sympy as sp

# Part (a)
matrix_a = sp.Matrix(
    [
        [0, -1, 2, 1, 2, 1, -1],
        [0, 1, -2, 2, 7, 2, 4],
        [0, -2, 4, 3, 7, 1, 0],
        [0, 3, -6, 1, 6, 4, 1],
    ]
)

# Part (b)
matrix_b = sp.Matrix(
    [
        [0, -1, 3, 1, 3, 2, 1],
        [0, 2, 6, 1, -5, 0, -1],
        [0, 3, -9, 2, 4, 1, -1],
        [0, 1, -3, -1, 3, 0, 1],
    ]
)

# Compute RREF for both
rref_a, pivots_a = matrix_a.rref()
rref_b, pivots_b = matrix_b.rref()

# Output the results
print("Reduced Row-Echelon Form of Matrix A:")
sp.pprint(rref_a, use_unicode=True)

print("\nReduced Row-Echelon Form of Matrix B:")
sp.pprint(rref_b, use_unicode=True)
