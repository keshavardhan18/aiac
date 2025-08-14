# Take input from the user as a comma-separated list of numbers
numbers = input("Enter numbers separated by commas: ")

# Convert the input string to a list of integers
num_list = [int(num.strip()) for num in numbers.split(',')]

# Initialize sums
even_sum = 0
odd_sum = 0

# Calculate sums
for num in num_list:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

# Display results
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)