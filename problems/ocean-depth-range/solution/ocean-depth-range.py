def classify_ocean_zone(depth):
    if depth >= 0 and depth <= 200:
        return "Sunlight Zone"
    elif depth >= 201 and depth <= 1000:
        return "Twilight Zone"
    elif depth >= 1001 and depth <= 4000:
        return "Midnight Zone"
    elif depth >= 4001 and depth <= 6000:
        return "Abyssal Zone"
    elif depth >= 6001:
        return "Trenches"
    else:
        return "Unknown"

def count_ocean_zones(depths):
    zone_counts = {
        "Sunlight Zone": 0,
        "Twilight Zone": 0,
        "Midnight Zone": 0,
        "Abyssal Zone": 0,
        "Trenches": 0
    }
    
    for depth in depths:
        zone = classify_ocean_zone(depth)
        zone_counts[zone] += 1
    
    return zone_counts

# input handling
def main():
    import sys
    input = sys.stdin.read().strip().split()
    
    num_cases = int(input[0])
    depths = list(map(int, input[1:num_cases+1]))
    
    zone_counts = count_ocean_zones(depths)
    
    for zone, count in zone_counts.items():
        print(f"{zone}: {count}")

if __name__ == "__main__":
    main()
