def lu_factorization_nonsquare(A):
    m = len(A)  # Number of rows
    n = len(A[0])  # Number of columns
    min_dim = min(m, n)
    L = [[0.0] * m for _ in range(m)]  # Initialize L as m x m
    U = [[0.0] * n for _ in range(m)]  # Initialize U as m x n
    A_current = [row[:] for row in A]  # Make a copy
    tol = 1e-10  # Tolerance for zero

    for k in range(min_dim):
        if abs(A_current[k][k]) < tol:
            # Zero pivot: set diagonal of L to 1
            L[k][k] = 1.0
        else:
            pivot = A_current[k][k]
            L[k][k] = pivot
            # Scale the pivot row for U
            for j in range(k, n):
                U[k][j] = A_current[k][j] / pivot
            # Eliminate below
            for i in range(k + 1, m):
                L[i][k] = A_current[i][k]
                for j in range(k, n):
                    A_current[i][j] -= L[i][k] * U[k][j]

    # Fill remaining diagonals of L with 1 (identity columns)
    for k in range(min_dim, m):
        L[k][k] = 1.0

    return L, U


def mat_mult(A, B):
    m = len(A)
    p = len(B)
    n = len(B[0]) if p > 0 else 0
    C = [[0.0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C


def print_matrix(matrix, name):
    print(f"{name} =")
    for row in matrix:
        print([f"{x:.1f}" if x != 0 else "0.0" for x in row])
    print()


def main():
    # Example nonsquare matrices
    A_wide = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]]  # 3x4 (wide matrix)

    A_tall = [[-1, 1, 2], [-1, 2, 4], [1, 1, 2], [-2, 4, 8]]  # 4x2 (tall matrix)

    print("LU-Factorization for Wide Matrix (3x4):")
    L_wide, U_wide = lu_factorization_nonsquare(A_wide)
    print_matrix(L_wide, "L")
    print_matrix(U_wide, "U")
    LU_wide = mat_mult(L_wide, U_wide)
    print_matrix(LU_wide, "L * U (Should equal original A)")

    print("\nLU-Factorization for Tall Matrix (4x2):")
    L_tall, U_tall = lu_factorization_nonsquare(A_tall)
    print_matrix(L_tall, "L")
    print_matrix(U_tall, "U")
    LU_tall = mat_mult(L_tall, U_tall)
    print_matrix(LU_tall, "L * U (Should equal original A)")


if __name__ == "__main__":
    main()
