# GETTING STARTED WITH PYTHON - COMPREHENSIVE GUIDE

print("=" * 70)
print("GETTING STARTED WITH PYTHON")
print("=" * 70)

print("\n" + "=" * 50)
print("1. WHAT IS PYTHON?")
print("=" * 50)

print("Python is a high-level, interpreted programming language created by Guido van Rossum")
print("First released: 1991")
print("Philosophy: 'Simple is better than complex'")
print("\nKey Features:")
print("✓ Easy to read and write")
print("✓ Interpreted language (no compilation needed)")
print("✓ Cross-platform (Windows, Mac, Linux)")
print("✓ Large standard library")
print("✓ Huge community and ecosystem")
print("✓ Versatile (web, data science, AI, automation, etc.)")

print("\n" + "=" * 50)
print("2. PYTHON SYNTAX BASICS")
print("=" * 50)

print("Python uses indentation to define code blocks (not braces like other languages)")
print("\nExample of Python's clean syntax:")

# This is a comment
name = "World"
print(f"Hello, {name}!")

# Conditional statement
age = 25
if age >= 18:
    print("You are an adult")
    if age >= 65:
        print("You are a senior")
    else:
        print("You are a working adult")
else:
    print("You are a minor")

# Loop example
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"Count: {i}")

print("\n" + "=" * 50)
print("3. BASIC PYTHON CONCEPTS")
print("=" * 50)

print("3.1 VARIABLES AND DATA TYPES")
print("-" * 30)

# Variables (no declaration needed)
message = "Hello Python!"          # String
number = 42                        # Integer
decimal = 3.14                     # Float
is_learning = True                 # Boolean
shopping_list = ["apple", "banana"] # List
person = {"name": "Alice", "age": 30} # Dictionary

print(f"String: {message}")
print(f"Integer: {number}")
print(f"Float: {decimal}")
print(f"Boolean: {is_learning}")
print(f"List: {shopping_list}")
print(f"Dictionary: {person}")

print("\n3.2 BASIC OPERATIONS")
print("-" * 30)

# Arithmetic operations
a = 10
b = 3
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Floor Division: {a} // {b} = {a // b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Exponent: {a} ** {b} = {a ** b}")

print("\n3.3 STRING OPERATIONS")
print("-" * 30)

first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name
print(f"String concatenation: '{first_name}' + ' ' + '{last_name}' = '{full_name}'")
print(f"String length: len('{full_name}') = {len(full_name)}")
print(f"Uppercase: '{full_name}'.upper() = '{full_name.upper()}'")
print(f"String slicing: '{full_name}'[0:4] = '{full_name[0:4]}'")

print("\n" + "=" * 50)
print("4. CONTROL STRUCTURES")
print("=" * 50)

print("4.1 CONDITIONAL STATEMENTS")
print("-" * 30)

temperature = 25
print(f"Temperature: {temperature}°C")

if temperature > 30:
    weather = "Hot"
elif temperature > 20:
    weather = "Warm"
elif temperature > 10:
    weather = "Cool"
else:
    weather = "Cold"

print(f"Weather condition: {weather}")

print("\n4.2 LOOPS")
print("-" * 30)

# For loop with range
print("For loop with range(5):")
for i in range(5):
    print(f"  Iteration {i}")

# For loop with list
fruits = ["apple", "banana", "orange"]
print(f"\nFor loop with list {fruits}:")
for fruit in fruits:
    print(f"  Fruit: {fruit}")

# While loop
print(f"\nWhile loop (countdown from 3):")
countdown = 3
while countdown > 0:
    print(f"  {countdown}")
    countdown -= 1
print("  Blast off!")

print("\n" + "=" * 50)
print("5. FUNCTIONS")
print("=" * 50)

# Function definition
def greet(name, greeting="Hello"):
    """A simple greeting function with default parameter"""
    return f"{greeting}, {name}!"

# Function calls
print("Function examples:")
print(greet("Alice"))
print(greet("Bob", "Hi"))
print(greet("Charlie", "Good morning"))

# Function with multiple return values
def calculate(x, y):
    """Calculate sum, difference, and product"""
    return x + y, x - y, x * y

sum_result, diff_result, prod_result = calculate(10, 3)
print(f"\nMultiple return values:")
print(f"calculate(10, 3) returns: {sum_result}, {diff_result}, {prod_result}")

print("\n" + "=" * 50)
print("6. DATA STRUCTURES")
print("=" * 50)

print("6.1 LISTS (Mutable, Ordered)")
print("-" * 30)

numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")
numbers.append(6)
print(f"After append(6): {numbers}")
numbers.insert(0, 0)
print(f"After insert(0, 0): {numbers}")
numbers.remove(3)
print(f"After remove(3): {numbers}")

print("\n6.2 DICTIONARIES (Key-Value Pairs)")
print("-" * 30)

student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 90, 88]
}
print(f"Student dictionary: {student}")
print(f"Student name: {student['name']}")
print(f"Average grade: {sum(student['grades']) / len(student['grades'])}")

