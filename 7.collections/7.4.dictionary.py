# Python Dictionaries - Complete Guide
# Dictionaries are ordered collections of key-value pairs

print("=" * 50)
print("PYTHON DICTIONARIES - COMPREHENSIVE GUIDE")
print("=" * 50)

# 1. CREATING DICTIONARIES
print("\n1. CREATING DICTIONARIES")
print("-" * 25)

# Empty dictionary
empty_dict = {}
empty_dict2 = dict()
print(f"Empty dict: {empty_dict}")
print(f"Empty dict (using dict()): {empty_dict2}")

# Dictionary with initial values
student = {"name": "Alice", "age": 25, "grade": "A"}
print(f"Student dict: {student}")

# Using dict() constructor
person = dict(name="Bob", age=30, city="New York")
print(f"Person dict: {person}")

# From list of tuples
pairs = [("apple", 5), ("banana", 3), ("cherry", 8)]
fruit_prices = dict(pairs)
print(f"From tuples: {fruit_prices}")

# Mixed data types
mixed_dict = {
    "string": "hello",
    "number": 42,
    "list": [1, 2, 3],
    "nested": {"a": 1, "b": 2}
}
print(f"Mixed types: {mixed_dict}")

# 2. DICTIONARY CHARACTERISTICS
print("\n2. DICTIONARY CHARACTERISTICS")
print("-" * 30)

print("• Ordered: Maintains insertion order (Python 3.7+)")
print("• Mutable: Can add/modify/remove items")
print("• Key-Value pairs: Each item has a key and value")
print("• Unique keys: No duplicate keys allowed")
print("• Keys must be immutable: strings, numbers, tuples")

# Demonstrating key uniqueness
duplicate_keys = {"a": 1, "b": 2, "a": 3}  # Last value wins
print(f"Duplicate keys: {duplicate_keys}")

# 3. ACCESSING DICTIONARY ELEMENTS
print("\n3. ACCESSING DICTIONARY ELEMENTS")
print("-" * 33)

colors = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
print(f"Colors dict: {colors}")

# Access by key
print(f"Red color: {colors['red']}")

# Using get() method (safer)
print(f"Green color: {colors.get('green')}")
print(f"Purple color: {colors.get('purple', 'Not found')}")

# Check if key exists
print(f"'red' in dict: {'red' in colors}")
print(f"'purple' in dict: {'purple' in colors}")

# Get all keys, values, items
print(f"Keys: {list(colors.keys())}")
print(f"Values: {list(colors.values())}")
print(f"Items: {list(colors.items())}")

# 4. MODIFYING DICTIONARIES
print("\n4. MODIFYING DICTIONARIES")
print("-" * 26)

inventory = {"apples": 50, "bananas": 30}
print(f"Original: {inventory}")

# Add new item
inventory["oranges"] = 25
print(f"After adding oranges: {inventory}")

# Modify existing item
inventory["apples"] = 60
print(f"After modifying apples: {inventory}")

# Update multiple items
inventory.update({"bananas": 35, "grapes": 20})
print(f"After update: {inventory}")

# Update with another dict
more_fruits = {"kiwi": 15, "mango": 10}
inventory.update(more_fruits)
print(f"After updating with dict: {inventory}")

# 5. REMOVING ELEMENTS
print("\n5. REMOVING ELEMENTS")
print("-" * 22)

books = {
    "Python": 29.99,
    "Java": 39.99,
    "C++": 34.99,
    "JavaScript": 24.99
}
print(f"Original: {books}")

# Remove specific key-value pair
removed_value = books.pop("Java")
print(f"Removed 'Java': {removed_value}")
print(f"After pop: {books}")

# Remove with default value
removed = books.pop("Ruby", "Not found")
print(f"Tried to remove 'Ruby': {removed}")

# Remove last inserted item
last_item = books.popitem()
print(f"Removed last item: {last_item}")
print(f"After popitem: {books}")

# Delete using del
del books["C++"]
print(f"After del: {books}")

# Clear all items
temp_dict = {"a": 1, "b": 2}
print(f"Before clear: {temp_dict}")
temp_dict.clear()
print(f"After clear: {temp_dict}")

# 6. DICTIONARY METHODS
print("\n6. DICTIONARY METHODS")
print("-" * 21)

scores = {"Alice": 95, "Bob": 87, "Carol": 92}
print(f"Scores: {scores}")

# copy() - shallow copy
scores_copy = scores.copy()
print(f"Copy: {scores_copy}")

