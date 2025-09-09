# PYTHON DATA TYPES - COMPREHENSIVE EXPLANATION

print("=" * 70)
print("PYTHON DATA TYPES DEMONSTRATION")
print("=" * 70)

print("\n" + "=" * 50)
print("1. TEXT TYPE - STRING (str)")
print("=" * 50)

# String - sequence of characters
text = "Hello, Python!"
multiline = """This is a
multiline string"""

print(f"Single line string: {text}")
print(f"Type: {type(text)}")
print(f"Length: {len(text)}")
print(f"Multiline string: {repr(multiline)}")

# String operations
print(f"Uppercase: {text.upper()}")
print(f"Contains 'Python': {'Python' in text}")

print("\n" + "=" * 50)
print("2. NUMERIC TYPES")
print("=" * 50)

print("2.1 INTEGER (int) - Whole numbers")
integer_num = 42
negative_int = -17
big_int = 123456789012345678901234567890

print(f"Positive integer: {integer_num} (type: {type(integer_num)})")
print(f"Negative integer: {negative_int} (type: {type(negative_int)})")
print(f"Big integer: {big_int}")
print(f"Integer operations: {integer_num} + {negative_int} = {integer_num + negative_int}")

print("\n2.2 FLOAT - Decimal numbers")
float_num = 3.14159
scientific = 2.5e-4  # 0.00025
negative_float = -9.81

print(f"Float number: {float_num} (type: {type(float_num)})")
print(f"Scientific notation: {scientific}")
print(f"Negative float: {negative_float}")
print(f"Float precision: {1/3:.10f}")

print("\n2.3 COMPLEX - Complex numbers")
complex_num = 3 + 4j
complex_num2 = complex(2, -3)

print(f"Complex number: {complex_num} (type: {type(complex_num)})")
print(f"Real part: {complex_num.real}")
print(f"Imaginary part: {complex_num.imag}")
print(f"Another complex: {complex_num2}")
print(f"Complex addition: {complex_num} + {complex_num2} = {complex_num + complex_num2}")

print("\n" + "=" * 50)
print("3. SEQUENCE TYPES")
print("=" * 50)

print("3.1 LIST - Mutable ordered collection")
fruits = ["apple", "banana", "orange"]
mixed_list = [1, "hello", 3.14, True]
nested_list = [[1, 2], [3, 4], [5, 6]]

print(f"Fruits list: {fruits} (type: {type(fruits)})")
print(f"Mixed list: {mixed_list}")
print(f"Nested list: {nested_list}")

# List operations
fruits.append("grape")
print(f"After append: {fruits}")
fruits[1] = "blueberry"
print(f"After modification: {fruits}")
print(f"List length: {len(fruits)}")
print(f"First item: {fruits[0]}")
print(f"Last item: {fruits[-1]}")

print("\n3.2 TUPLE - Immutable ordered collection")
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item_tuple = ("item",)  # Note the comma

print(f"Coordinates: {coordinates} (type: {type(coordinates)})")
print(f"Colors: {colors}")
print(f"Single item tuple: {single_item_tuple}")

# Tuple operations
print(f"First coordinate: {coordinates[0]}")
print(f"Tuple unpacking: x={coordinates[0]}, y={coordinates[1]}")
x, y = coordinates
print(f"Unpacked values: x={x}, y={y}")

# Trying to modify tuple (will cause error if uncommented)
# coordinates[0] = 30  # This would raise TypeError

print("\n3.3 RANGE - Sequence of numbers")
range1 = range(5)           # 0 to 4
range2 = range(2, 10)       # 2 to 9
range3 = range(0, 20, 3)    # 0 to 19, step 3

print(f"Range 0-4: {range1} (type: {type(range1)})")
print(f"Range as list: {list(range1)}")
print(f"Range 2-9: {list(range2)}")
print(f"Range with step: {list(range3)}")

print("\n" + "=" * 50)
print("4. MAPPING TYPE - DICTIONARY (dict)")
print("=" * 50)

# Dictionary - key-value pairs
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}

nested_dict = {
    "user1": {"name": "John", "score": 95},
    "user2": {"name": "Jane", "score": 87}
}

print(f"Person dictionary: {person}")
print(f"Type: {type(person)}")
print(f"Name: {person['name']}")
print(f"Age: {person.get('age')}")
print(f"Keys: {list(person.keys())}")
print(f"Values: {list(person.values())}")

# Dictionary operations
person["email"] = "alice@example.com"
print(f"After adding email: {person}")
person["age"] = 31
print(f"After updating age: {person}")

print(f"Nested dictionary: {nested_dict}")
print(f"John's score: {nested_dict['user1']['score']}")

print("\n" + "=" * 50)
print("5. SET TYPES")
print("=" * 50)

print("5.1 SET - Mutable collection of unique items")
numbers_set = {1, 2, 3, 4, 5}
fruits_set = {"apple", "banana", "orange"}
mixed_set = {1, "hello", 3.14}

print(f"Numbers set: {numbers_set} (type: {type(numbers_set)})")
print(f"Fruits set: {fruits_set}")

# Set operations
numbers_set.add(6)
print(f"After adding 6: {numbers_set}")
numbers_set.add(3)  # Adding duplicate - no effect
print(f"After adding duplicate 3: {numbers_set}")

# Set operations - mathematical
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

