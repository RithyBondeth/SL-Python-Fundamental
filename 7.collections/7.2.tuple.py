# PYTHON TUPLES - COMPREHENSIVE GUIDE

print("=" * 70)
print("PYTHON TUPLES - COMPLETE TUTORIAL")
print("=" * 70)

print("\n" + "=" * 50)
print("1. WHAT ARE TUPLES?")
print("=" * 50)

print("Tuples are ordered, immutable collections that can store multiple items")
print("Key characteristics:")
print("✓ Ordered - items have a defined order")
print("✓ Immutable - cannot be changed after creation")
print("✓ Allow duplicates - same value can appear multiple times")
print("✓ Can store different data types")
print("✓ Defined using parentheses () or tuple() constructor")

print("\n" + "=" * 50)
print("2. CREATING TUPLES")
print("=" * 50)

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Tuple with items
fruits = ("apple", "banana", "orange", "grape")
print(f"Fruits tuple: {fruits}")

# Single item tuple (note the comma!)
single_item = ("hello",)
print(f"Single item tuple: {single_item}")

# Without comma, it's just a string
not_tuple = ("hello")
print(f"Not a tuple (missing comma): {not_tuple} - type: {type(not_tuple)}")

# Mixed data types
mixed_tuple = (1, "hello", 3.14, True, None)
print(f"Mixed data types: {mixed_tuple}")

# Tuple with duplicates
numbers = (1, 2, 2, 3, 2, 4, 5)
print(f"Tuple with duplicates: {numbers}")

# Without parentheses (tuple packing)
coordinates = 10, 20, 30
print(f"Tuple packing: {coordinates}")

# Using tuple() constructor
tuple_from_string = tuple("hello")
tuple_from_list = tuple([1, 2, 3, 4, 5])
tuple_from_range = tuple(range(5))
print(f"From string: {tuple_from_string}")
print(f"From list: {tuple_from_list}")
print(f"From range: {tuple_from_range}")

# Nested tuples
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(f"2D tuple (matrix): {matrix}")

print("\n" + "=" * 50)
print("3. ACCESSING TUPLE ELEMENTS")
print("=" * 50)

colors = ("red", "green", "blue", "yellow", "purple")
print(f"Colors tuple: {colors}")

# Positive indexing (0-based)
print(f"First element (index 0): {colors[0]}")
print(f"Second element (index 1): {colors[1]}")
print(f"Third element (index 2): {colors[2]}")

# Negative indexing (-1 is last element)
print(f"Last element (index -1): {colors[-1]}")
print(f"Second last (index -2): {colors[-2]}")

# Getting tuple length
print(f"Tuple length: {len(colors)}")

# Index visualization
print(f"\nIndex visualization:")
print(f"Positive: {tuple(range(len(colors)))}")
print(f"Tuple:    {colors}")
print(f"Negative: {tuple(i-len(colors) for i in range(len(colors)))}")

print("\n" + "=" * 50)
print("4. TUPLE SLICING")
print("=" * 50)

numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Original tuple: {numbers}")

# Basic slicing [start:end]
print(f"numbers[2:6]: {numbers[2:6]}")        # Items 2,3,4,5
print(f"numbers[:4]: {numbers[:4]}")          # First 4 items
print(f"numbers[6:]: {numbers[6:]}")          # From index 6 to end
print(f"numbers[:]: {numbers[:]}")            # Entire tuple (copy)

# Slicing with step [start:end:step]
print(f"numbers[::2]: {numbers[::2]}")        # Every 2nd element
print(f"numbers[1::2]: {numbers[1::2]}")      # Every 2nd, starting from index 1
print(f"numbers[::3]: {numbers[::3]}")        # Every 3rd element

# Negative slicing
print(f"numbers[-3:]: {numbers[-3:]}")        # Last 3 elements
print(f"numbers[:-2]: {numbers[:-2]}")        # All except last 2
print(f"numbers[-5:-1]: {numbers[-5:-1]}")    # Slice using negative indices

# Reverse slicing
print(f"numbers[::-1]: {numbers[::-1]}")      # Reverse the tuple
print(f"numbers[8:2:-1]: {numbers[8:2:-1]}")  # Reverse slice from 8 to 2

