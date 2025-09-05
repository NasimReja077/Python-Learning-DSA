# Alternative version with explicit comments
numbers = [12, 75, 150, 180, 145, 525, 50]

print("Processing numbers:")
for number in numbers:
    # First check: Stop if number is too large
    if number > 500:
        print(f"Found {number} > 500, stopping loop")
        break
    
    # Second check: Skip large numbers
    if number > 150:
        print(f"Skipping {number} (> 150)")
        continue
    
    # Third check: Print if divisible by 5
    if number % 5 == 0:
        print(f"{number} is divisible by 5")
    else:
        print(f"{number} is not divisible by 5")

print("Loop finished")
