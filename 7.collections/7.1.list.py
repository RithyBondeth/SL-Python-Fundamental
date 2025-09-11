# PYTHON LISTS - COMPREHENSIVE GUIDE

print("=" * 70)
print("PYTHON LISTS - COMPLETE TUTORIAL")
print("=" * 70)

print("\n" + "=" * 50)
print("1. WHAT ARE LISTS?")
print("=" * 50)

print("Lists are ordered, mutable collections that can store multiple items")
print("Key characteristics:")
print(" Ordered - items have a defined order")
print(" Mutable - can be changed after creation") 
print(" Allow duplicates - same value can appear multiple times")
print(" Dynamic size - can grow and shrink")
print(" Can store different data types")

print("\n" + "=" * 50)
print("2. CREATING LISTS")
print("=" * 50)

# Empty list
empty_list = []
print(f"Empty list: {empty_list}")

# List with items
fruits = ["apple", "banana", "orange", "grape"]
print(f"Fruits list: {fruits}")

# Mixed data types
mixed_list = [1, "hello", 3.14, True, None]
print(f"Mixed data types: {mixed_list}")

# List with duplicates
numbers = [1, 2, 2, 3, 2, 4, 5]
print(f"List with duplicates: {numbers}")

# Using list() constructor
list_from_string = list("hello")
list_from_range = list(range(5))
print(f"From string: {list_from_string}")
print(f"From range: {list_from_range}")

# Nested lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"2D list (matrix): {matrix}")

print("\n" + "=" * 50)
print("3. ACCESSING LIST ELEMENTS")
print("=" * 50)

colors = ["red", "green", "blue", "yellow", "purple"]
print(f"Colors list: {colors}")

# Positive indexing (0-based)
print(f"First element (index 0): {colors[0]}")
print(f"Second element (index 1): {colors[1]}")
print(f"Third element (index 2): {colors[2]}")

# Negative indexing (-1 is last element)
print(f"Last element (index -1): {colors[-1]}")
print(f"Second last (index -2): {colors[-2]}")

# Getting list length
print(f"List length: {len(colors)}")

# Index visualization
print(f"\nIndex visualization:")
print(f"Positive: {[i for i in range(len(colors))]}")
print(f"List:     {colors}")
print(f"Negative: {[i-len(colors) for i in range(len(colors))]}")

print("\n" + "=" * 50)
print("4. LIST SLICING")
print("=" * 50)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Original list: {numbers}")

# Basic slicing [start:end]
print(f"numbers[2:6]: {numbers[2:6]}")        # Items 2,3,4,5
print(f"numbers[:4]: {numbers[:4]}")          # First 4 items
print(f"numbers[6:]: {numbers[6:]}")          # From index 6 to end
print(f"numbers[:]: {numbers[:]}")            # Entire list (copy)

# Slicing with step [start:end:step]
print(f"numbers[::2]: {numbers[::2]}")        # Every 2nd element
print(f"numbers[1::2]: {numbers[1::2]}")      # Every 2nd, starting from index 1
print(f"numbers[::3]: {numbers[::3]}")        # Every 3rd element

# Negative slicing
print(f"numbers[-3:]: {numbers[-3:]}")        # Last 3 elements
print(f"numbers[:-2]: {numbers[:-2]}")        # All except last 2
print(f"numbers[-5:-1]: {numbers[-5:-1]}")    # Slice using negative indices

# Reverse slicing
print(f"numbers[::-1]: {numbers[::-1]}")      # Reverse the list
print(f"numbers[8:2:-1]: {numbers[8:2:-1]}")  # Reverse slice from 8 to 2

print("\n" + "=" * 50)
print("5. MODIFYING LISTS")
print("=" * 50)

# Single item assignment
animals = ["cat", "dog", "bird", "fish"]
print(f"Original: {animals}")

animals[1] = "rabbit"
print(f"After changing index 1: {animals}")

# Multiple items assignment (slice assignment)
animals[1:3] = ["hamster", "turtle", "snake"]
print(f"After slice assignment: {animals}")

# Insert items with slice assignment
animals[2:2] = ["lizard", "frog"]  # Insert at index 2
print(f"After inserting at index 2: {animals}")

# Delete items with slice assignment
animals[1:4] = []  # Delete items from index 1 to 3
print(f"After deleting slice: {animals}")

print("\n" + "=" * 50)
print("6. LIST METHODS - ADDING ELEMENTS")
print("=" * 50)

# append() - add single item to end
fruits = ["apple", "banana"]
print(f"Original: {fruits}")

fruits.append("orange")
print(f"After append('orange'): {fruits}")

fruits.append(["grape", "kiwi"])  # Adds the entire list as one element
print(f"After append(['grape', 'kiwi']): {fruits}")

# insert() - add item at specific position
fruits = ["apple", "banana", "orange"]
print(f"\nOriginal: {fruits}")