# fromkeys() - create dict with same values
subjects = ["Math", "Science", "English"]
default_scores = dict.fromkeys(subjects, 0)
print(f"Default scores: {default_scores}")

# setdefault() - get value or set default
scores.setdefault("David", 0)
print(f"After setdefault: {scores}")

# 7. ITERATING THROUGH DICTIONARIES
print("\n7. ITERATING THROUGH DICTIONARIES")
print("-" * 35)

animals = {"cat": "meow", "dog": "woof", "cow": "moo"}
print(f"Animals: {animals}")

# Iterate over keys
print("Keys:")
for animal in animals:
    print(f"  {animal}")

# Iterate over values
print("Values:")
for sound in animals.values():
    print(f"  {sound}")

# Iterate over key-value pairs
print("Key-Value pairs:")
for animal, sound in animals.items():
    print(f"  {animal}: {sound}")

# 8. DICTIONARY COMPREHENSIONS
print("\n8. DICTIONARY COMPREHENSIONS")
print("-" * 28)

# Basic comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

# With condition
even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
print(f"Even squares: {even_squares}")

# From existing dict
temps_celsius = {"London": 15, "Paris": 18, "Tokyo": 22}
temps_fahrenheit = {city: (temp * 9/5) + 32 for city, temp in temps_celsius.items()}
print(f"Celsius: {temps_celsius}")
print(f"Fahrenheit: {temps_fahrenheit}")

# String manipulation
sentence = "hello world"
char_count = {char: sentence.count(char) for char in set(sentence) if char != ' '}
print(f"Character count in '{sentence}': {char_count}")

# 9. NESTED DICTIONARIES
print("\n9. NESTED DICTIONARIES")
print("-" * 23)

# Dictionary of dictionaries
employees = {
    "emp001": {
        "name": "Alice Johnson",
        "department": "Engineering",
        "salary": 75000,
        "skills": ["Python", "JavaScript", "SQL"]
    },
    "emp002": {
        "name": "Bob Smith",
        "department": "Marketing",
        "salary": 65000,
        "skills": ["SEO", "Content Writing", "Analytics"]
    }
}

print("Employees database:")
for emp_id, details in employees.items():
    print(f"  {emp_id}: {details['name']} - {details['department']}")

# Accessing nested values
print(f"Alice's salary: ${employees['emp001']['salary']:,}")
print(f"Bob's skills: {employees['emp002']['skills']}")

# Modifying nested values
employees["emp001"]["salary"] = 80000
print(f"Alice's new salary: ${employees['emp001']['salary']:,}")

# 10. DICTIONARY WITH LISTS/SETS
print("\n10. DICTIONARIES WITH COLLECTIONS")
print("-" * 33)

# Dictionary with lists as values
student_grades = {
    "Alice": [95, 87, 92, 88],
    "Bob": [78, 85, 90, 82],
    "Carol": [88, 91, 89, 93]
}

print("Student grades:")
for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    print(f"  {student}: {grades} (Average: {average:.1f})")

# Dictionary with sets as values
word_letters = {}
words = ["hello", "world", "python"]
for word in words:
    word_letters[word] = set(word)

print(f"\nWord letters: {word_letters}")

# 11. PRACTICAL EXAMPLES
print("\n11. PRACTICAL EXAMPLES")
print("-" * 24)

# Word frequency counter
def count_words(text):
    words = text.lower().split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

text = "python is great python is powerful python is fun"
word_freq = count_words(text)
print(f"Word frequency: {word_freq}")

# Group items by category
products = [
    {"name": "iPhone", "category": "Electronics", "price": 999},
    {"name": "Shirt", "category": "Clothing", "price": 29},
    {"name": "iPad", "category": "Electronics", "price": 799},
    {"name": "Jeans", "category": "Clothing", "price": 59}
]

grouped = {}
for product in products:
    category = product["category"]
    if category not in grouped:
        grouped[category] = []
    grouped[category].append(product["name"])

print(f"Grouped products: {grouped}")

# Configuration settings
config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "api": {
        "base_url": "https://api.example.com",
        "timeout": 30,
        "retries": 3
    },
    "features": {
        "debug": True,
        "logging": True,
        "cache": False
    }
}

print(f"Database host: {config['database']['host']}")
print(f"API timeout: {config['api']['timeout']} seconds")

# 12. DICTIONARY SORTING
print("\n12. DICTIONARY SORTING")
print("-" * 23)

