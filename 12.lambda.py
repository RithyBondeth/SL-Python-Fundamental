# 9. Python Lambda Functions - Complete Guide

# Lambda functions are small, anonymous functions that can have any number of arguments
# but can only have one expression. They are also known as "anonymous functions"
# Syntax: lambda arguments: expression

print("=== PYTHON LAMBDA FUNCTIONS TUTORIAL ===\n")

# 1. BASIC LAMBDA SYNTAX AND COMPARISON WITH REGULAR FUNCTIONS
print("1. Basic Lambda Syntax:")

# Regular function
def add_regular(x, y):
    return x + y

# Lambda function (anonymous)
add_lambda = lambda x, y: x + y

print("Regular function vs Lambda function:")
print(f"Regular function: add_regular(3, 5) = {add_regular(3, 5)}")
print(f"Lambda function: add_lambda(3, 5) = {add_lambda(3, 5)}")

# Lambda without assignment (inline usage)
result = (lambda a, b: a * b)(4, 6)
print(f"Inline lambda: (lambda a, b: a * b)(4, 6) = {result}")
print()

# 2. SINGLE ARGUMENT LAMBDA FUNCTIONS
print("2. Single Argument Lambda Functions:")

# Square function
square = lambda x: x ** 2
print(f"Square of 7: {square(7)}")

# Cube function
cube = lambda x: x ** 3
print(f"Cube of 4: {cube(4)}")

# String operations
uppercase = lambda s: s.upper()
print(f"Uppercase 'hello': {uppercase('hello')}")

# Boolean operations
is_even = lambda n: n % 2 == 0
print(f"Is 8 even? {is_even(8)}")
print(f"Is 9 even? {is_even(9)}")
print()

# 3. MULTIPLE ARGUMENT LAMBDA FUNCTIONS
print("3. Multiple Argument Lambda Functions:")

# Mathematical operations
multiply = lambda x, y: x * y
divide = lambda a, b: a / b if b != 0 else "Cannot divide by zero"
power = lambda base, exp: base ** exp

print(f"Multiply 6 × 7 = {multiply(6, 7)}")
print(f"Divide 15 ÷ 3 = {divide(15, 3)}")
print(f"Power 2³ = {power(2, 3)}")

# String operations
full_name = lambda first, last: f"{first} {last}"
print(f"Full name: {full_name('John', 'Doe')}")

# Conditional lambda
max_value = lambda a, b: a if a > b else b
min_value = lambda a, b: a if a < b else b

print(f"Max of 10, 25: {max_value(10, 25)}")
print(f"Min of 10, 25: {min_value(10, 25)}")
print()

# 4. LAMBDA WITH DEFAULT ARGUMENTS
print("4. Lambda with Default Arguments:")

# Note: Lambda functions can't use default arguments directly
# But we can achieve similar behavior with nested lambdas or wrapper functions

def create_greeter(default_greeting="Hello"):
    return lambda name: f"{default_greeting}, {name}!"

# Create different greeters
hello_greeter = create_greeter()
hi_greeter = create_greeter("Hi")
welcome_greeter = create_greeter("Welcome")

print("Lambda with default-like behavior:")
print(hello_greeter("Alice"))
print(hi_greeter("Bob"))
print(welcome_greeter("Charlie"))
print()

# 5. LAMBDA FUNCTIONS WITH MAP()
print("5. Lambda Functions with map():")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(f"Original numbers: {numbers}")
print(f"Squared numbers: {squared}")

# Convert temperatures from Celsius to Fahrenheit
celsius_temps = [0, 20, 25, 30, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius_temps))
print(f"Celsius: {celsius_temps}")
print(f"Fahrenheit: {fahrenheit}")

# String operations with map
words = ["python", "lambda", "function", "programming"]
capitalized = list(map(lambda word: word.capitalize(), words))
lengths = list(map(lambda word: len(word), words))

print(f"Original words: {words}")
print(f"Capitalized: {capitalized}")
print(f"Word lengths: {lengths}")
print()

# 6. LAMBDA FUNCTIONS WITH FILTER()
print("6. Lambda Functions with filter():")

numbers = list(range(1, 21))  # Numbers 1 to 20

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"All numbers: {numbers}")
print(f"Even numbers: {evens}")

# Filter numbers greater than 10
greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(f"Numbers > 10: {greater_than_10}")

# Filter numbers divisible by 3
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(f"Divisible by 3: {divisible_by_3}")

# Filter strings by length
words = ["cat", "elephant", "dog", "hippopotamus", "bird", "ant"]
long_words = list(filter(lambda word: len(word) > 4, words))
short_words = list(filter(lambda word: len(word) <= 3, words))

print(f"All words: {words}")
print(f"Long words (>4 chars): {long_words}")
print(f"Short words (≤3 chars): {short_words}")
print()

# 7. LAMBDA FUNCTIONS WITH REDUCE()
print("7. Lambda Functions with reduce():")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"Numbers: {numbers}")
print(f"Sum using reduce: {sum_result}")