fruits.insert(1, "mango")
print(f"After insert(1, 'mango'): {fruits}")

fruits.insert(0, "strawberry")
print(f"After insert(0, 'strawberry'): {fruits}")

# extend() - add multiple items to end
fruits = ["apple", "banana"]
print(f"\nOriginal: {fruits}")

fruits.extend(["orange", "grape"])
print(f"After extend(['orange', 'grape']): {fruits}")

fruits.extend("kiwi")  # Extends with each character
print(f"After extend('kiwi'): {fruits}")

print("\n" + "=" * 50)
print("7. LIST METHODS - REMOVING ELEMENTS")
print("=" * 50)

# remove() - remove first occurrence of value
numbers = [1, 2, 3, 2, 4, 2, 5]
print(f"Original: {numbers}")

numbers.remove(2)
print(f"After remove(2): {numbers}")  # Only first 2 is removed

# pop() - remove and return item at index (default: last)
fruits = ["apple", "banana", "orange", "grape"]
print(f"\nOriginal: {fruits}")

removed_fruit = fruits.pop()
print(f"Popped item: '{removed_fruit}', List now: {fruits}")

removed_fruit = fruits.pop(1)
print(f"Popped index 1: '{removed_fruit}', List now: {fruits}")

# clear() - remove all items
numbers = [1, 2, 3, 4, 5]
print(f"\nBefore clear(): {numbers}")
numbers.clear()
print(f"After clear(): {numbers}")

# del statement - remove items or slices
colors = ["red", "green", "blue", "yellow", "purple"]
print(f"\nOriginal: {colors}")

del colors[1]
print(f"After del colors[1]: {colors}")

del colors[1:3]
print(f"After del colors[1:3]: {colors}")

print("\n" + "=" * 50)
print("8. LIST METHODS - FINDING AND COUNTING")
print("=" * 50)

# index() - find first occurrence index
fruits = ["apple", "banana", "orange", "banana", "grape"]
print(f"List: {fruits}")

banana_index = fruits.index("banana")
print(f"Index of 'banana': {banana_index}")

# index() with start and end parameters
banana_index = fruits.index("banana", 2)  # Search starting from index 2
print(f"Index of 'banana' after position 2: {banana_index}")

# count() - count occurrences
numbers = [1, 2, 3, 2, 4, 2, 5, 2]
print(f"\nList: {numbers}")

count_2 = numbers.count(2)
print(f"Count of 2: {count_2}")

count_6 = numbers.count(6)
print(f"Count of 6: {count_6}")

# Checking if item exists
print(f"Is 3 in list? {3 in numbers}")
print(f"Is 10 in list? {10 in numbers}")

print("\n" + "=" * 50)
print("9. LIST METHODS - SORTING AND REVERSING")
print("=" * 50)

# sort() - sort list in place
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"Original: {numbers}")

numbers.sort()
print(f"After sort(): {numbers}")

# sort() with reverse parameter
numbers.sort(reverse=True)
print(f"After sort(reverse=True): {numbers}")

# sorted() - return new sorted list (doesn't modify original)
original = [3, 1, 4, 1, 5, 9, 2, 6, 5]
sorted_list = sorted(original)
print(f"\nOriginal: {original}")
print(f"Sorted copy: {sorted_list}")

# Sorting strings
words = ["banana", "apple", "cherry", "date"]
print(f"\nOriginal words: {words}")

words.sort()
print(f"Alphabetical: {words}")

words.sort(key=len)  # Sort by length
print(f"By length: {words}")

# reverse() - reverse list in place
numbers = [1, 2, 3, 4, 5]
print(f"\nOriginal: {numbers}")

numbers.reverse()
print(f"After reverse(): {numbers}")

# reversed() - return reverse iterator
original = [1, 2, 3, 4, 5]
reversed_list = list(reversed(original))
print(f"Original: {original}")
print(f"Reversed copy: {reversed_list}")

print("\n" + "=" * 50)
print("10. LIST COPYING")
print("=" * 50)

# Shallow copy vs reference
original = [1, 2, 3, [4, 5]]
print(f"Original: {original}")

# Reference (not a copy)
reference = original
reference.append(6)
print(f"After modifying reference: {original}")  # Original is also modified

# Shallow copy methods
original = [1, 2, 3, [4, 5]]
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

print(f"\nOriginal: {original}")
print(f"copy(): {copy1}")
print(f"slice [:]: {copy2}")
print(f"list(): {copy3}")

# Modifying shallow copy
copy1.append(6)
print(f"After copy1.append(6):")
print(f"Original: {original}")
print(f"Copy1: {copy1}")

# Nested list issue with shallow copy
copy1[3].append(7)  # Modifying nested list
print(f"After modifying nested list in copy:")
print(f"Original: {original}")  # Also affected!
print(f"Copy1: {copy1}")

print("\n" + "=" * 50)
print("11. LIST COMPREHENSIONS")
print("=" * 50)

# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# List comprehension with condition
evens = [x for x in range(10) if x % 2 == 0]
print(f"Even numbers 0-9: {evens}")

# List comprehension with expression
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Words: {words}")
print(f"Uppercase: {uppercase}")

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(f"Matrix: {matrix}")
print(f"Flattened: {flattened}")

# List comprehension vs traditional loop
print(f"\nTraditional way:")
result = []
for x in range(5):
    result.append(x**2)
print(f"Squares: {result}")

print(f"List comprehension way:")
result = [x**2 for x in range(5)]
print(f"Squares: {result}")

print("\n" + "=" * 50)
print("12. ITERATING THROUGH LISTS")
print("=" * 50)

fruits = ["apple", "banana", "orange"]

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

# Iterating multiple lists with zip()
colors = ["red", "yellow", "orange"]
print(f"\nIterating two lists together:")
for fruit, color in zip(fruits, colors):
    print(f"  {fruit} is {color}")

print("\n" + "=" * 50)
print("13. COMMON LIST OPERATIONS")
print("=" * 50)

# Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"Concatenation: {list1} + {list2} = {combined}")

# Repetition
pattern = [0, 1]
repeated = pattern * 4
print(f"Repetition: {pattern} * 4 = {repeated}")

# Min, max, sum
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"\nNumbers: {numbers}")
print(f"Min: {min(numbers)}")
print(f"Max: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
print(f"Average: {sum(numbers) / len(numbers):.2f}")

# All and any
boolean_list = [True, True, False]
print(f"\nBoolean list: {boolean_list}")
print(f"all(): {all(boolean_list)}")  # True if all are True
print(f"any(): {any(boolean_list)}")  # True if any is True

print("\n" + "=" * 50)
print("14. PRACTICAL EXAMPLES")
print("=" * 50)

print("Example 1: Shopping Cart")
shopping_cart = []

# Adding items
shopping_cart.append(("Apple", 1.50, 3))
shopping_cart.append(("Banana", 0.80, 5))
shopping_cart.append(("Orange", 2.00, 2))

print("Shopping Cart:")
total = 0
for item, price, quantity in shopping_cart:
    subtotal = price * quantity
    total += subtotal
    print(f"  {item}: ${price} � {quantity} = ${subtotal:.2f}")

print(f"Total: ${total:.2f}")

print(f"\nExample 2: Grade Processing")
grades = [85, 92, 78, 96, 88, 79, 94]

# Statistics
print(f"Grades: {grades}")
print(f"Highest: {max(grades)}")
print(f"Lowest: {min(grades)}")
print(f"Average: {sum(grades) / len(grades):.1f}")

# Grade categories
excellent = [g for g in grades if g >= 90]
good = [g for g in grades if 80 <= g < 90]
needs_improvement = [g for g in grades if g < 80]

print(f"Excellent (90+): {excellent}")
print(f"Good (80-89): {good}")
print(f"Needs Improvement (<80): {needs_improvement}")

print(f"\nExample 3: Text Processing")
sentence = "Python programming is fun and powerful"
words = sentence.split()

# Word analysis
word_lengths = [len(word) for word in words]
print(f"Words: {words}")
print(f"Word lengths: {word_lengths}")
print(f"Longest word: {max(words, key=len)}")
print(f"Words with 6+ letters: {[w for w in words if len(w) >= 6]}")

print("\n" + "=" * 50)
print("15. PERFORMANCE TIPS")
print("=" * 50)

import time

# Performance comparison example
def performance_comparison():
    n = 1000
    
    # List - inserting at beginning (slow)
    test_list = []
    start_time = time.time()
    for i in range(n):
        test_list.insert(0, i)
    list_time = time.time() - start_time
    
    # List - appending at end (fast)
    test_list = []
    start_time = time.time()
    for i in range(n):
        test_list.append(i)
    append_time = time.time() - start_time
    
    print(f"Performance comparison ({n} operations):")
    print(f"Insert at beginning: {list_time:.6f} seconds")
    print(f"Append at end: {append_time:.6f} seconds")
    if append_time > 0:
        print(f"Append is {list_time/append_time:.0f}x faster")

performance_comparison()

print(f"\nPerformance Tips:")
print(" Use append() instead of insert(0, item)")
print(" Use list comprehensions for filtering/mapping")
print(" Use extend() instead of multiple append() calls")
print(" Pre-allocate lists if size is known")
print(" Use deque for frequent insertions at both ends")

print("\n" + "=" * 70)
print("PYTHON LISTS SUMMARY")
print("=" * 70)
print(" Ordered, mutable collections")
print(" Support indexing, slicing, and iteration")
print(" Rich set of built-in methods")
print(" Can store any data type")
print(" Dynamic sizing")
print(" List comprehensions for concise operations")
print(" Great for most general-purpose collections")
print("=" * 70)