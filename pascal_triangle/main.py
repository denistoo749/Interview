#!/usr/bin/python3

def print_triangle(triangle):
    """Prints Pascal's Triangle in a formatted way."""
    max_len = len(triangle[-1])
    for row in triangle:
        # Convert each number to string and join them with spaces
        row_str = ' '.join(map(str, row))
        # Center each row for better formatting
        print(row_str.center(max_len * 2))

# Import the pascal_triangle function
pascal_triangle = __import__('pascal_triangle').pascal_triangle

# Generate Pascal's Triangle for n = 5
triangle = pascal_triangle(5)

# Print the formatted Pascal's Triangle
print_triangle(triangle)