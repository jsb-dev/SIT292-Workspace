import sympy as sp

# Define symbols
x, y, x_p, y_p = sp.symbols("x y x_p y_p")

# Variable substitutions
x_sub = 5 * x_p - 2 * y_p
y_sub = -7 * x_p + 3 * y_p

# Transformed equations using substitutions
eq1 = sp.Eq(3 * x_sub + 2 * y_sub, 5)
eq2 = sp.Eq(7 * x_sub + 5 * y_sub, 1)

# Solve the transformed system
solution_prime = sp.solve((eq1, eq2), (x_p, y_p), dict=True)[0]
x_p_val = solution_prime[x_p]
y_p_val = solution_prime[y_p]

# Back-substitute to find original x and y
x_val = x_sub.subs({x_p: x_p_val, y_p: y_p_val})
y_val = y_sub.subs({x_p: x_p_val, y_p: y_p_val})

print(f"x' = {x_p_val}")
print(f"y' = {y_p_val}")
print(f"x = {x_val}")
print(f"y = {y_val}")
