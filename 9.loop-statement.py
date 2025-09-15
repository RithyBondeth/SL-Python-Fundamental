# 9. Loop Statements in Python
# Loops allow you to execute a block of code repeatedly

print("=== LOOP STATEMENTS IN PYTHON ===\n")

# 1. FOR LOOPS
print("1. For Loops:")

# Basic for loop with range
print("Counting from 0 to 4:")
for i in range(5):
    print(f"Count: {i}")

print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"Number: {i}")

print("\nCounting by 2s from 0 to 10:")
for i in range(0, 11, 2):
    print(f"Even number: {i}")

print()

# For loop with strings
print("2. For Loops with Strings:")
word = "Python"
print(f"Letters in '{word}':")
for letter in word:
    print(f"Letter: {letter}")

print()

# For loop with lists
print("3. For Loops with Lists:")
fruits = ["apple", "banana", "orange", "grape"]
print("Fruits in the list:")
for fruit in fruits:
    print(f"Fruit: {fruit}")

print("\nFruits with index:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

print()

# For loop with dictionaries
print("4. For Loops with Dictionaries:")
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78, "Diana": 96}

print("Student names:")
for name in student_grades:
    print(f"Student: {name}")

print("\nStudent names and grades:")
for name, grade in student_grades.items():
    print(f"{name}: {grade}")

print("\nJust the grades:")
for grade in student_grades.values():
    print(f"Grade: {grade}")

print()

# 5. WHILE LOOPS
print("5. While Loops:")

# Basic while loop
count = 0
print("Counting with while loop:")
while count < 5:
    print(f"Count: {count}")
    count += 1

print()

# While loop with user input simulation
print("While loop with condition:")
number = 1
total = 0
while number <= 10:
    total += number
    print(f"Adding {number}, total so far: {total}")
    number += 1
print(f"Final total: {total}")

print()

# While loop with complex condition
print("While loop with multiple conditions:")
attempts = 0
success = False
max_attempts = 3

while attempts < max_attempts and not success:
    attempts += 1
    print(f"Attempt {attempts}")
    # Simulate success on attempt 2
    if attempts == 2:
        success = True
        print("Success!")
    else:
        print("Failed, trying again...")

print()

# 6. BREAK STATEMENT
print("6. Break Statement:")

print("Finding first even number greater than 10:")
for num in range(1, 100):
    if num > 10 and num % 2 == 0:
        print(f"Found: {num}")
        break
    print(f"Checking: {num}")

print()

print("Break in while loop:")
counter = 0
while True:  # Infinite loop
    counter += 1
    print(f"Counter: {counter}")
    if counter >= 3:
        print("Breaking out of loop")
        break

print()

# 7. CONTINUE STATEMENT
print("7. Continue Statement:")

print("Printing only odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:  # If even, skip
        continue
    print(f"Odd number: {num}")

print()

print("Continue in while loop:")
num = 0
while num < 10:
    num += 1
    if num % 3 == 0:  # Skip multiples of 3
        continue
    print(f"Not divisible by 3: {num}")

print()

# 8. NESTED LOOPS
print("8. Nested Loops:")

print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()  # Empty line after each row

print("Pattern with nested loops:")
for row in range(5):
    for col in range(row + 1):
        print("*", end=" ")
    print()  # New line after each row

print()

# 9. LOOP WITH ELSE
print("9. Loop with Else:")

print("For loop with else (completes normally):")
for i in range(3):
    print(f"Loop iteration: {i}")
else:
    print("For loop completed normally")

print()

print("For loop with else (breaks early):")
for i in range(10):
    print(f"Checking: {i}")
    if i == 2:
        print("Found target, breaking")
        break
else:
    print("This won't print because loop was broken")

print()

print("While loop with else:")
count = 0
while count < 3:
    print(f"While count: {count}")
    count += 1
else:
    print("While loop completed normally")

print()

# 10. LIST COMPREHENSIONS
print("10. List Comprehensions:")

# Basic list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
print(f"Numbers: {numbers}")
print(f"Squares: {squares}")

# List comprehension with condition
even_squares = [x**2 for x in numbers if x % 2 == 0]
print(f"Even squares: {even_squares}")

# List comprehension with range
cubes = [x**3 for x in range(1, 6)]
print(f"Cubes: {cubes}")

# List comprehension with strings
words = ["hello", "world", "python", "programming"]
uppercase_words = [word.upper() for word in words]
print(f"Uppercase: {uppercase_words}")

# List comprehension with conditional expression
numbers = [-2, -1, 0, 1, 2]
abs_numbers = [x if x >= 0 else -x for x in numbers]
print(f"Absolute values: {abs_numbers}")

print()

# 11. OTHER COMPREHENSIONS
print("11. Other Comprehensions:")

# Dictionary comprehension
numbers = [1, 2, 3, 4, 5]
number_squares = {x: x**2 for x in numbers}
print(f"Dictionary comprehension: {number_squares}")

# Set comprehension
unique_remainders = {x % 3 for x in range(10)}
print(f"Set comprehension: {unique_remainders}")

print()

# 12. ZIP FUNCTION WITH LOOPS
print("12. Zip Function with Loops:")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

print("Zipping two lists:")
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

print("\nZipping three lists:")
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, lives in {city}")

print()

# 13. PRACTICAL EXAMPLES
print("13. Practical Examples:")

# Password validation
def validate_password(password):
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit and len(password) >= 8:
        return "Strong password"
    else:
        return "Weak password"

test_passwords = ["Password123", "password", "PASSWORD", "Pass1"]
for pwd in test_passwords:
    result = validate_password(pwd)
    print(f"'{pwd}': {result}")

print()

# Finding prime numbers
def find_primes(limit):
    primes = []
    for num in range(2, limit + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes = find_primes(20)
print(f"Prime numbers up to 20: {primes}")

print()

# Menu system simulation
print("Menu system simulation:")
simulated_choices = ["1", "2", "5", "4"]
choice_index = 0

options = {
    "1": "View Profile",
    "2": "Settings",
    "3": "Help",
    "4": "Exit"
}

while choice_index < len(simulated_choices):
    print("\n--- Menu ---")
    for key, value in options.items():
        print(f"{key}. {value}")

    choice = simulated_choices[choice_index]
    print(f"Simulated choice: {choice}")
    choice_index += 1

    if choice == "1":
        print("Viewing profile...")
    elif choice == "2":
        print("Opening settings...")
    elif choice == "3":
        print("Displaying help...")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, please try again.")

print()

# 14. COMMON LOOP PATTERNS
print("14. Common Loop Patterns:")

# Counter pattern
print("Counter pattern:")
data = ["apple", "banana", "apple", "orange", "banana", "apple"]
counter = {}
for item in data:
    if item in counter:
        counter[item] += 1
    else:
        counter[item] = 1
print(f"Item counts: {counter}")

# Accumulator pattern
print("\nAccumulator pattern:")
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"Sum of {numbers} = {total}")

# Filter pattern
print("\nFilter pattern:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
print(f"Even numbers: {even_numbers}")

# Transform pattern
print("\nTransform pattern:")
celsius_temps = [0, 20, 30, 40]
fahrenheit_temps = []
for temp in celsius_temps:
    fahrenheit = (temp * 9/5) + 32
    fahrenheit_temps.append(fahrenheit)
print(f"Celsius: {celsius_temps}")
print(f"Fahrenheit: {fahrenheit_temps}")

print("\n=== LOOP STATEMENTS LESSON COMPLETE ===")