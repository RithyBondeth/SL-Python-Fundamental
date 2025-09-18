# 7. ARRAYS IN PYTHON
# ==================

print("=== ARRAYS IN PYTHON ===\n")

# In Python, we work with array-like structures in several ways:
# 1. Lists (most common, mutable)
# 2. Tuples (immutable)
# 3. Arrays from array module (homogeneous data)
# 4. NumPy arrays (for scientific computing)

print("1. PYTHON LISTS (Dynamic Arrays)")
print("-" * 40)

# Creating lists
empty_list = []
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]

print(f"Empty list: {empty_list}")
print(f"Numbers list: {numbers}")
print(f"Mixed data types: {mixed_list}")
print(f"Nested list: {nested_list}")

# List creation methods
range_list = list(range(1, 6))  # [1, 2, 3, 4, 5]
repeated_list = [0] * 5  # [0, 0, 0, 0, 0]
comprehension_list = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

print(f"From range: {range_list}")
print(f"Repeated elements: {repeated_list}")
print(f"List comprehension: {comprehension_list}")

print("\n2. ACCESSING LIST ELEMENTS")
print("-" * 40)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(f"Fruits list: {fruits}")

# Positive indexing (0-based)
print(f"First fruit (index 0): {fruits[0]}")
print(f"Third fruit (index 2): {fruits[2]}")
print(f"Last fruit (index 4): {fruits[4]}")

# Negative indexing
print(f"Last fruit (index -1): {fruits[-1]}")
print(f"Second to last (index -2): {fruits[-2]}")
print(f"First fruit (index -5): {fruits[-5]}")

# Slicing [start:end:step]
print(f"First three fruits: {fruits[0:3]}")
print(f"From index 2 to end: {fruits[2:]}")
print(f"Last three fruits: {fruits[-3:]}")
print(f"Every second fruit: {fruits[::2]}")
print(f"Reversed list: {fruits[::-1]}")

print("\n3. MODIFYING LISTS")
print("-" * 40)

# Lists are mutable
colors = ["red", "green", "blue"]
print(f"Original colors: {colors}")

# Changing elements
colors[1] = "yellow"
print(f"After changing index 1: {colors}")

# Adding elements
colors.append("purple")  # Add to end
print(f"After append: {colors}")

colors.insert(1, "orange")  # Insert at specific position
print(f"After insert at index 1: {colors}")

colors.extend(["pink", "brown"])  # Add multiple elements
print(f"After extend: {colors}")

# Removing elements
colors.remove("orange")  # Remove first occurrence
print(f"After remove 'orange': {colors}")

popped_color = colors.pop()  # Remove and return last element
print(f"Popped color: {popped_color}")
print(f"After pop: {colors}")

popped_at_index = colors.pop(1)  # Remove at specific index
print(f"Popped at index 1: {popped_at_index}")
print(f"After pop at index: {colors}")

del colors[0]  # Delete by index
print(f"After del colors[0]: {colors}")

print("\n4. LIST METHODS")
print("-" * 40)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Original numbers: {numbers}")

# Common list methods
print(f"Length: {len(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 4: {numbers.index(4)}")
print(f"Max value: {max(numbers)}")
print(f"Min value: {min(numbers)}")
print(f"Sum: {sum(numbers)}")

# Sort and reverse
numbers_copy = numbers.copy()  # Create a copy
numbers_copy.sort()
print(f"Sorted (ascending): {numbers_copy}")

numbers_copy.sort(reverse=True)
print(f"Sorted (descending): {numbers_copy}")

numbers.reverse()
print(f"Reversed original: {numbers}")

# Clear all elements
test_list = [1, 2, 3]
test_list.clear()
print(f"After clear: {test_list}")

print("\n5. TUPLES (Immutable Arrays)")
print("-" * 40)

# Creating tuples
empty_tuple = ()
single_tuple = (42,)  # Note the comma for single element
coordinates = (10, 20)
rgb_color = (255, 128, 0)
mixed_tuple = (1, "hello", 3.14, True)

print(f"Empty tuple: {empty_tuple}")
print(f"Single element: {single_tuple}")
print(f"Coordinates: {coordinates}")
print(f"RGB color: {rgb_color}")
print(f"Mixed tuple: {mixed_tuple}")

# Tuple without parentheses
point = 5, 10, 15
print(f"Point (no parentheses): {point}")

# Accessing tuple elements (same as lists)
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"Last element of point: {point[-1]}")

# Tuple unpacking
x, y = coordinates
print(f"Unpacked - x: {x}, y: {y}")

r, g, b = rgb_color
print(f"Unpacked RGB - R: {r}, G: {g}, B: {b}")

# Tuple methods (limited because immutable)
numbers_tuple = (1, 2, 3, 2, 4, 2, 5)
print(f"Count of 2: {numbers_tuple.count(2)}")
print(f"Index of 4: {numbers_tuple.index(4)}")
print(f"Length: {len(numbers_tuple)}")