print("\n5.2 FROZENSET - Immutable set")
frozen_set = frozenset([1, 2, 3, 4])
print(f"Frozen set: {frozen_set} (type: {type(frozen_set)})")
# frozen_set.add(5)  # This would raise AttributeError

print("\n" + "=" * 50)
print("6. BOOLEAN TYPE (bool)")
print("=" * 50)

bool_true = True
bool_false = False
bool_from_comparison = 10 > 5
bool_from_function = bool("hello")

print(f"Boolean True: {bool_true} (type: {type(bool_true)})")
print(f"Boolean False: {bool_false}")
print(f"From comparison: {bool_from_comparison}")
print(f"From function: {bool_from_function}")

# Truthy and falsy values
print("\nTruthy and Falsy values:")
values_to_test = [True, False, 1, 0, "hello", "", [1], [], None]
for value in values_to_test:
    print(f"bool({repr(value):>10}) = {bool(value)}")

print("\n" + "=" * 50)
print("7. BINARY TYPES")
print("=" * 50)

print("7.1 BYTES - Immutable byte sequence")
bytes_data = b"Hello"
bytes_from_string = "Hello".encode('utf-8')
bytes_from_list = bytes([72, 101, 108, 108, 111])

print(f"Bytes literal: {bytes_data} (type: {type(bytes_data)})")
print(f"From string: {bytes_from_string}")
print(f"From list: {bytes_from_list}")
print(f"Decoded: {bytes_data.decode('utf-8')}")

print("\n7.2 BYTEARRAY - Mutable byte sequence")
byte_array = bytearray(b"Hello")
print(f"Bytearray: {byte_array} (type: {type(byte_array)})")
byte_array[0] = 72  # Modify first byte
print(f"After modification: {byte_array}")

print("\n7.3 MEMORYVIEW - Memory view object")
data = bytearray(b"Hello World")
memory_view = memoryview(data)
print(f"Memory view: {memory_view} (type: {type(memory_view)})")
print(f"Memory view slice: {memory_view[0:5].tobytes()}")

print("\n" + "=" * 50)
print("8. NONE TYPE")
print("=" * 50)

none_value = None
print(f"None value: {none_value} (type: {type(none_value)})")
print(f"None is None: {none_value is None}")
print(f"None == None: {none_value == None}")

# None is often used as default value
def greet(name=None):
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"

print(f"Function with None default: {greet()}")
print(f"Function with name: {greet('Alice')}")

print("\n" + "=" * 50)
print("9. TYPE CHECKING AND CONVERSION")
print("=" * 50)

# Type checking
values = [42, 3.14, "hello", [1, 2, 3], {"key": "value"}, True]
for value in values:
    print(f"{str(value):>15} is type {type(value).__name__}")
    print(f"    isinstance(int): {isinstance(value, int)}")
    print(f"    isinstance(str): {isinstance(value, str)}")

print("\nType Conversions:")
original_int = 42
print(f"Original integer: {original_int}")
print(f"To string: '{str(original_int)}' (type: {type(str(original_int))})")
print(f"To float: {float(original_int)} (type: {type(float(original_int))})")
print(f"To boolean: {bool(original_int)}")

original_string = "123"
print(f"\nOriginal string: '{original_string}'")
print(f"To integer: {int(original_string)}")
print(f"To float: {float(original_string)}")

# Type conversion with lists, tuples, sets
original_list = [1, 2, 3, 2, 1]
print(f"\nOriginal list: {original_list}")
print(f"To tuple: {tuple(original_list)}")
print(f"To set (removes duplicates): {set(original_list)}")

print("\n" + "=" * 50)
print("10. PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Data processing with different types
students_data = [
    {"name": "Alice", "grades": [85, 92, 88], "active": True},
    {"name": "Bob", "grades": [78, 85, 90], "active": True},
    {"name": "Charlie", "grades": [92, 88, 94], "active": False}
]

print("Student Grade Analysis:")
for student in students_data:
    if student["active"]:  # Boolean check
        name = student["name"]  # String
        grades = student["grades"]  # List
        average = sum(grades) / len(grades)  # Float calculation
        print(f"{name}: Average grade = {average:.2f}")

# Example 2: Using different data types together
inventory = {
    "items": ["laptop", "mouse", "keyboard"],  # List
    "prices": (999.99, 25.50, 75.00),        # Tuple
    "in_stock": {True, False, True},           # Set
    "categories": {"electronics": ["laptop", "mouse"], 
                  "accessories": ["keyboard"]}, # Nested dict
    "last_updated": None                       # None
}

print(f"\nInventory Management:")
print(f"Total items: {len(inventory['items'])}")
print(f"Average price: ${sum(inventory['prices']) / len(inventory['prices']):.2f}")
print(f"All in stock: {all(inventory['in_stock'])}")

print("\n" + "=" * 70)
print("DATA TYPES SUMMARY")
print("=" * 70)
print("✓ Text: str - for text data")
print("✓ Numbers: int, float, complex - for mathematical operations")  
print("✓ Sequences: list (mutable), tuple (immutable), range - for ordered data")
print("✓ Mapping: dict - for key-value relationships")
print("✓ Sets: set (mutable), frozenset (immutable) - for unique collections")
print("✓ Boolean: bool - for True/False logic")
print("✓ Binary: bytes, bytearray, memoryview - for binary data")
print("✓ None: NoneType - for representing absence of value")
print("=" * 70)