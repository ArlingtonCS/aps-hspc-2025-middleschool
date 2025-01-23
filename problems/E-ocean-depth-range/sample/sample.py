def count_ocean_zones(depths):
    # WRITE CODE HERE
    
    return None  # modify this line
















# DO NOT MODIFY BELOW HERE
num_cases = int(input())
depths = []

for _ in range(num_cases):
    depths.append(int(input()))

zone_counts = count_ocean_zones(depths)

for zone, count in zone_counts.items():
    print(f"{zone}: {count}")
