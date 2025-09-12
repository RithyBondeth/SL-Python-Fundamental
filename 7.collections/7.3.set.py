# Python Sets - Complete Guide
# Sets are unordered collections of unique elements

print("=" * 50)
print("PYTHON SETS - COMPREHENSIVE GUIDE")
print("=" * 50)

# 1. CREATING SETS
print("\n1. CREATING SETS")
print("-" * 20)

# Empty set
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Type: {type(empty_set)}")

# Set with elements
fruits = {"apple", "banana", "cherry"}
print(f"Fruits set: {fruits}")

# Set from list (duplicates removed)
numbers_list = [1, 2, 2, 3, 3, 4, 5]
numbers_set = set(numbers_list)
print(f"From list {numbers_list}: {numbers_set}")

# Set from string
char_set = set("hello")
print(f"From string 'hello': {char_set}")

# Mixed data types
mixed_set = {1, "hello", 3.14, True}
print(f"Mixed types: {mixed_set}")

# 2. SET CHARACTERISTICS
print("\n2. SET CHARACTERISTICS")
print("-" * 25)

print("• Unordered: No specific order")
print("• Unique elements: No duplicates")
print("• Mutable: Can add/remove elements")
print("• Iterable: Can loop through elements")
print("• No indexing: Cannot access by index")

# Demonstrating uniqueness
duplicate_set = {1, 1, 2, 2, 3}
print(f"Duplicates removed: {duplicate_set}")

# 3. ACCESSING SET ELEMENTS
print("\n3. ACCESSING SET ELEMENTS")
print("-" * 28)

colors = {"red", "green", "blue", "yellow"}
print(f"Colors set: {colors}")

# Check if element exists
print(f"'red' in set: {'red' in colors}")
print(f"'purple' in set: {'purple' in colors}")

# Loop through set
print("Iterating through set:")
for color in colors:
    print(f"  {color}")

# 4. ADDING ELEMENTS
print("\n4. ADDING ELEMENTS")
print("-" * 20)

animals = {"cat", "dog"}
print(f"Original: {animals}")

# Add single element
animals.add("bird")
print(f"After add('bird'): {animals}")

# Add multiple elements
animals.update(["fish", "rabbit", "mouse"])
print(f"After update with list: {animals}")

# Update with another set
more_animals = {"elephant", "lion"}
animals.update(more_animals)
print(f"After update with set: {animals}")

# Update with string (each character added)
animals.update("xy")
print(f"After update('xy'): {animals}")

# 5. REMOVING ELEMENTS
print("\n5. REMOVING ELEMENTS")
print("-" * 22)

numbers = {1, 2, 3, 4, 5, 6}
print(f"Original: {numbers}")

# Remove specific element (raises KeyError if not found)
numbers.remove(3)
print(f"After remove(3): {numbers}")

# Discard element (no error if not found)
numbers.discard(10)  # Element doesn't exist
print(f"After discard(10): {numbers}")
numbers.discard(4)
print(f"After discard(4): {numbers}")

# Pop random element
popped = numbers.pop()
print(f"Popped element: {popped}")
print(f"After pop(): {numbers}")

# Clear all elements
temp_set = {7, 8, 9}
print(f"Before clear: {temp_set}")
temp_set.clear()
print(f"After clear: {temp_set}")

# 6. SET OPERATIONS
print("\n6. SET OPERATIONS")
print("-" * 20)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

# Union (all elements from both sets)
union_result = set1.union(set2)
print(f"Union: {union_result}")
print(f"Using | operator: {set1 | set2}")

# Intersection (common elements)
intersection_result = set1.intersection(set2)
print(f"Intersection: {intersection_result}")
print(f"Using & operator: {set1 & set2}")

# Difference (elements in set1 but not in set2)
difference_result = set1.difference(set2)
print(f"Difference (set1 - set2): {difference_result}")
print(f"Using - operator: {set1 - set2}")

# Symmetric difference (elements in either set, but not both)
sym_diff_result = set1.symmetric_difference(set2)
print(f"Symmetric difference: {sym_diff_result}")
print(f"Using ^ operator: {set1 ^ set2}")

# 7. SET COMPARISON METHODS
print("\n7. SET COMPARISON METHODS")
print("-" * 28)

A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {6, 7, 8}
D = {1, 2, 3}

print(f"A: {A}")
print(f"B: {B}")
print(f"C: {C}")
print(f"D: {D}")

# Subset and superset
print(f"A is subset of B: {A.issubset(B)}")
print(f"B is superset of A: {B.issuperset(A)}")
print(f"A is disjoint with C: {A.isdisjoint(C)}")
print(f"A equals D: {A == D}")

