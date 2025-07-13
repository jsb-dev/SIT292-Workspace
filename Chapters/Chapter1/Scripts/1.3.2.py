from sympy import symbols, Matrix, linsolve, pprint, Eq

# Define symbols
x, y, z, a = symbols("x y z a", real=True)

# Coefficient matrix (left-hand side) of the system
A = Matrix([[1, -2, 1], [1, a, -3], [-1, 6, -5]])

# Right-hand side (homogeneous system)
b = Matrix([0, 0, 0])

# Augmented matrix
augmented = A.row_join(b)


# Step 1: Find values of a for which system has nontrivial solutions
# That happens when rank of coefficient matrix < number of variables
# i.e., rank < 3
def find_nontrivial_a():
    free_a = []
    for a_val in range(-10, 11):
        A_sub = A.subs(a, a_val)
        rank = A_sub.rank()
        if rank < 3:
            free_a.append(a_val)
    return free_a


# Step 2: Solve the system symbolically for specific a
def solve_for_a(a_val):
    system = [
        Eq(x - 2 * y + z, 0),
        Eq(x + a_val * y - 3 * z, 0),
        Eq(-x + 6 * y - 5 * z, 0),
    ]
    sol = linsolve(system, x, y, z)
    print(f"\na = {a_val} ⇒ Nontrivial solution:")
    pprint(sol)


# Find values of a with nontrivial solutions
a_candidates = find_nontrivial_a()
print("🧮 Values of a that lead to nontrivial solutions:")
print(a_candidates)

# Print full solution for each candidate
for a_val in a_candidates:
    solve_for_a(a_val)