print("\n" + "=" * 50)
print("5. TUPLE IMMUTABILITY")
print("=" * 50)

# Tuples cannot be modified after creation
animals = ("cat", "dog", "bird", "fish")
print(f"Original tuple: {animals}")

print("Attempting to modify tuple:")
try:
    animals[1] = "rabbit"  # This will raise an error
except TypeError as e:
    print(f"Error: {e}")

print("Tuples are immutable - you cannot change, add, or remove items")

# However, if tuple contains mutable objects, those can be modified
mutable_content = ([1, 2, 3], {"key": "value"})
print(f"\nTuple with mutable content: {mutable_content}")

# Modifying the list inside the tuple
mutable_content[0].append(4)
print(f"After modifying list inside: {mutable_content}")

# But you still can't reassign the tuple element
try:
    mutable_content[0] = [5, 6, 7]  # This will fail
except TypeError as e:
    print(f"Error: {e}")

print("\n" + "=" * 50)
print("6. TUPLE METHODS")
print("=" * 50)

# Tuples have only two built-in methods
print("Tuples have only 2 built-in methods:")

# count() - count occurrences
numbers = (1, 2, 3, 2, 4, 2, 5, 2)
print(f"Tuple: {numbers}")

count_2 = numbers.count(2)
print(f"count(2): {count_2}")

count_6 = numbers.count(6)
print(f"count(6): {count_6}")

# index() - find first occurrence index
fruits = ("apple", "banana", "orange", "banana", "grape")
print(f"\nFruits tuple: {fruits}")

banana_index = fruits.index("banana")
print(f"index('banana'): {banana_index}")

# index() with start and end parameters
banana_index = fruits.index("banana", 2)  # Search starting from index 2
print(f"index('banana', 2): {banana_index}")

# Checking if item exists
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'mango' in fruits: {'mango' in fruits}")

print("\n" + "=" * 50)
print("7. TUPLE UNPACKING")
print("=" * 50)

# Basic unpacking
coordinates = (10, 20)
x, y = coordinates
print(f"Tuple: {coordinates}")
print(f"Unpacked: x = {x}, y = {y}")

# Multiple values
person_data = ("Alice", 25, "Engineer", "New York")
name, age, job, city = person_data
print(f"\nPerson data: {person_data}")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Job: {job}")
print(f"City: {city}")

# Unpacking with star operator (*)
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
first, second, *middle, last = numbers
print(f"\nNumbers: {numbers}")
print(f"First: {first}")
print(f"Second: {second}")
print(f"Middle: {middle}")
print(f"Last: {last}")

# Unpacking in function calls
def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

point1 = (0, 0)
point2 = (3, 4)
distance = calculate_distance(*point1, *point2)
print(f"\nDistance between {point1} and {point2}: {distance}")

# Swapping variables using tuple unpacking
a, b = 10, 20
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}")

print("\n" + "=" * 50)
print("8. ITERATING THROUGH TUPLES")
print("=" * 50)

fruits = ("apple", "banana", "orange")

# Basic iteration
print("Basic iteration:")
for fruit in fruits:
    print(f"  {fruit}")

