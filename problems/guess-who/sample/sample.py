def find_mystery_guest(number_of_guests, guests, clues):
    # WRITE CODE HERE
    
    return None

# DO NOT MODIFY BELOW HERE
test_cases = int(input().strip())
results = []

for _ in range(test_cases):
    number_of_guests = int(input().strip())
    guests = [input().strip().split() for _ in range(number_of_guests)]
    clues = input().strip().split()
    result = find_mystery_guest(number_of_guests, guests, clues)
    results.append(result)

# Output results
for result in results:
    if isinstance(result, list): # if theres multiple people
        print(*result)
    else:
        print(result)
