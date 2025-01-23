def classify_ocean_zone(depth):
    # WRITE CODE HERE
    
    return None  # modify this line
















# DO NOT MODIFY BELOW HERE
# Input reading
T = int(input())  # Number of test cases
zone_counts = {
    "Sunlight Zone": 0,
    "Twilight Zone": 0,
    "Midnight Zone": 0,
    "Abyssal Zone": 0,
    "Trenches": 0
}

for _ in range(T):
    depth = int(input().strip())  # Read a single depth value
    zone = classify_ocean_zone(depth)
    if zone:  # Increment the count only if the zone is valid
        zone_counts[zone] += 1

# Output results
for zone, count in zone_counts.items():
    print(f"{zone}: {count}")
