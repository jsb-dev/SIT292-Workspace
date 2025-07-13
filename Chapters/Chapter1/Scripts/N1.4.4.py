from sympy import symbols, Eq, solve, Matrix, linsolve, simplify

# Define symbols
x, y, z, k = symbols("x y z k", real=True)

# System of equations
eq1 = Eq(x + y, k)
eq2 = Eq(2 * x + (2 * k - 2) * y + 3 * k * z, -2)
eq3 = Eq(-x - y + (k**2 - 6 * k + 8) * z, -4)

# Construct augmented matrix for analysis
A = Matrix(
    [[1, 1, 0, k], [2, (2 * k - 2), 3 * k, -2], [-1, -1, (k**2 - 6 * k + 8), -4]]
)

# Reduce to RREF
rref_matrix, pivots = A.rref()


# Analyze rank vs unknowns
def analyze_solution_type(k_val):
    system = [eq1.subs(k, k_val), eq2.subs(k, k_val), eq3.subs(k, k_val)]
    sol = linsolve(system, x, y, z)

    if sol == set():
        return "No solution"

    try:
        result = next(iter(sol))
    except StopIteration:
        return "No solution"

    # If any components of the solution contain free symbols, it's parametric
    if any(getattr(s, "free_symbols", set()) for s in result):
        return "Multiple solutions"
    else:
        return "Unique solution"


# Scan integer values of k from -5 to 10
for kv in range(-5, 11):
    result = analyze_solution_type(kv)
    print(f"k = {kv}: {result}")

# Example: multiple solution case
k_example = 2
system_example = [
    eq1.subs(k, k_example),
    eq2.subs(k, k_example),
    eq3.subs(k, k_example),
]
sol_set = linsolve(system_example, x, y, z)

if sol_set:
    sol = next(iter(sol_set))
    print(f"\nGeneral solution for k = {k_example}:")
    print(sol)

    # Express vector form if free parameters exist
    free_vars = [s for s in sol if s.free_symbols]
    if free_vars:
        param = list(free_vars[0])[0]
        print(f"\nVector form:")
        print(f"⎛x⎞ = b + a·v")
        print(f"b = {sol}")
        print(f"v = derivative of solution w.r.t {param}")
else:
    print(f"\nNo solution returned for k = {k_example} (unexpected).")