# Product of all numbers
product_result = reduce(lambda x, y: x * y, numbers)
print(f"Product using reduce: {product_result}")

# Find maximum number
max_result = reduce(lambda x, y: x if x > y else y, numbers)
print(f"Maximum using reduce: {max_result}")

# Concatenate strings
words = ["Python", "is", "awesome", "!"]
sentence = reduce(lambda x, y: x + " " + y, words)
print(f"Words: {words}")
print(f"Sentence: {sentence}")
print()

# 8. LAMBDA FUNCTIONS WITH SORTED()
print("8. Lambda Functions with sorted():")

# Sort by different criteria
students = [
    {"name": "Alice", "age": 23, "grade": 88},
    {"name": "Bob", "age": 20, "grade": 92},
    {"name": "Charlie", "age": 22, "grade": 85},
    {"name": "Diana", "age": 21, "grade": 95}
]

print("Original student data:")
for student in students:
    print(f"  {student}")

# Sort by age
by_age = sorted(students, key=lambda x: x["age"])
print("\nSorted by age:")
for student in by_age:
    print(f"  {student['name']}: {student['age']} years")

# Sort by grade (descending)
by_grade = sorted(students, key=lambda x: x["grade"], reverse=True)
print("\nSorted by grade (highest first):")
for student in by_grade:
    print(f"  {student['name']}: {student['grade']}")

# Sort strings by length
words = ["python", "java", "c", "javascript", "go", "rust"]
by_length = sorted(words, key=lambda word: len(word))
print(f"\nWords sorted by length: {by_length}")

# Sort tuples by second element
points = [(1, 3), (3, 1), (2, 2), (4, 0)]
by_y_coordinate = sorted(points, key=lambda point: point[1])
print(f"Points sorted by Y coordinate: {by_y_coordinate}")
print()

# 9. LAMBDA IN LIST COMPREHENSIONS AND GENERATOR EXPRESSIONS
print("9. Lambda with List Comprehensions:")

# Lambda functions can be used within list comprehensions
numbers = [1, 2, 3, 4, 5]

# Apply lambda function in list comprehension
transformed = [(lambda x: x**2 + 2*x + 1)(n) for n in numbers]
print(f"Transformed using lambda: {transformed}")

# More complex example with conditional lambda
data = [1, -2, 3, -4, 5, -6]
processed = [(lambda x: abs(x) if x < 0 else x**2)(n) for n in data]
print(f"Original data: {data}")
print(f"Processed (abs if negative, square if positive): {processed}")
print()

# 10. LAMBDA FUNCTIONS WITH ANY() AND ALL()
print("10. Lambda Functions with any() and all():")

numbers = [2, 4, 6, 8, 10]
mixed_numbers = [1, 3, 4, 7, 8]

# Check if any number is even
any_even = any(lambda x: x % 2 == 0 for x in numbers)
print(f"Numbers: {numbers}")
print(f"Any even numbers? {any_even}")

# Check if all numbers are even
all_even = all(lambda x: x % 2 == 0 for x in numbers)
print(f"All numbers even? {all_even}")

# Mixed numbers test
any_even_mixed = any(lambda x: x % 2 == 0 for x in mixed_numbers)
all_even_mixed = all(lambda x: x % 2 == 0 for x in mixed_numbers)
print(f"\nMixed numbers: {mixed_numbers}")
print(f"Any even? {any_even_mixed}")
print(f"All even? {all_even_mixed}")

# String validation
emails = ["user@example.com", "test@test.org", "invalid-email"]
all_valid = all(lambda email: "@" in email and "." in email for email in emails)
print(f"\nEmails: {emails}")
print(f"All valid emails? {all_valid}")
print()

# 11. LAMBDA FUNCTIONS IN EVENT-DRIVEN PROGRAMMING SIMULATION
print("11. Lambda in Event-Driven Programming:")

# Simulate event handlers using lambdas
event_handlers = {
    "click": lambda: print("🖱️  Button clicked!"),
    "hover": lambda: print("👆 Mouse hovering!"),
    "keypress": lambda key: print(f"⌨️  Key pressed: {key}"),
    "submit": lambda data: print(f"📤 Form submitted with: {data}")
}

# Simulate events
print("Simulating events with lambda handlers:")
event_handlers["click"]()
event_handlers["hover"]()
event_handlers["keypress"]("Enter")
event_handlers["submit"]({"username": "alice", "email": "alice@example.com"})
print()

# 12. LAMBDA FUNCTIONS FOR QUICK CALCULATIONS
print("12. Lambda for Quick Calculations:")

# Mathematical formulas as lambdas
circle_area = lambda r: 3.14159 * r ** 2
rectangle_area = lambda l, w: l * w
triangle_area = lambda base, height: 0.5 * base * height
sphere_volume = lambda r: (4/3) * 3.14159 * r ** 3

print("Geometric calculations:")
print(f"Circle area (r=5): {circle_area(5):.2f}")
print(f"Rectangle area (10×6): {rectangle_area(10, 6)}")
print(f"Triangle area (base=8, height=6): {triangle_area(8, 6)}")
print(f"Sphere volume (r=3): {sphere_volume(3):.2f}")

