# 7. Python Functions - Complete Guide

# Functions are reusable blocks of code that perform specific tasks
# They help organize code, avoid repetition, and make programs more readable

print("=== PYTHON FUNCTIONS TUTORIAL ===\n")

# 1. BASIC FUNCTION DEFINITION AND CALLING
print("1. Basic Function Definition:")

def greet():
    """A simple function that prints a greeting"""
    print("Hello, World!")

# Calling the function
greet()
print()

# 2. FUNCTIONS WITH PARAMETERS
print("2. Functions with Parameters:")

def greet_person(name):
    """Function with one parameter"""
    print(f"Hello, {name}!")

def add_numbers(a, b):
    """Function with multiple parameters"""
    result = a + b
    print(f"{a} + {b} = {result}")

greet_person("Alice")
greet_person("Bob")
add_numbers(5, 3)
add_numbers(10, 20)
print()

# 3. FUNCTIONS WITH RETURN VALUES
print("3. Functions with Return Values:")

def multiply(x, y):
    """Function that returns a value"""
    return x * y

def calculate_area(length, width):
    """Function that calculates and returns rectangle area"""
    area = length * width
    return area

# Using returned values
product = multiply(4, 7)
print(f"4 × 7 = {product}")

rectangle_area = calculate_area(5, 8)
print(f"Rectangle area (5×8) = {rectangle_area}")
print()

# 4. DEFAULT PARAMETERS
print("4. Default Parameters:")

def introduce(name, age=25, city="Unknown"):
    """Function with default parameter values"""
    print(f"Name: {name}, Age: {age}, City: {city}")

# Different ways to call with defaults
introduce("John")  # Uses defaults for age and city
introduce("Sarah", 30)  # Uses default for city only
introduce("Mike", 35, "New York")  # No defaults used
introduce("Lisa", city="Boston")  # Keyword argument, age uses default
print()

# 5. KEYWORD ARGUMENTS
print("5. Keyword Arguments:")

def create_profile(name, age, profession, married=False):
    """Function demonstrating keyword arguments"""
    print(f"Profile: {name}, {age} years old, {profession}")
    print(f"Married: {married}")

# Using keyword arguments (order doesn't matter)
create_profile(age=28, name="Emma", profession="Engineer")
create_profile(name="David", profession="Teacher", age=45, married=True)
print()

# 6. VARIABLE-LENGTH ARGUMENTS (*args)
print("6. Variable-Length Arguments (*args):")

def sum_all(*numbers):
    """Function that accepts any number of arguments"""
    total = sum(numbers)
    print(f"Numbers: {numbers}")
    print(f"Sum: {total}")
    return total

sum_all(1, 2, 3)
sum_all(10, 20, 30, 40, 50)
sum_all(1)  # Single argument
print()

# 7. KEYWORD VARIABLE-LENGTH ARGUMENTS (**kwargs)
print("7. Keyword Variable-Length Arguments (**kwargs):")

def create_student(**details):
    """Function that accepts any number of keyword arguments"""
    print("Student Details:")
    for key, value in details.items():
        print(f"  {key}: {value}")

create_student(name="Alice", grade="A", subject="Math", age=16)
create_student(name="Bob", grade="B+", school="High School")
print()

# 8. COMBINING *args AND **kwargs
print("8. Combining *args and **kwargs:")

def flexible_function(required_param, *args, **kwargs):
    """Function combining required, *args, and **kwargs"""
    print(f"Required parameter: {required_param}")
    print(f"Additional arguments: {args}")
    print(f"Keyword arguments: {kwargs}")

flexible_function("Hello", 1, 2, 3, name="John", age=30)
print()

# 9. LOCAL AND GLOBAL VARIABLES
print("9. Variable Scope (Local vs Global):")

global_var = "I'm global"

def scope_demo():
    """Demonstrates local and global scope"""
    local_var = "I'm local"
    print(f"Inside function - Global: {global_var}")
    print(f"Inside function - Local: {local_var}")

