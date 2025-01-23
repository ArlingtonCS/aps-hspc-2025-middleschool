def calculate_final_position(instructions):
    # WRITE CODE HERE
    
    return None # MODIFY THIS LINE








# DO NOT MODIFY BELOW HERE
# Input Parsing
n = int(input())
instructions = []

for _ in range(n):
    line = input().split()
    direction = line[0]
    units = int(line[1])
    instructions.append((direction, units))

# Calculate final position
final_position = calculate_final_position(instructions)

# Output the result
print(f"({final_position[0]},{final_position[1]})")
