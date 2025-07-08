from sympy import symbols, Eq, simplify

# 1.1.1 a
# Define the parameter
t = symbols(
    "t"
)  # One symnol because the solution is expressed with one unknown parameter

# Define the expressions
x = 19 * t - 35
y = 25 - 13 * t
z = t

# Define the equations
eq1 = Eq(2 * x + 3 * y + z, 5)
eq2 = Eq(5 * x + 7 * y - 4 * z, 0)

# Substitute and simplify
eq1_simplified = simplify(eq1.lhs - eq1.rhs)
eq2_simplified = simplify(eq2.lhs - eq2.rhs)

print("Equation 1 simplifies to:", eq1_simplified)
print("Equation 2 simplifies to:", eq2_simplified)

# If both simplify to 0, the solution is valid for all t

# 1.1.1 b
# Define the parameters
s, t = symbols(
    "s t"
)  # Two symbols because the solution is expressed with two unknown parameters

# Define the expressions
x1 = 2 * s + 12 * t + 13
x2 = s
x3 = -s - 3 * t - 3
x4 = t

# Define the equations
eq1 = Eq(2 * x1 + 5 * x2 + 9 * x3 + 3 * x4, -1)
eq2 = Eq(x1 + 2 * x2 + 4 * x3, 1)

# Substitute and simplify
eq1_simplified = simplify(eq1.lhs - eq1.rhs)
eq2_simplified = simplify(eq2.lhs - eq2.rhs)

print("Equation 1 simplifies to:", eq1_simplified)
print("Equation 2 simplifies to:", eq2_simplified)

# If both simplify to 0, the solution is valid for all s and