# 8. UPDATE OPERATIONS (MODIFYING SETS IN PLACE)
print("\n8. UPDATE OPERATIONS")
print("-" * 23)

x = {1, 2, 3}
y = {3, 4, 5}
print(f"x: {x}, y: {y}")

# Union update
x_copy = x.copy()
x_copy.update(y)
print(f"After x.update(y): {x_copy}")

# Intersection update
x_copy = x.copy()
x_copy.intersection_update(y)
print(f"After x.intersection_update(y): {x_copy}")

# Difference update
x_copy = x.copy()
x_copy.difference_update(y)
print(f"After x.difference_update(y): {x_copy}")

# Symmetric difference update
x_copy = x.copy()
x_copy.symmetric_difference_update(y)
print(f"After x.symmetric_difference_update(y): {x_copy}")

# 9. SET COMPREHENSIONS
print("\n9. SET COMPREHENSIONS")
print("-" * 22)

# Basic set comprehension
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From string
vowels = {char.lower() for char in "Hello World" if char.lower() in "aeiou"}
print(f"Vowels in 'Hello World': {vowels}")

# 10. FROZEN SETS (IMMUTABLE SETS)
print("\n10. FROZEN SETS")
print("-" * 17)

# Creating frozen set
frozen_fruits = frozenset(["apple", "banana", "cherry"])
print(f"Frozen set: {frozen_fruits}")
print(f"Type: {type(frozen_fruits)}")

# Frozen sets are hashable (can be set elements)
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of frozen sets: {set_of_sets}")

# Frozen set operations work the same
frozen1 = frozenset([1, 2, 3])
frozen2 = frozenset([3, 4, 5])
print(f"Frozen union: {frozen1 | frozen2}")

# 11. PRACTICAL EXAMPLES
print("\n11. PRACTICAL EXAMPLES")
print("-" * 24)

# Remove duplicates from list
def remove_duplicates(lst):
    return list(set(lst))

duplicate_list = [1, 2, 2, 3, 3, 4, 5, 5]
unique_list = remove_duplicates(duplicate_list)
print(f"Remove duplicates: {duplicate_list} → {unique_list}")

# Find common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"Common elements: {common}")

# Count unique characters in text
text = "programming"
unique_chars = set(text)
print(f"Unique characters in '{text}': {unique_chars}")
print(f"Count: {len(unique_chars)}")

# Track visited pages (example)
visited_pages = set()
pages_to_visit = ["home", "about", "contact", "home", "services"]

for page in pages_to_visit:
    if page not in visited_pages:
        print(f"Visiting: {page}")
        visited_pages.add(page)
    else:
        print(f"Already visited: {page}")

print(f"All visited pages: {visited_pages}")

# 12. SET METHODS SUMMARY
print("\n12. SET METHODS SUMMARY")
print("-" * 25)

demo_set = {1, 2, 3}
print(f"Demo set: {demo_set}")

methods_info = [
    ("add(elem)", "Add element to set"),
    ("update(iterable)", "Add multiple elements"),
    ("remove(elem)", "Remove element (KeyError if missing)"),
    ("discard(elem)", "Remove element (no error if missing)"),
    ("pop()", "Remove and return random element"),
    ("clear()", "Remove all elements"),
    ("copy()", "Return shallow copy"),
    ("union(other)", "Return union of sets"),
    ("intersection(other)", "Return intersection"),
    ("difference(other)", "Return difference"),
    ("symmetric_difference(other)", "Return symmetric difference"),
    ("issubset(other)", "Check if subset"),
    ("issuperset(other)", "Check if superset"),
    ("isdisjoint(other)", "Check if no common elements")
]

for method, description in methods_info:
    print(f"  {method:<25} - {description}")

# 13. PERFORMANCE CONSIDERATIONS
print("\n13. PERFORMANCE NOTES")
print("-" * 22)

import time

# Fast membership testing
large_list = list(range(100000))
large_set = set(large_list)

# Test membership in list
start_time = time.time()
result = 99999 in large_list
list_time = time.time() - start_time

# Test membership in set
start_time = time.time()
result = 99999 in large_set
set_time = time.time() - start_time

print(f"Membership test (99999 in collection):")
print(f"  List time: {list_time:.8f} seconds")
print(f"  Set time:  {set_time:.8f} seconds")
print(f"  Set is ~{list_time/set_time:.0f}x faster")

print("\n" + "=" * 50)
print("Sets are ideal for:")
print("• Removing duplicates")
print("• Fast membership testing")
print("• Mathematical set operations")
print("• Tracking unique items")
print("• Finding intersections/differences")
print("=" * 50)