def lu_factorization_nonsquare(A, log_operations=True):
    m = len(A)  # Number of rows
    n = len(A[0])  # Number of columns
    min_dim = min(m, n)
    L = [[0.0] * m for _ in range(m)]  # Initialize L as m x m
    U = [[0.0] * n for _ in range(m)]  # Initialize U as m x n
    A_current = [row[:] for row in A]  # Make a copy
    tol = 1e-10  # Tolerance for zero

    if log_operations:
        print("=== LU Factorization Tutorial ===")
        print(
            "Goal: Factorize matrix A into L (lower triangular) and U (upper triangular) such that A = L*U"
        )
        print("\nInitial Matrix A:")
        print_matrix(A_current, "A")
        print(
            "\nWe'll process one pivot at a time, working left to right and top to bottom."
        )

    for r in range(min_dim):
        if log_operations:
            print(f"\n=== STEP {r+1}: Finding Pivot in Row {r+1} ===")
            print(
                f"Looking for first non-zero element in row {r+1} starting from column {r+1}..."
            )

        # Find the first nonzero pivot in row r
        p = r
        while p < n and abs(A_current[r][p]) < tol:
            p += 1

        if p == n:  # No non-zero found in row
            if log_operations:
                print(
                    f"Row {r+1} has no non-zero pivot. Setting L[{r+1}][{r+1}] = 1 and copying to U."
                )
            L[r][r] = 1.0
            for j in range(r, n):
                U[r][j] = A_current[r][j]
        else:
            pivot = A_current[r][p]
            if log_operations:
                print(f"Pivot found at position ({r+1},{p+1}) with value = {pivot:.2f}")

            # Store the pivot in L (scaled to 1 for U)
            L[r][r] = pivot
            if log_operations:
                print(f"\nACTION 1: Store pivot value {pivot:.2f} in L[{r+1}][{r+1}]")
                print("(This will be used later to reconstruct the original matrix)")

            # Scale the row to make U[r][p] = 1 (implicitly)
            if log_operations:
                print(f"\nACTION 2: Scale row {r+1} by 1/{pivot:.2f} for U matrix")
                print(f"R{r+1} (U) <- R{r+1} (A) / {pivot:.2f}")
            for j in range(r, n):
                U[r][j] = A_current[r][j] / pivot
            if log_operations:
                print_matrix(U, f"U after scaling row {r+1}")

            # Eliminate below
            for i in range(r + 1, m):
                factor = A_current[i][p]
                if abs(factor) > tol:
                    if log_operations:
                        print(
                            f"\nACTION 3: Eliminate element at ({i+1},{p+1}) using row {r+1}"
                        )
                        print(
                            f"Elimination factor = {factor:.2f} (value at position ({i+1},{p+1}))"
                        )
                        print(
                            f"Operation: R{i+1} (A) <- R{i+1} (A) - {factor:.2f} * R{r+1} (U)"
                        )
                        print(f"Which means: R{i+1} <- R{i+1} + {-factor:.2f}*R{r+1}")

                    L[i][r] = factor
                    for j in range(r, n):
                        old_val = A_current[i][j]
                        A_current[i][j] -= factor * U[r][j]
                        if log_operations and j == p:
                            print(
                                f"-> Position ({i+1},{j+1}): {old_val:.2f} - {factor:.2f}*1.00 = {A_current[i][j]:.2f}"
                            )
                        elif log_operations:
                            print(
                                f"-> Position ({i+1},{j+1}): {old_val:.2f} - {factor:.2f}*{U[r][j]:.2f} = {A_current[i][j]:.2f}"
                            )

                    if log_operations:
                        print_matrix(A_current, f"A after eliminating row {i+1}")

    # Handle remaining rows (for tall matrices)
    for i in range(min_dim, m):
        if log_operations:
            print(f"\n=== FINAL STEP: Handling remaining row {i+1} ===")
            print(
                f"Row {i+1} doesn't have a pivot position. Copying to U and setting L[{i+1}][{i+1}] = 1"
            )
        for j in range(0, n):
            U[i][j] = A_current[i][j]
        L[i][i] = 1.0

    if log_operations:
        print("\n=== FACTORIZATION COMPLETE ===")
        print("Final L matrix (contains the elimination factors):")
        print_matrix(L, "L")
        print("Final U matrix (upper triangular form):")
        print_matrix(U, "U")
        print("\nVerification:")
        print("We should have L * U = original A matrix")

    return L, U


def print_matrix(matrix, name):
    print(f"{name} =")
    for row in matrix:
        formatted_row = []
        for x in row:
            if abs(x - round(x)) < 1e-5:
                formatted_row.append(f"{int(round(x))}")
            else:
                formatted_row.append(f"{x:.2f}")
        print("[" + ", ".join(formatted_row) + "]")
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
    A_tall = [[-2, -2, 4], [-3, -1, 8], [3, 1, -6], [2, 1, -3]]
    A_wide = [[2, 6, -2, 0, 2], [3, 9, -3, 3, 1], [-1, -3, 1, -3, 1]]

    print("=" * 70)
    print("TUTORIAL: LU FACTORIZATION WITH ROW OPERATIONS EXPLANATION")
    print("=" * 70)
    print("Example Tall Matrix (4x3):")
    print_matrix(A_tall, "A")

    print("\nLet's factorize this matrix step by step:")
    print("1. We'll find pivots from top to bottom, left to right")
    print("2. For each pivot, we'll:")
    print("   - Store the pivot value in L")
    print("   - Scale the row to make the pivot = 1 in U")
    print("   - Use this row to eliminate below")
    print("3. For rows without pivots, we'll copy them to U")

    input("\nPress Enter to begin the tall matrix factorization...")

    L, U = lu_factorization_nonsquare(A_tall)

    print("\nVerification:")
    LU = mat_mult(L, U)
    print_matrix(LU, "L * U")
    print_matrix(A_tall, "Original A")
    print("These should be identical!")

    print("\n" + "=" * 70)
    print("Now let's try a WIDE matrix example (3x4):")
    print_matrix(A_wide, "A_wide")

    input("\nPress Enter to begin the wide matrix factorization...")

    L_wide, U_wide = lu_factorization_nonsquare(A_wide)

    print("\nVerification:")
    LU_wide = mat_mult(L_wide, U_wide)
    print_matrix(LU_wide, "L * U")
    print_matrix(A_wide, "Original A_wide")
    print("These should be identical!")


if __name__ == "__main__":
    main()
