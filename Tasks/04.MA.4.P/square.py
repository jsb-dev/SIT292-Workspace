def lu_factorization(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    A_current = [row[:] for row in A]  # Make a copy
    tol = 1e-10  # Tolerance for zero

    for k in range(n):
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
            for i in range(k + 1, n):
                L[i][k] = A_current[i][k]
                for j in range(k, n):
                    A_current[i][j] -= L[i][k] * U[k][j]
    return L, U


def mat_mult(A, B):
    n = len(A)
    p = len(B)
    m = len(B[0])
    C = [[0.0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(p):
                C[i][j] += A[i][k] * B[k][j]
    return C


def main():
    A = [[-3, -6, -9, 6], [1, 3, 0, -5], [3, 9, 0, -15], [2, 2, 12, 2]]

    L, U = lu_factorization(A)

    # Print results
    print("L =")
    for row in L:
        print([f"{x:.1f}" if x != 0 else "0.0" for x in row])

    print("\nU =")
    for row in U:
        print([f"{x:.1f}" if x != 0 else "0.0" for x in row])

    # Verify L * U = A
    LU = mat_mult(L, U)
    print("\nL * U =")
    for row in LU:
        print([f"{x:.1f}" if x != 0 else "0.0" for x in row])


if __name__ == "__main__":
    main()