grades = {"Alice": 95, "David": 78, "Carol": 92, "Bob": 87}
print(f"Original: {grades}")

# Sort by keys
sorted_by_keys = dict(sorted(grades.items()))
print(f"Sorted by keys: {sorted_by_keys}")

# Sort by values
sorted_by_values = dict(sorted(grades.items(), key=lambda item: item[1]))
print(f"Sorted by values: {sorted_by_values}")

# Sort by values (descending)
sorted_desc = dict(sorted(grades.items(), key=lambda item: item[1], reverse=True))
print(f"Sorted descending: {sorted_desc}")

# 13. MERGING DICTIONARIES
print("\n13. MERGING DICTIONARIES")
print("-" * 26)

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"b": 5, "e": 6}  # Note: 'b' conflicts with dict1

print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")
print(f"Dict3: {dict3}")

# Using update()
merged1 = dict1.copy()
merged1.update(dict2)
print(f"Dict1 + Dict2: {merged1}")

# Using ** operator (Python 3.5+)
merged2 = {**dict1, **dict2, **dict3}
print(f"Merged all (** operator): {merged2}")

# Using | operator (Python 3.9+)
try:
    merged3 = dict1 | dict2 | dict3
    print(f"Merged all (| operator): {merged3}")
except TypeError:
    print("| operator not available (Python < 3.9)")

# 14. DEFAULT DICTIONARIES
print("\n14. DEFAULT DICTIONARIES")
print("-" * 26)

from collections import defaultdict

# Regular dict - KeyError if key doesn't exist
regular_dict = {}
# regular_dict['missing_key'] += 1  # This would raise KeyError

# defaultdict - provides default value
dd_int = defaultdict(int)  # Default value: 0
dd_list = defaultdict(list)  # Default value: []

# Count characters using defaultdict
text = "programming"
char_count = defaultdict(int)
for char in text:
    char_count[char] += 1

print(f"Character count with defaultdict: {dict(char_count)}")

# Group by first letter
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
grouped_words = defaultdict(list)
for word in words:
    grouped_words[word[0]].append(word)

print(f"Grouped by first letter: {dict(grouped_words)}")

# 15. ORDERED DICT (for Python < 3.7 compatibility)
print("\n15. ORDERED DICT")
print("-" * 18)

from collections import OrderedDict

# Regular dict (ordered in Python 3.7+)
regular = {"first": 1, "second": 2, "third": 3}
print(f"Regular dict: {regular}")

# OrderedDict (explicitly ordered)
ordered = OrderedDict([("first", 1), ("second", 2), ("third", 3)])
print(f"OrderedDict: {ordered}")

# Move to end
ordered.move_to_end("first")
print(f"After move_to_end('first'): {ordered}")

# 16. PERFORMANCE TIPS
print("\n16. PERFORMANCE TIPS")
print("-" * 20)

import time

# Fast lookup demonstration
large_list = [(i, f"value_{i}") for i in range(100000)]
large_dict = dict(large_list)

# Search in list of tuples
start_time = time.time()
result = None
for key, value in large_list:
    if key == 99999:
        result = value
        break
list_time = time.time() - start_time

# Search in dictionary
start_time = time.time()
result = large_dict.get(99999)
dict_time = time.time() - start_time

print(f"Lookup performance (key=99999):")
print(f"  List search: {list_time:.8f} seconds")
print(f"  Dict lookup: {dict_time:.8f} seconds")
print(f"  Dict is ~{list_time/dict_time:.0f}x faster")

# 17. DICTIONARY METHODS SUMMARY
print("\n17. DICTIONARY METHODS SUMMARY")
print("-" * 31)

methods_info = [
    ("get(key, default)", "Get value with optional default"),
    ("keys()", "Get all keys"),
    ("values()", "Get all values"),
    ("items()", "Get key-value pairs"),
    ("pop(key, default)", "Remove and return value"),
    ("popitem()", "Remove and return last item"),
    ("update(other)", "Update with another dict"),
    ("setdefault(key, default)", "Get or set default value"),
    ("clear()", "Remove all items"),
    ("copy()", "Create shallow copy"),
    ("fromkeys(keys, value)", "Create dict from keys")
]

for method, description in methods_info:
    print(f"  {method:<25} - {description}")

print("\n" + "=" * 50)
print("Dictionaries are perfect for:")
print("• Fast key-based lookups")
print("• Storing structured data")
print("• Counting and frequency analysis")
print("• Caching and memoization")
print("• Configuration settings")
print("• Database-like operations")
print("=" * 50)