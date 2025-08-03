def lu_factorization_nonsquare(A, log_operations=True):
    m = len(A)  # Number of rows
    n = len(A[0])  # Number of columns
    min_dim = min(m, n)
    L = [[0.0] * m for _ in range(m)]  # Initialize L as m x m
    U = [[0.0] * n for _ in range(m)]  # Initialize U as m x n
    A_current = [row[:] for row in A]  # Make a copy
    tol = 1e-10  # Tolerance for zero

    if log_operations:
        print("Starting LU Factorization:")
        print(f"Initial Matrix A ({m}x{n}):")
        print_matrix(A_current, "A")

    for r in range(min_dim):
        if log_operations:
            print(f"\n=== Step {r+1}: Processing row {r+1} ===")
            print(f"Looking for pivot in row {r+1}...")

        # Find the first nonzero pivot in row r
        p = r
        while p < n and abs(A_current[r][p]) < tol:
            p += 1

        if p == n:  # No non-zero found in row
            if log_operations:
                print(
                    f"No nonzero pivot found in row {r+1}. Setting L[{r+1}][{r+1}] = 1 and copying row to U."
                )
            L[r][r] = 1.0
            for j in range(r, n):
                U[r][j] = A_current[r][j]
        else:
            pivot = A_current[r][p]
            if log_operations:
                print(f"Found pivot at A[{r+1}][{p+1}] = {pivot:.2f}")

            # Store the pivot in L (scaled to 1 for U)
            L[r][r] = pivot
            if log_operations:
                print(f"Storing pivot value {pivot:.2f} in L[{r+1}][{r+1}]")

            # Scale the row to make U[r][p] = 1 (implicitly)
            for j in range(r, n):
                U[r][j] = A_current[r][j] / pivot
            if log_operations:
                print(f"Row {r+1} scaled by 1/{pivot:.2f} and stored in U:")
                print_matrix(U, f"U after row {r+1} scaling")

            # Eliminate below
            for i in range(r + 1, m):
                factor = A_current[i][p]
                if abs(factor) > tol:
                    if log_operations:
                        print(f"Eliminating row {i+1} using factor = {factor:.2f}")
                    L[i][r] = factor
                    for j in range(r, n):
                        A_current[i][j] -= factor * U[r][j]
                    if log_operations:
                        print(f"Updated A after elimination:")
                        print_matrix(A_current, f"A after eliminating row {i+1}")

    # Handle remaining rows (for tall matrices)
    for i in range(min_dim, m):
        if log_operations:
            print(f"\n=== Final Step: Copying remaining row {i+1} to U ===")
        for j in range(0, n):
            U[i][j] = A_current[i][j]
        L[i][i] = 1.0

    if log_operations:
        print("\nFactorization complete!")
        print_matrix(L, "Final L")
        print_matrix(U, "Final U")

    return L, U


def print_matrix(matrix, name):
    print(f"{name} =")
    for row in matrix:
        s = []
        for x in row:
            if abs(x - round(x)) < 1e-5:
                s.append(str(int(round(x))))
            else:
                s.append(f"{x:.2f}")
        print("[" + ", ".join(s) + "]")
    print()


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


def main():
    A_wide = [[-3, -3, 3, 9], [-2, 0, 2, 4], [-2, -1, 2, 8]]
    A_tall = [[-1, -3, 1], [-2, -3, -7], [-1, -4, 3], [-3, -12, 11]]

    print("=" * 50)
    print("LU-Factorization for Wide Matrix (3x4):")
    print("=" * 50)
    L_wide, U_wide = lu_factorization_nonsquare(A_wide)
    LU_wide = mat_mult(L_wide, U_wide)
    print_matrix(LU_wide, "L * U (Should equal original A)")

    print("=" * 50)
    print("\nLU-Factorization for Tall Matrix (4x3):")
    print("=" * 50)
    L_tall, U_tall = lu_factorization_nonsquare(A_tall)
    LU_tall = mat_mult(L_tall, U_tall)
    print_matrix(LU_tall, "L * U (Should equal original A)")


if __name__ == "__main__":
    main()
