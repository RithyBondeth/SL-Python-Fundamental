# PYTHON VARIABLES - COMPREHENSIVE EXPLANATION

print("=" * 70)
print("PYTHON VARIABLES DEMONSTRATION")
print("=" * 70)

print("\n" + "=" * 50)
print("1. BASIC VARIABLE CREATION")
print("=" * 50)

# Creating variables - no declaration needed
name = "Alice"
age = 25
height = 5.6
is_student = True

print("Variables created:")
print(f"name = '{name}' (type: {type(name).__name__})")
print(f"age = {age} (type: {type(age).__name__})")
print(f"height = {height} (type: {type(height).__name__})")
print(f"is_student = {is_student} (type: {type(is_student).__name__})")

print("\n" + "=" * 50)
print("2. DYNAMIC TYPING")
print("=" * 50)

# Variables can change type during runtime
variable = "Hello"
print(f"variable = '{variable}' (type: {type(variable).__name__})")

variable = 42
print(f"variable = {variable} (type: {type(variable).__name__})")

variable = [1, 2, 3]
print(f"variable = {variable} (type: {type(variable).__name__})")

variable = {"key": "value"}
print(f"variable = {variable} (type: {type(variable).__name__})")

print("✓ Python variables are dynamically typed!")

print("\n" + "=" * 50)
print("3. VARIABLE NAMING RULES AND CONVENTIONS")
print("=" * 50)

# Valid variable names
first_name = "John"          # Snake case (recommended)
lastName = "Doe"             # Camel case (acceptable)
age2 = 30                    # Numbers allowed (not at start)
_private_var = "hidden"      # Underscore prefix for "private"
__special__ = "magic"        # Double underscores for special methods
CONSTANT_VALUE = 100         # All caps for constants

print("Valid variable names:")
print(f"first_name = '{first_name}'")
print(f"lastName = '{lastName}'")
print(f"age2 = {age2}")
print(f"_private_var = '{_private_var}'")
print(f"__special__ = '{__special__}'")
print(f"CONSTANT_VALUE = {CONSTANT_VALUE}")

# Invalid names (commented to avoid errors)
# 2age = 30           # Can't start with number
# first-name = "Bad"  # No hyphens allowed
# first name = "Bad"  # No spaces allowed
# class = "keyword"   # Can't use reserved keywords

print("\nNaming Rules:")
print("✓ Start with letter or underscore")
print("✓ Can contain letters, numbers, underscores")
print("✗ Can't start with numbers")
print("✗ Can't contain spaces or special characters")
print("✗ Can't use Python keywords")

print("\n" + "=" * 50)
print("4. MULTIPLE VARIABLE ASSIGNMENT")
print("=" * 50)

# Multiple assignment in one line
x, y, z = 1, 2, 3
print(f"Multiple assignment: x={x}, y={y}, z={z}")

# Same value to multiple variables
a = b = c = "same value"
print(f"Same value assignment: a='{a}', b='{b}', c='{c}'")

# Unpacking collections
coordinates = (10, 20)
lat, lng = coordinates
print(f"Unpacking tuple: lat={lat}, lng={lng}")

fruits = ["apple", "banana", "orange"]
fruit1, fruit2, fruit3 = fruits
print(f"Unpacking list: {fruit1}, {fruit2}, {fruit3}")

# Swapping variables
num1 = 100
num2 = 200
print(f"Before swap: num1={num1}, num2={num2}")
num1, num2 = num2, num1
print(f"After swap: num1={num1}, num2={num2}")

print("\n" + "=" * 50)
print("5. VARIABLE SCOPE")
print("=" * 50)

# Global variable
global_var = "I'm global"

def demonstrate_scope():
    # Declare global variable at the beginning
    global global_var
    
    # Local variable
    local_var = "I'm local"
    
    # Accessing global variable
    print(f"Inside function - global_var: '{global_var}'")
    print(f"Inside function - local_var: '{local_var}'")
    
    # Modifying global variable
    global_var = "Modified global"

print(f"Before function call - global_var: '{global_var}'")
demonstrate_scope()
print(f"After function call - global_var: '{global_var}'")

# Local variable example
def scope_example():
    message = "Local message"
    return message

result = scope_example()
print(f"Returned local variable: '{result}'")
# print(message)  # This would cause NameError

print("\n" + "=" * 50)
print("6. VARIABLE MEMORY AND IDENTITY")
print("=" * 50)

# Variable identity and memory
str1 = "Hello"
str2 = "Hello"
str3 = str1

print("String variables:")
print(f"str1 = '{str1}', id: {id(str1)}")
print(f"str2 = '{str2}', id: {id(str2)}")  
print(f"str3 = '{str3}', id: {id(str3)}")
print(f"str1 is str2: {str1 is str2}")  # True (string interning)
print(f"str1 is str3: {str1 is str3}")  # True

# List variables (different behavior)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\nList variables:")
print(f"list1 = {list1}, id: {id(list1)}")
print(f"list2 = {list2}, id: {id(list2)}")
print(f"list3 = {list3}, id: {id(list3)}")
print(f"list1 is list2: {list1 is list2}")  # False
print(f"list1 is list3: {list1 is list3}")  # True