def modify_global():
    """Function that modifies global variable"""
    global global_var
    global_var = "Modified global"
    print(f"Global variable modified to: {global_var}")

scope_demo()
print(f"Outside function - Global: {global_var}")
modify_global()
print(f"After modification - Global: {global_var}")
print()

# 10. LAMBDA FUNCTIONS (Anonymous Functions)
print("10. Lambda Functions:")

# Basic lambda function
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Lambda with multiple parameters
add = lambda a, b: a + b
print(f"3 + 7 = {add(3, 7)}")

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared_numbers}")

# Filter with lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")
print()

# 11. RECURSIVE FUNCTIONS
print("11. Recursive Functions:")

def factorial(n):
    """Calculate factorial using recursion"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def fibonacci(n):
    """Calculate Fibonacci number using recursion"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(f"Factorial of 5: {factorial(5)}")
print(f"Fibonacci sequence (first 8 numbers):")
for i in range(8):
    print(f"F({i}) = {fibonacci(i)}")
print()

# 12. FUNCTION DOCUMENTATION AND ANNOTATIONS
print("12. Function Documentation and Type Annotations:")

def calculate_bmi(weight: float, height: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters

    Returns:
        float: BMI value

    Example:
        >>> calculate_bmi(70, 1.75)
        22.86
    """
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Using the documented function
person_bmi = calculate_bmi(70.0, 1.75)
print(f"BMI: {person_bmi}")

# Accessing function documentation
print(f"Function docstring: {calculate_bmi.__doc__}")
print()

# 13. HIGHER-ORDER FUNCTIONS
print("13. Higher-Order Functions:")

def apply_operation(numbers, operation):
    """Apply an operation function to a list of numbers"""
    return [operation(num) for num in numbers]

def double(x):
    return x * 2

def cube(x):
    return x ** 3

numbers = [1, 2, 3, 4, 5]
doubled = apply_operation(numbers, double)
cubed = apply_operation(numbers, cube)

print(f"Original: {numbers}")
print(f"Doubled: {doubled}")
print(f"Cubed: {cubed}")
print()

# 14. FUNCTION AS RETURN VALUE
print("14. Functions Returning Functions:")

def create_multiplier(factor):
    """Create a function that multiplies by a given factor"""
    def multiplier(x):
        return x * factor
    return multiplier

# Create specific multiplier functions
double_func = create_multiplier(2)
triple_func = create_multiplier(3)

print(f"Double 10: {double_func(10)}")
print(f"Triple 10: {triple_func(10)}")
print()

# 15. PRACTICAL EXAMPLES
print("15. Practical Function Examples:")

def validate_email(email):
    """Simple email validation"""
    return "@" in email and "." in email

def format_currency(amount, currency="USD"):
    """Format amount as currency"""
    return f"{currency} ${amount:.2f}"

def get_grade(score):
    """Convert numeric score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# Using practical functions
emails = ["user@example.com", "invalid-email", "another@test.org"]
for email in emails:
    print(f"{email}: {'Valid' if validate_email(email) else 'Invalid'}")

print(f"Price: {format_currency(99.99)}")
print(f"Price in EUR: {format_currency(99.99, 'EUR')}")

scores = [95, 87, 76, 65, 54]
for score in scores:
    print(f"Score {score}: Grade {get_grade(score)}")

print("\n=== FUNCTION TUTORIAL COMPLETE ===")
print("Key takeaways:")
print("• Functions organize code into reusable blocks")
print("• Use parameters to pass data into functions")
print("• Use return statements to get data out of functions")
print("• Default parameters provide flexibility")
print("• *args and **kwargs handle variable arguments")
print("• Lambda functions are useful for short, simple operations")
print("• Docstrings document what functions do")
print("• Functions can call themselves (recursion)")
print("• Functions are first-class objects in Python")