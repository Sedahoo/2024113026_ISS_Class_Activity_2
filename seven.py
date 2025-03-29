def find_cube_pairs(target):
    cube_map = {}  # Dictionary to store cube values
    solutions = []

    max_num = round(target ** (1 / 3))

    for a in range(1, max_num + 1):
        a3 = a ** 3  # Precompute cube of a
        for b in range(a, max_num + 1):
            b3 = b ** 3  # Precompute cube of b
            if a3 + b3 == target:
                solutions.append((a, b))
    
    return solutions

# Compute and print results
target = 1729
pairs = find_cube_pairs(target)

print(f"Valid cube pairs for {target}:")
for a, b in pairs:
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = {target}")