# Modifying list3 affects list1
list3.append(4)
print(f"After modifying list3: list1 = {list1}")

print("\n" + "=" * 50)
print("7. TYPE CHECKING AND CONVERSION")
print("=" * 50)

# Type checking
value = 42
print(f"value = {value}")
print(f"type(value): {type(value)}")
print(f"isinstance(value, int): {isinstance(value, int)}")
print(f"isinstance(value, str): {isinstance(value, str)}")

# Type conversion (casting)
original_number = 42
string_number = str(original_number)
float_number = float(original_number)
bool_number = bool(original_number)

print(f"\nType conversions from {original_number}:")
print(f"To string: '{string_number}' (type: {type(string_number).__name__})")
print(f"To float: {float_number} (type: {type(float_number).__name__})")
print(f"To boolean: {bool_number} (type: {type(bool_number).__name__})")

# Converting string to number
string_value = "123"
int_value = int(string_value)
float_value = float(string_value)

print(f"\nConversions from '{string_value}':")
print(f"To int: {int_value} (type: {type(int_value).__name__})")
print(f"To float: {float_value} (type: {type(float_value).__name__})")

print("\n" + "=" * 50)
print("8. VARIABLE DELETION")
print("=" * 50)

# Creating and deleting variables
temp_var = "I will be deleted"
print(f"temp_var exists: '{temp_var}'")

del temp_var
print("temp_var has been deleted")

# Checking if variable exists
try:
    print(temp_var)
except NameError:
    print("temp_var no longer exists (NameError)")

print("\n" + "=" * 50)
print("9. CONSTANTS AND CONVENTIONS")
print("=" * 50)

# Python doesn't have true constants, but convention is ALL_CAPS
PI = 3.14159
MAX_SIZE = 1000
DEFAULT_COLOR = "blue"
API_KEY = "secret_key_123"

print("Constants (by convention):")
print(f"PI = {PI}")
print(f"MAX_SIZE = {MAX_SIZE}")
print(f"DEFAULT_COLOR = '{DEFAULT_COLOR}'")
print(f"API_KEY = '{API_KEY}'")

# These are just variables - they can still be changed
PI = 3.14  # Not recommended, but possible
print(f"PI after 'modification': {PI}")

print("\n" + "=" * 50)
print("10. PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: User information
print("Example 1: User Profile")
username = "john_doe"
email = "john@example.com"
login_count = 0
is_premium = False
last_login = None

print(f"Username: {username}")
print(f"Email: {email}")
print(f"Login count: {login_count}")
print(f"Premium user: {is_premium}")
print(f"Last login: {last_login}")

# Simulating user activity
login_count += 1
is_premium = True
last_login = "2024-01-15"

print(f"\nAfter user activity:")
print(f"Login count: {login_count}")
print(f"Premium user: {is_premium}")
print(f"Last login: {last_login}")

# Example 2: Shopping cart
print(f"\nExample 2: Shopping Cart")
items = []
total_price = 0.0
discount_rate = 0.1
is_checkout_complete = False

# Adding items
items.append({"name": "Laptop", "price": 999.99})
items.append({"name": "Mouse", "price": 25.50})

# Calculate total
for item in items:
    total_price += item["price"]

# Apply discount
discounted_price = total_price * (1 - discount_rate)

print(f"Items in cart: {len(items)}")
print(f"Subtotal: ${total_price:.2f}")
print(f"Discount ({discount_rate*100}%): ${total_price - discounted_price:.2f}")
print(f"Final total: ${discounted_price:.2f}")
print(f"Checkout complete: {is_checkout_complete}")

print("\n" + "=" * 50)
print("11. COMMON VARIABLE MISTAKES")
print("=" * 50)

print("Common mistakes to avoid:")
print("✗ Using reserved keywords as variable names")
print("✗ Starting variable names with numbers")
print("✗ Using spaces or special characters in names")
print("✗ Not following naming conventions")
print("✗ Creating variables with unclear names")

print("\nGood practices:")
print("✓ Use descriptive variable names")
print("✓ Follow snake_case convention")
print("✓ Use ALL_CAPS for constants")
print("✓ Initialize variables before using them")
print("✓ Be consistent with naming patterns")

# Example of good vs bad variable names
print(f"\nNaming examples:")

# Bad names
d = "2024-01-15"
x = 25
temp = True

# Good names  
birth_date = "2024-01-15"
user_age = 25
is_active = True

print("Bad names: d, x, temp")
print("Good names: birth_date, user_age, is_active")

print("\n" + "=" * 70)
print("VARIABLES SUMMARY")
print("=" * 70)
print("✓ Variables are containers for data")
print("✓ No explicit type declaration needed")
print("✓ Dynamic typing - types can change")
print("✓ Use descriptive names with snake_case")
print("✓ Variables have scope (global vs local)")
print("✓ Use ALL_CAPS for constants")
print("✓ Can assign multiple variables at once")
print("✓ Variables reference objects in memory")
print("=" * 70)