# Get user input as a list of integers
user_input = input("Enter integers separated by spaces: ")
numbers = list(map(int, user_input.split()))

# Remove duplicates using set, then sort
unique_sorted = sorted(set(numbers))

# Print the result
print("Sorted list without duplicates:", unique_sorted)