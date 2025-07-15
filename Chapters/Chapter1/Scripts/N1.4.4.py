import sympy as sp

# Define variables
x, y, z, k = sp.symbols("x y z k")

# Define equations
eq1 = sp.Eq(x + y, k)
eq2 = sp.Eq(2 * x + (2 * k - 2) * y + 3 * k * z, -2)
eq3 = sp.Eq(-x - y + (k**2 - 6 * k + 8) * z, -4)

# Solve the system of equations
solutions = sp.solve((eq1, eq2, eq3), (x, y, z))

# Print solutions
for k_val in [
    0,
    1,
    2,
]:  # Test for no solution, unique solution, and multiple solutions respectively
    sol = solutions.subs(k, k_val)
    print(f"k = {k_val}:")
    if not sol:
        print("No solution\n")
    else:
        print(sol)

# For case (iii), find all solutions in terms of a vector form (x y z)^T = b + a·v
print("\nCase (iii) - Multiple Solutions:")
for k_val in [2]:  # Test for multiple solutions (k = 2)
    sol = solutions.subs(k, k_val)
    if len(sol) > 1:
        print("Multiple solutions exist:\n")
        b = sp.Matrix([sol[i].subs("a", 0) for i in range(3)])
        v = sp.Matrix([sp.diff(sol[i], "a") for i in range(3)])
        print(f"(x y z)^T = {b} + a·{v}\n")