# Add new key-value pair
student["email"] = "alice@example.com"
print(f"After adding email: {student}")

print("\n6.3 TUPLES (Immutable, Ordered)")
print("-" * 30)

coordinates = (10, 20)
print(f"Coordinates tuple: {coordinates}")
x, y = coordinates  # Tuple unpacking
print(f"Unpacked: x={x}, y={y}")

print("\n" + "=" * 50)
print("7. WORKING WITH FILES")
print("=" * 50)

# Writing to a file
print("Writing to a file:")
filename = "sample.txt"
content = "Hello, this is a sample file created by Python!"

try:
    with open(filename, "w") as file:
        file.write(content)
    print(f"✓ Successfully wrote to '{filename}'")
    
    # Reading from the file
    with open(filename, "r") as file:
        read_content = file.read()
    print(f"✓ File content: '{read_content}'")
    
except Exception as e:
    print(f"✗ Error working with file: {e}")

print("\n" + "=" * 50)
print("8. ERROR HANDLING")
print("=" * 50)

print("Error handling with try-except:")

# Example 1: Division by zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("✗ Cannot divide by zero!")
    result = "undefined"

print(f"Result: {result}")

# Example 2: Invalid type conversion
try:
    number = int("not_a_number")
except ValueError as e:
    print(f"✗ Value error: {e}")
    number = 0

print(f"Number: {number}")

print("\n" + "=" * 50)
print("9. MODULES AND IMPORTS")
print("=" * 50)

# Built-in modules
import math
import random
from datetime import datetime

print("Using built-in modules:")
print(f"math.pi = {math.pi}")
print(f"math.sqrt(16) = {math.sqrt(16)}")
print(f"random.randint(1, 10) = {random.randint(1, 10)}")
print(f"Current time: {datetime.now()}")

# Using specific functions from modules
from math import factorial, pow
print(f"factorial(5) = {factorial(5)}")
print(f"pow(2, 3) = {pow(2, 3)}")

print("\n" + "=" * 50)
print("10. PRACTICAL EXAMPLE - SIMPLE CALCULATOR")
print("=" * 50)

def calculator():
    """A simple calculator function"""
    print("\n=== Simple Calculator ===")
    
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else "Cannot divide by zero"
    }
    
    # Sample calculations
    test_cases = [
        (10, "+", 5),
        (20, "-", 8),
        (6, "*", 7),
        (15, "/", 3),
        (10, "/", 0)  # Division by zero test
    ]
    
    for num1, op, num2 in test_cases:
        if op in operations:
            result = operations[op](num1, num2)
            print(f"{num1} {op} {num2} = {result}")
        else:
            print(f"Unknown operation: {op}")

# Run the calculator
calculator()

print("\n" + "=" * 50)
print("11. PYTHON DEVELOPMENT TIPS")
print("=" * 50)

print("Best Practices for Beginners:")
print("✓ Use meaningful variable names")
print("✓ Write comments to explain your code")
print("✓ Follow PEP 8 style guidelines")
print("✓ Use functions to organize your code")
print("✓ Handle errors gracefully")
print("✓ Test your code with different inputs")

print(f"\nCommon Beginner Mistakes:")
print("✗ Forgetting colons after if/for/while statements")
print("✗ Incorrect indentation")
print("✗ Using = instead of == for comparison")
print("✗ Not closing parentheses or quotes")
print("✗ Mixing tabs and spaces for indentation")

print("\n" + "=" * 50)
print("12. NEXT STEPS IN LEARNING PYTHON")
print("=" * 50)

print("Fundamental Topics to Learn:")
print("1. Object-Oriented Programming (Classes and Objects)")
print("2. List Comprehensions and Generators")
print("3. Decorators and Context Managers")
print("4. Working with APIs and JSON")
print("5. Database connections")
print("6. Web frameworks (Django, Flask)")
print("7. Data analysis (Pandas, NumPy)")
print("8. Machine Learning (Scikit-learn, TensorFlow)")

print("\nPractice Projects:")
print("• Build a to-do list application")
print("• Create a simple web scraper")
print("• Develop a basic game (like Tic-Tac-Toe)")
print("• Build a personal expense tracker")
print("• Create a weather app using APIs")

print("\n" + "=" * 70)
print("GETTING STARTED SUMMARY")
print("=" * 70)
print("✓ Python is beginner-friendly and versatile")
print("✓ No compilation needed - just write and run")
print("✓ Indentation is crucial for code structure")
print("✓ Start with basics: variables, loops, functions")
print("✓ Practice with small projects")
print("✓ Use Python's extensive standard library")
print("✓ Join the Python community for help and resources")
print("✓ Keep practicing and building projects!")
print("=" * 70)

print(f"\n🎉 Congratulations! You've completed the Python getting started guide!")
print(f"💡 Remember: The best way to learn programming is by doing!")
print(f"🚀 Start building your own projects and keep experimenting!")