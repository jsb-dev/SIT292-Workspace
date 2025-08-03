def lu_factorization_nonsquare(A):
    m = len(A)  # Number of rows
    n = len(A[0])  # Number of columns
    min_dim = min(m, n)
    L = [[0.0] * m for _ in range(m)]  # Initialize L as m x m
    U = [[0.0] * n for _ in range(m)]  # Initialize U as m x n
    A_current = [row[:] for row in A]  # Make a copy
    tol = 1e-10  # Tolerance for zero

    for r in range(min_dim):
        p = r
        while p < n and abs(A_current[r][p]) < tol:
            p += 1
        if p == n:  # No non-zero found in row
            L[r][r] = 1.0
            for j in range(r, n):
                U[r][j] = A_current[r][j]
        else:
            pivot = A_current[r][p]
            L[r][r] = pivot
            # Scale entire row from r to n-1
            for j in range(r, n):
                U[r][j] = A_current[r][j] / pivot
            # Eliminate below
            for i in range(r + 1, m):
                factor = A_current[i][p]
                L[i][r] = factor
                for j in range(r, n):
                    A_current[i][j] -= factor * U[r][j]

    # Handle remaining rows
    for i in range(min_dim, m):
        for j in range(0, n):
            U[i][j] = A_current[i][j]
        L[i][i] = 1.0

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
        s = []
        for x in row:
            if abs(x - round(x)) < 1e-5:
                s.append(str(int(round(x))))
            else:
                s.append(f"{x:.1f}")
        print(s)
    print()


def main():
    A_wide = [[3, 6, 6, 9, -9], [-2, -4, -6, -4, 8], [0, 0, 1, -1, -1]]
    A_tall = [[-1, 1, 2], [-1, 2, 4], [1, 1, 2], [-2, 4, 8]]

    print("LU-Factorization for Wide Matrix (3x4):")
    L_wide, U_wide = lu_factorization_nonsquare(A_wide)
    print_matrix(L_wide, "L")
    print_matrix(U_wide, "U")
    LU_wide = mat_mult(L_wide, U_wide)
    print_matrix(LU_wide, "L * U (Should equal original A)")

    print("\nLU-Factorization for Tall Matrix (4x3):")
    L_tall, U_tall = lu_factorization_nonsquare(A_tall)
    print_matrix(L_tall, "L")
    print_matrix(U_tall, "U")
    LU_tall = mat_mult(L_tall, U_tall)
    print_matrix(LU_tall, "L * U (Should equal original A)")


if __name__ == "__main__":
    main()