print("\n6. ARRAY MODULE (Homogeneous Arrays)")
print("-" * 40)

import array

# Type codes: 'i' = signed int, 'f' = float, 'd' = double, etc.
int_array = array.array('i', [1, 2, 3, 4, 5])
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4])

print(f"Integer array: {int_array}")
print(f"Float array: {float_array}")
print(f"Array type code: {int_array.typecode}")

# Array methods
int_array.append(6)
print(f"After append: {int_array}")

int_array.insert(0, 0)
print(f"After insert at 0: {int_array}")

print(f"Array as list: {int_array.tolist()}")

print("\n7. LIST VS TUPLE VS ARRAY COMPARISON")
print("-" * 40)

print("Lists:")
print("  - Mutable (can be changed)")
print("  - Mixed data types allowed")
print("  - More memory overhead")
print("  - Syntax: [1, 2, 3]")

print("\nTuples:")
print("  - Immutable (cannot be changed)")
print("  - Mixed data types allowed")
print("  - Less memory overhead")
print("  - Syntax: (1, 2, 3)")

print("\nArrays:")
print("  - Mutable but homogeneous (same type)")
print("  - More memory efficient for large datasets")
print("  - Limited to numeric types")
print("  - Syntax: array.array('i', [1, 2, 3])")

print("\n8. MULTIDIMENSIONAL ARRAYS (NESTED LISTS)")
print("-" * 40)

# 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2D Matrix:")
for row in matrix:
    print(f"  {row}")

# Accessing 2D elements
print(f"Element at row 1, col 2: {matrix[1][2]}")  # 6
print(f"First row: {matrix[0]}")
print(f"Second column: {[row[1] for row in matrix]}")

# 3D array
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
]

print(f"\n3D Cube: {cube}")
print(f"Element at [0][1][0]: {cube[0][1][0]}")  # 3

print("\n9. LIST COMPREHENSIONS (Advanced)")
print("-" * 40)

# Basic comprehensions
squares = [x**2 for x in range(5)]
print(f"Squares: {squares}")

# With condition
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(f"Even squares: {even_squares}")

# Nested comprehension (2D)
multiplication_table = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Multiplication table:")
for row in multiplication_table:
    print(f"  {row}")

# String processing
words = ["hello", "world", "python", "arrays"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase words: {uppercase_words}")

# Filtering
long_words = [word for word in words if len(word) > 5]
print(f"Words longer than 5 chars: {long_words}")

print("\n10. PRACTICAL EXAMPLES")
print("-" * 40)

# Shopping cart
shopping_cart = []
shopping_cart.extend(["apples", "bread", "milk"])
shopping_cart.append("cheese")
print(f"Shopping cart: {shopping_cart}")

# Grade tracking
grades = [85, 92, 78, 96, 88]
average = sum(grades) / len(grades)
highest = max(grades)
lowest = min(grades)

print(f"Grades: {grades}")
print(f"Average: {average:.1f}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

# Data processing
temperatures = [23.5, 25.0, 22.1, 26.8, 24.3]
celsius_to_fahrenheit = [(temp * 9/5) + 32 for temp in temperatures]
print(f"Celsius: {temperatures}")
print(f"Fahrenheit: {celsius_to_fahrenheit}")

# Finding elements
inventory = ["laptop", "mouse", "keyboard", "monitor", "speakers"]
search_item = "keyboard"
if search_item in inventory:
    position = inventory.index(search_item)
    print(f"'{search_item}' found at position {position}")
else:
    print(f"'{search_item}' not found in inventory")

print("\n11. COMMON ARRAY OPERATIONS")
print("-" * 40)

arr1 = [1, 2, 3]
arr2 = [4, 5, 6]

# Concatenation
combined = arr1 + arr2
print(f"Concatenated: {combined}")

# Repetition
repeated = arr1 * 3
print(f"Repeated: {repeated}")

# Membership testing
print(f"2 in arr1: {2 in arr1}")
print(f"7 in arr1: {7 in arr1}")

# Iteration
print("Iterating with index:")
for i, value in enumerate(arr1):
    print(f"  Index {i}: {value}")

# Sorting different data types
mixed_numbers = [3.14, 2, 1.5, 4]
mixed_numbers.sort()
print(f"Sorted mixed numbers: {mixed_numbers}")

strings = ["banana", "apple", "cherry"]
strings.sort()
print(f"Sorted strings: {strings}")

# Reverse sorting
strings.sort(reverse=True)
print(f"Reverse sorted strings: {strings}")

print("\n=== ARRAY LESSON COMPLETE ===")
print("Key takeaways:")
print("1. Lists are the most versatile array-like structure")
print("2. Use tuples for immutable sequences")
print("3. Use array module for memory-efficient numeric arrays")
print("4. List comprehensions provide powerful data processing")
print("5. Choose the right structure based on your needs")