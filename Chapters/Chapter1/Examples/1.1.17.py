from sympy import symbols, Eq, solve

# Define the symbols
a, b, c = symbols("a b c")

# Define the equations based on coefficient equating
eq1 = Eq(1, 2 * a + c)  # Coefficient of x^2
eq2 = Eq(-1, -a + 2 * b)  # Coefficient of x
eq3 = Eq(3, -b + 2 * c)  # Constant term

# Solve the system of equations
solutions = solve((eq1, eq2, eq3), (a, b, c))

# Print the solutions
print("Solution:")
for var, val in solutions.items():
    print(f"{var} = {val}")
