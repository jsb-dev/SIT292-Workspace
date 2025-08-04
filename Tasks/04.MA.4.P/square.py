def lu_factorization(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]
    U = [[0.0] * n for _ in range(n)]
    A_current = [row[:] for row in A]
    tol = 1e-10

    print("=== LU Factorization ===")
    print("Initial matrix:")
    print_matrix(A_current)

    for k in range(n):
        print(f"\nStep {k+1}: Pivot at ({k+1},{k+1}) = {A_current[k][k]:.2f}")

        if abs(A_current[k][k]) < tol:
            print(f"Zero pivot - setting L[{k+1}][{k+1}] = 1.0")
            L[k][k] = 1.0
        else:
            pivot = A_current[k][k]
            L[k][k] = pivot

            # Scale pivot row for U
            print(f"R{k+1}(U) <- R{k+1}(A)/{pivot:.2f}")
            for j in range(k, n):
                U[k][j] = A_current[k][j] / pivot

            # Elimination
            for i in range(k + 1, n):
                factor = A_current[i][k]
                if abs(factor) > tol:
                    L[i][k] = factor
                    print(f"R{i+1} <- R{i+1} - ({factor:.2f})*R{k+1}")
                    for j in range(k, n):
                        A_current[i][j] -= factor * U[k][j]

        print("\nCurrent state:")
        print("L =")
        print_matrix(L)
        print("U =")
        print_matrix(U)
        print("Working matrix:")
        print_matrix(A_current)
        print("-" * 40)

    print("\nFactorization complete!")
    return L, U


def print_matrix(M):
    for row in M:
        print(
            "["
            + " ".join(f"{x:6.2f}" if abs(x) >= 0.01 else "  0.00" for x in row)
            + "]"
        )


def main():
    A = [[3, -6, -3, 9], [1, 1, -1, 9], [2, -7, -2, 0], [0, -3, 0, -6]]

    print("Original matrix A:")
    print_matrix(A)

    L, U = lu_factorization(A)

    print("\nFinal results:")
    print("L =")
    print_matrix(L)
    print("\nU =")
    print_matrix(U)


if __name__ == "__main__":
    main()