# Financial calculations
compound_interest = lambda principal, rate, time: principal * (1 + rate) ** time
simple_interest = lambda principal, rate, time: principal * (1 + rate * time)

print("\nFinancial calculations:")
print(f"Compound interest ($1000, 5%, 3 years): ${compound_interest(1000, 0.05, 3):.2f}")
print(f"Simple interest ($1000, 5%, 3 years): ${simple_interest(1000, 0.05, 3):.2f}")
print()

# 13. LAMBDA WITH CONDITIONAL EXPRESSIONS (TERNARY OPERATOR)
print("13. Lambda with Conditional Expressions:")

# Grade calculator
get_grade = lambda score: "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

scores = [95, 87, 76, 65, 54, 43]
print("Grade calculator using lambda:")
for score in scores:
    print(f"Score {score}: Grade {get_grade(score)}")

# Temperature classifier
temp_category = lambda temp: "Hot" if temp > 30 else "Warm" if temp > 20 else "Cool" if temp > 10 else "Cold"

temperatures = [35, 25, 15, 5, -5]
print("\nTemperature categories:")
for temp in temperatures:
    print(f"{temp}°C: {temp_category(temp)}")

# Age group classifier
age_group = lambda age: "Child" if age < 13 else "Teen" if age < 20 else "Adult" if age < 65 else "Senior"

ages = [8, 16, 25, 45, 70]
print("\nAge groups:")
for age in ages:
    print(f"Age {age}: {age_group(age)}")
print()

# 14. ADVANCED LAMBDA PATTERNS
print("14. Advanced Lambda Patterns:")

# Lambda returning lambda (higher-order functions)
multiplier_factory = lambda n: lambda x: x * n

double = multiplier_factory(2)
triple = multiplier_factory(3)
quadruple = multiplier_factory(4)

print("Lambda factories:")
print(f"Double 7: {double(7)}")
print(f"Triple 7: {triple(7)}")
print(f"Quadruple 7: {quadruple(7)}")

# Partial application simulation
def partial_lambda(func, *partial_args):
    return lambda *remaining_args: func(*(partial_args + remaining_args))

# Create specialized functions
add_10 = partial_lambda(lambda x, y: x + y, 10)
multiply_by_5 = partial_lambda(lambda x, y: x * y, 5)

print(f"Add 10 to 15: {add_10(15)}")
print(f"Multiply 8 by 5: {multiply_by_5(8)}")

# Composition of lambda functions
compose = lambda f, g: lambda x: f(g(x))

square_then_double = compose(lambda x: x * 2, lambda x: x ** 2)
print(f"Square 6 then double: {square_then_double(6)}")  # (6²) × 2 = 72
print()

# 15. LAMBDA LIMITATIONS AND ALTERNATIVES
print("15. Lambda Limitations and When to Use Regular Functions:")

print("Lambda limitations:")
print("• Can only contain expressions, not statements")
print("• Cannot contain multiple lines")
print("• Cannot contain assignments")
print("• Limited debugging capability")
print("• Can be less readable for complex logic")

# Examples of what lambdas CANNOT do:

# ❌ Cannot do this with lambda (multiple statements):
def complex_function(x):
    if x < 0:
        print("Negative number")
        return abs(x)
    else:
        print("Positive or zero")
        return x * 2

# ❌ Cannot do this with lambda (assignments):
def function_with_assignment(items):
    result = []
    for item in items:
        result.append(item * 2)
    return result

# ✅ Good lambda use cases:
good_lambdas = {
    "Simple math": lambda x, y: x + y,
    "Quick filter": lambda x: x > 0,
    "Key function": lambda item: item[1],
    "Simple transform": lambda s: s.upper(),
}

# ❌ Bad lambda use cases (use regular functions instead):
print("\n⚠️  When to avoid lambdas:")
print("• Complex conditional logic")
print("• Multiple operations")
print("• Error handling")
print("• Documentation needed")
print("• Reused in many places")

# Better as regular function:
def calculate_discount(price, customer_type, is_member):
    """Calculate discount based on multiple factors"""
    base_discount = 0.0

    if customer_type == "premium":
        base_discount = 0.15
    elif customer_type == "regular":
        base_discount = 0.05

    if is_member:
        base_discount += 0.10

    return price * (1 - base_discount)

print(f"\nBetter as regular function: ${calculate_discount(100, 'premium', True):.2f}")
print()

print("=== LAMBDA FUNCTIONS TUTORIAL COMPLETE ===")
print("Key takeaways:")
print("• Lambda functions are anonymous, single-expression functions")
print("• Syntax: lambda arguments: expression")
print("• Perfect for short, simple operations")
print("• Commonly used with map(), filter(), reduce(), sorted()")
print("• Great for functional programming patterns")
print("• Can be assigned to variables or used inline")
print("• Support multiple arguments and conditional expressions")
print("• Limited to expressions only (no statements)")
print("• Use regular functions for complex logic")
print("• Excellent for event handlers and callbacks")
print("• Enable concise, readable code for simple operations")