from sympy import symbols, Eq, solve

x, y, t, s = symbols("x y t s")

# 1.1.2 a
# 3x + y = 2

# Way 1: Let y = t
sol_a1 = solve(Eq(3 * x + t, 2), x)
print("1.1.2 (a) Way 1: x =", sol_a1[0], ", y = t")

# Way 2: Let x = s
sol_a2 = solve(Eq(3 * s + y, 2), y)
print("1.1.2 (a) Way 2: x = s, y =", sol_a2[0])

# 1.1.2 b
# 2x - 5y = 7

# Way 1: Let y = t
sol_b1 = solve(Eq(2 * x - 5 * t, 7), x)
print("1.1.2 (b) Way 1: x =", sol_b1[0], ", y = t")

# Way 2: Let x = s
sol_b2 = solve(Eq(2 * s - 5 * y, 7), y)
print("1.1.2 (b) Way 2: x = s, y =", sol_b2[0])
