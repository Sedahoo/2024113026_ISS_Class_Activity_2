def find_cube_pairs(target):
    solutions = []  # Store valid (a, b) pairs
    max_num = round(target ** (1/3))  # Max possible value for a and b

    for a in range(1, max_num + 1):
        for b in range(a, max_num + 1):  # Avoid duplicate pairs
            if a**3 + b**3 == target:  
                solutions.append((a, b))  

    return solutions  

# Find cube pairs for 1729
pairs = find_cube_pairs(1729)

print("Valid cube pairs for 1729:")
for a, b in pairs:
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")