# Iteration with index using enumerate()
print(f"\nWith index using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Iteration with index using range()
print(f"\nWith index using range():")
for i in range(len(fruits)):
    print(f"  {i}: {fruits[i]}")

# Iterating multiple tuples with zip()
colors = ("red", "yellow", "orange")
print(f"\nIterating two tuples together:")
for fruit, color in zip(fruits, colors):
    print(f"  {fruit} is {color}")

print("\n" + "=" * 50)
print("9. TUPLE OPERATIONS")
print("=" * 50)

# Concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Concatenation: {tuple1} + {tuple2} = {combined}")

# Repetition
pattern = (0, 1)
repeated = pattern * 4
print(f"Repetition: {pattern} * 4 = {repeated}")

# Membership testing
numbers = (1, 2, 3, 4, 5)
print(f"\nTuple: {numbers}")
print(f"3 in tuple: {3 in numbers}")
print(f"10 in tuple: {10 in numbers}")

# Min, max, sum (for numeric tuples)
numbers = (3, 1, 4, 1, 5, 9, 2, 6, 5)
print(f"\nNumbers: {numbers}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

# Comparing tuples
tuple_a = (1, 2, 3)
tuple_b = (1, 2, 4)
tuple_c = (1, 2, 3)

print(f"\nTuple comparison:")
print(f"{tuple_a} == {tuple_c}: {tuple_a == tuple_c}")
print(f"{tuple_a} < {tuple_b}: {tuple_a < tuple_b}")
print(f"{tuple_a} > {tuple_b}: {tuple_a > tuple_b}")

print("\n" + "=" * 50)
print("10. TUPLE CONVERSION")
print("=" * 50)

# Converting between tuple and list
original_tuple = (1, 2, 3, 4, 5)
converted_list = list(original_tuple)
print(f"Tuple to list: {original_tuple} → {converted_list}")

original_list = [6, 7, 8, 9, 10]
converted_tuple = tuple(original_list)
print(f"List to tuple: {original_list} → {converted_tuple}")

# Converting string to tuple
string = "hello"
char_tuple = tuple(string)
print(f"String to tuple: '{string}' → {char_tuple}")

# Converting set to tuple
original_set = {3, 1, 4, 1, 5}  # Note: sets don't keep duplicates
tuple_from_set = tuple(original_set)
print(f"Set to tuple: {original_set} → {tuple_from_set}")

print("\n" + "=" * 50)
print("11. NAMED TUPLES")
print("=" * 50)

from collections import namedtuple

# Creating a named tuple class
Point = namedtuple('Point', ['x', 'y'])
Person = namedtuple('Person', ['name', 'age', 'city'])

# Creating instances
point1 = Point(10, 20)
point2 = Point(x=30, y=40)

person1 = Person("Alice", 25, "New York")
person2 = Person(name="Bob", age=30, city="London")

print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
print(f"Person 1: {person1}")
print(f"Person 2: {person2}")

# Accessing fields
print(f"\nAccessing named tuple fields:")
print(f"Point 1 - x: {point1.x}, y: {point1.y}")
print(f"Person 1 - name: {person1.name}, age: {person1.age}")

# Named tuples are still tuples
print(f"Point 1 by index: {point1[0]}, {point1[1]}")

# Named tuple methods
print(f"Point 1 as dict: {point1._asdict()}")
print(f"Person 1 fields: {person1._fields}")

# Creating new instance with replaced values
point3 = point1._replace(x=50)
print(f"Point 1 with replaced x: {point3}")

print("\n" + "=" * 50)
print("12. PRACTICAL EXAMPLES")
print("=" * 50)

print("Example 1: Coordinates and GPS Data")
# Using tuples for immutable coordinate data
locations = [
    ("New York", 40.7128, -74.0060),
    ("London", 51.5074, -0.1278),
    ("Tokyo", 35.6762, 139.6503),
    ("Sydney", -33.8688, 151.2093)
]

print("City coordinates:")
for city, lat, lng in locations:
    print(f"  {city}: ({lat}, {lng})")

# Calculate distances (simplified)
import math

def calculate_distance(coord1, coord2):
    lat1, lng1 = coord1[1], coord1[2]
    lat2, lng2 = coord2[1], coord2[2]
    # Simplified distance calculation
    return math.sqrt((lat2 - lat1)**2 + (lng2 - lng1)**2)

ny_london_distance = calculate_distance(locations[0], locations[1])
print(f"\nDistance between NYC and London: {ny_london_distance:.4f}")

print(f"\nExample 2: RGB Color Representation")
# Using tuples for RGB colors
colors = {
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "yellow": (255, 255, 0),
    "magenta": (255, 0, 255),
    "cyan": (0, 255, 255)
}

print("RGB Color values:")
for color_name, (r, g, b) in colors.items():
    print(f"  {color_name.capitalize()}: RGB({r}, {g}, {b})")

# Color mixing function
def mix_colors(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2
    return ((r1 + r2) // 2, (g1 + g2) // 2, (b1 + b2) // 2)

mixed = mix_colors(colors["red"], colors["blue"])
print(f"\nMixing red and blue: {mixed}")

print(f"\nExample 3: Database Records")
# Using tuples for database-like records
students = [
    ("Alice", 20, "Computer Science", 3.8),
    ("Bob", 19, "Mathematics", 3.6),
    ("Charlie", 21, "Physics", 3.9),
    ("Diana", 20, "Engineering", 3.7)
]

print("Student records:")
for name, age, major, gpa in students:
    print(f"  {name} ({age}): {major}, GPA: {gpa}")

# Finding students with high GPA
high_achievers = [student for student in students if student[3] >= 3.7]
print(f"\nHigh achievers (GPA >= 3.7):")
for name, age, major, gpa in high_achievers:
    print(f"  {name}: {gpa}")

print("\n" + "=" * 50)
print("13. TUPLES VS LISTS COMPARISON")
print("=" * 50)

import sys
import time

print("Performance and Memory Comparison:")

# Memory usage comparison
list_data = [1, 2, 3, 4, 5] * 1000
tuple_data = (1, 2, 3, 4, 5) * 1000

list_size = sys.getsizeof(list_data)
tuple_size = sys.getsizeof(tuple_data)

print(f"List memory usage: {list_size} bytes")
print(f"Tuple memory usage: {tuple_size} bytes")
print(f"Tuple uses {((list_size - tuple_size) / list_size * 100):.1f}% less memory")

# Access speed comparison
def access_speed_test():
    data_list = list(range(10000))
    data_tuple = tuple(range(10000))
    
    # List access
    start_time = time.time()
    for i in range(1000):
        _ = data_list[i % len(data_list)]
    list_time = time.time() - start_time
    
    # Tuple access
    start_time = time.time()
    for i in range(1000):
        _ = data_tuple[i % len(data_tuple)]
    tuple_time = time.time() - start_time
    
    print(f"\nAccess speed (1000 operations):")
    print(f"List access: {list_time:.6f} seconds")
    print(f"Tuple access: {tuple_time:.6f} seconds")

access_speed_test()

print(f"\nWhen to use Tuples vs Lists:")
print("Use TUPLES when:")
print("✓ Data shouldn't change (coordinates, RGB values)")
print("✓ Need hashable objects (dictionary keys)")
print("✓ Want better performance and less memory")
print("✓ Returning multiple values from functions")
print("✓ Configuration settings")

print(f"\nUse LISTS when:")
print("✓ Data needs to be modified")
print("✓ Need to add/remove items")
print("✓ Order of items may change")
print("✓ Need list methods (append, remove, etc.)")

print("\n" + "=" * 50)
print("14. TUPLE BEST PRACTICES")
print("=" * 50)

print("Best Practices:")
print("✓ Use tuples for related data that belongs together")
print("✓ Use tuple unpacking for multiple return values")
print("✓ Use named tuples for better code readability")
print("✓ Use tuples as dictionary keys when needed")
print("✓ Don't forget the comma for single-item tuples")

# Example of tuple as dictionary key
coordinate_data = {
    (0, 0): "Origin",
    (1, 1): "Northeast",
    (-1, -1): "Southwest",
    (10, 5): "Point A"
}

print(f"\nTuples as dictionary keys:")
for coord, description in coordinate_data.items():
    print(f"  {coord}: {description}")

# Multiple return values
def get_name_parts(full_name):
    parts = full_name.split()
    if len(parts) >= 2:
        return parts[0], parts[-1], " ".join(parts[1:-1])
    return parts[0], "", ""

first, last, middle = get_name_parts("John Michael Smith")
print(f"\nName parsing: First='{first}', Middle='{middle}', Last='{last}'")

print("\n" + "=" * 70)
print("PYTHON TUPLES SUMMARY")
print("=" * 70)
print("✓ Ordered, immutable collections")
print("✓ Support indexing, slicing, and iteration")
print("✓ Only 2 methods: count() and index()")
print("✓ Can store any data type")
print("✓ Perfect for tuple unpacking")
print("✓ More memory efficient than lists")
print("✓ Can be used as dictionary keys")
print("✓ Great for coordinates, RGB values, database records")
print("=" * 70)