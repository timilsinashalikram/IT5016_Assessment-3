# Input the range for perfect squares
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Create a list of perfect squares using a for loop
perfect_squares = []
for num in range(start, end + 1):
    if num >= 0 and (num ** 0.5).is_integer():
        perfect_squares.append(num)

# Output the list of perfect squares
print(f"Perfect squares between {start} and {end}:")
print(perfect_squares)
