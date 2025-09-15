# 8. Python Decorators - Complete Guide

# Decorators are a powerful feature that allows you to modify or extend
# the behavior of functions or classes without permanently modifying them
# They use the @ symbol and are applied above function definitions

import time
import functools
from datetime import datetime

print("=== PYTHON DECORATORS TUTORIAL ===\n")

# 1. UNDERSTANDING THE CONCEPT - FUNCTIONS AS FIRST-CLASS OBJECTS
print("1. Functions as First-Class Objects:")

def say_hello():
    return "Hello!"

def say_goodbye():
    return "Goodbye!"

# Functions can be assigned to variables
greeting_func = say_hello
print(f"Calling through variable: {greeting_func()}")

# Functions can be passed as arguments
def call_function(func):
    return func()

print(f"Passing function as argument: {call_function(say_goodbye)}")
print()

# 2. BASIC DECORATOR CONCEPT - MANUAL WRAPPING
print("2. Basic Decorator Concept (Manual):")

def my_function():
    print("Original function called")

def simple_wrapper(func):
    """A simple wrapper function"""
    def wrapper():
        print("Before function call")
        result = func()
        print("After function call")
        return result
    return wrapper

# Manual decoration
decorated_function = simple_wrapper(my_function)
print("Calling manually decorated function:")
decorated_function()
print()

# 3. DECORATOR SYNTAX WITH @
print("3. Decorator Syntax with @:")

def my_decorator(func):
    """A basic decorator"""
    def wrapper():
        print("🎭 Decorator: Before function execution")
        result = func()
        print("🎭 Decorator: After function execution")
        return result
    return wrapper

@my_decorator
def greet_world():
    print("Hello, World from decorated function!")
    return "Greeting completed"

print("Calling @decorated function:")
result = greet_world()
print(f"Returned: {result}")
print()

# 4. DECORATORS WITH FUNCTION ARGUMENTS
print("4. Decorators with Function Arguments:")

def args_decorator(func):
    """Decorator that handles function arguments"""
    def wrapper(*args, **kwargs):
        print(f"📝 Arguments received: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"📝 Function returned: {result}")
        return result
    return wrapper

@args_decorator
def add_numbers(a, b, operation="addition"):
    result = a + b
    print(f"Performing {operation}: {a} + {b} = {result}")
    return result

@args_decorator
def greet_person(name, greeting="Hello"):
    message = f"{greeting}, {name}!"
    print(message)
    return message

print("Testing decorator with arguments:")
add_numbers(5, 3)
greet_person("Alice", greeting="Hi")
print()

# 5. TIMING DECORATOR - PRACTICAL EXAMPLE
print("5. Timing Decorator (Practical Example):")

def timing_decorator(func):
    """Decorator to measure function execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"⏱️  Starting {func.__name__} at {datetime.now().strftime('%H:%M:%S')}")

        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time
        print(f"⏱️  {func.__name__} completed in {execution_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """A function that takes some time to execute"""
    print("Processing...")
    time.sleep(1)  # Simulate work
    return "Task completed"

@timing_decorator
def calculate_fibonacci(n):
    """Calculate Fibonacci number"""
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

print("Testing timing decorator:")
slow_function()
print(f"Fibonacci(10) = {calculate_fibonacci(10)}")
print()

# 6. LOGGING DECORATOR
print("6. Logging Decorator:")

def logging_decorator(func):
    """Decorator that logs function calls"""
    def wrapper(*args, **kwargs):
        print(f"📋 LOG: Calling {func.__name__}")
        print(f"📋 LOG: Arguments - args: {args}, kwargs: {kwargs}")

        try:
            result = func(*args, **kwargs)
            print(f"📋 LOG: {func.__name__} executed successfully")
            print(f"📋 LOG: Returned: {result}")
            return result
        except Exception as e:
            print(f"📋 LOG: ERROR in {func.__name__}: {e}")
            raise
    return wrapper

@logging_decorator
def divide_numbers(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    result = a / b
    return result

print("Testing logging decorator:")
divide_numbers(10, 2)
try:
    divide_numbers(10, 0)
except ValueError as e:
    print(f"Caught exception: {e}")
print()

# 7. DECORATOR WITH PARAMETERS
print("7. Decorators with Parameters:")

def repeat_decorator(times):
    """Decorator factory that creates a decorator to repeat function calls"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"🔄 Repeating {func.__name__} {times} times:")
            results = []
            for i in range(times):
                print(f"  Execution #{i+1}:")
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat_decorator(times=3)
def say_hello_repeated(name):
    message = f"Hello, {name}!"
    print(f"  {message}")
    return message

print("Testing parameterized decorator:")
results = say_hello_repeated("Bob")
print(f"All results: {results}")
print()

# 8. AUTHENTICATION DECORATOR
print("8. Authentication Decorator:")

# Simulate user authentication
current_user = {"authenticated": False, "role": "guest"}

def require_auth(func):
    """Decorator that requires authentication"""
    def wrapper(*args, **kwargs):
        if not current_user.get("authenticated", False):
            print("🔒 Access denied: Authentication required")
            return "Authentication required"

        print(f"🔓 Access granted for user role: {current_user.get('role', 'unknown')}")
        return func(*args, **kwargs)
    return wrapper

def require_admin(func):
    """Decorator that requires admin role"""
    def wrapper(*args, **kwargs):
        if current_user.get("role") != "admin":
            print("🚫 Access denied: Admin privileges required")
            return "Admin privileges required"

        print("👑 Admin access granted")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def view_profile():
    return "Profile: User information displayed"

@require_auth
@require_admin
def delete_user(user_id):
    return f"User {user_id} deleted successfully"

print("Testing authentication decorators:")
print("As guest:")
print(view_profile())
print(delete_user("123"))

# Simulate login as regular user
current_user["authenticated"] = True
current_user["role"] = "user"
print("\nAs authenticated user:")
print(view_profile())
print(delete_user("123"))

# Simulate login as admin
current_user["role"] = "admin"
print("\nAs admin:")
print(view_profile())
print(delete_user("123"))
print()

# 9. CACHING DECORATOR
print("9. Caching Decorator:")

def cache_decorator(func):
    """Decorator that caches function results"""
    cache = {}

    def wrapper(*args, **kwargs):
        # Create cache key from arguments
        key = str(args) + str(sorted(kwargs.items()))

        if key in cache:
            print(f"💾 Cache hit for {func.__name__}{args}")
            return cache[key]

        print(f"🔄 Cache miss for {func.__name__}{args} - computing...")
        result = func(*args, **kwargs)
        cache[key] = result
        print(f"💾 Result cached for {func.__name__}{args}")
        return result

    return wrapper

@cache_decorator
def expensive_calculation(n):
    """Simulate an expensive calculation"""
    time.sleep(0.5)  # Simulate processing time
    result = n ** 2 + n * 10
    return result

print("Testing caching decorator:")
print(f"Result 1: {expensive_calculation(5)}")  # Cache miss
print(f"Result 2: {expensive_calculation(5)}")  # Cache hit
print(f"Result 3: {expensive_calculation(10)}")  # Cache miss
print(f"Result 4: {expensive_calculation(5)}")  # Cache hit
print()

# 10. FUNCTOOLS.WRAPS - PRESERVING FUNCTION METADATA
print("10. Preserving Function Metadata with functools.wraps:")

def bad_decorator(func):
    """Decorator without functools.wraps"""
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

def good_decorator(func):
    """Decorator with functools.wraps"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🔧 Good decorator wrapping {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def function_with_bad_decorator():
    """This docstring will be lost"""
    return "bad decorator result"

@good_decorator
def function_with_good_decorator():
    """This docstring will be preserved"""
    return "good decorator result"

print("Function metadata comparison:")
print(f"Bad decorator - Name: {function_with_bad_decorator.__name__}")
print(f"Bad decorator - Doc: {function_with_bad_decorator.__doc__}")
print(f"Good decorator - Name: {function_with_good_decorator.__name__}")
print(f"Good decorator - Doc: {function_with_good_decorator.__doc__}")
print()

# 11. CLASS-BASED DECORATORS
print("11. Class-Based Decorators:")

class CountCalls:
    """Decorator class that counts function calls"""

    def __init__(self, func):
        self.func = func
        self.count = 0
        functools.update_wrapper(self, func)

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"📊 Call #{self.count} to {self.func.__name__}")
        return self.func(*args, **kwargs)

@CountCalls
def say_python():
    print("Python is awesome!")
    return "Python"

print("Testing class-based decorator:")
say_python()
say_python()
say_python()
print(f"Total calls: {say_python.count}")
print()

# 12. MULTIPLE DECORATORS (DECORATOR STACKING)
print("12. Multiple Decorators (Stacking):")

def bold_decorator(func):
    """Add bold formatting"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"**{result}**"
    return wrapper

def italic_decorator(func):
    """Add italic formatting"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"*{result}*"
    return wrapper

def uppercase_decorator(func):
    """Convert to uppercase"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@bold_decorator
@italic_decorator
@uppercase_decorator
def format_text(text):
    return text

print("Testing stacked decorators:")
print(f"Formatted text: {format_text('hello world')}")
print("Note: Decorators are applied bottom-to-top (uppercase → italic → bold)")
print()

# 13. VALIDATION DECORATOR
print("13. Validation Decorator:")

def validate_types(**expected_types):
    """Decorator that validates argument types"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function signature
            import inspect
            sig = inspect.signature(func)
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()

            # Validate types
            for param_name, expected_type in expected_types.items():
                if param_name in bound.arguments:
                    value = bound.arguments[param_name]
                    if not isinstance(value, expected_type):
                        raise TypeError(
                            f"Argument '{param_name}' must be {expected_type.__name__}, "
                            f"got {type(value).__name__}"
                        )

            print(f"✅ Type validation passed for {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_types(name=str, age=int, salary=float)
def create_employee(name, age, salary=50000.0):
    """Create employee record"""
    return f"Employee: {name}, Age: {age}, Salary: ${salary}"

print("Testing validation decorator:")
print(create_employee("Alice", 30, 75000.0))

try:
    create_employee("Bob", "thirty", 60000.0)  # This will fail
except TypeError as e:
    print(f"Validation error: {e}")
print()

# 14. RETRY DECORATOR
print("14. Retry Decorator:")

def retry(max_attempts=3, delay=1):
    """Decorator that retries function on failure"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None

            for attempt in range(max_attempts):
                try:
                    print(f"🔄 Attempt {attempt + 1}/{max_attempts} for {func.__name__}")
                    result = func(*args, **kwargs)
                    print(f"✅ {func.__name__} succeeded on attempt {attempt + 1}")
                    return result
                except Exception as e:
                    last_exception = e
                    print(f"❌ Attempt {attempt + 1} failed: {e}")
                    if attempt < max_attempts - 1:
                        print(f"⏳ Waiting {delay} seconds before retry...")
                        time.sleep(delay)

            print(f"💥 All {max_attempts} attempts failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator

# Simulate unreliable function
import random

@retry(max_attempts=3, delay=0.5)
def unreliable_function():
    """Function that randomly fails"""
    if random.random() < 0.7:  # 70% chance of failure
        raise ConnectionError("Network timeout")
    return "Success! Data retrieved."

print("Testing retry decorator:")
try:
    result = unreliable_function()
    print(f"Final result: {result}")
except ConnectionError as e:
    print(f"Final failure: {e}")
print()

# 15. PRACTICAL DECORATOR COMBINATIONS
print("15. Practical Decorator Combinations:")

@timing_decorator
@cache_decorator
@logging_decorator
def complex_calculation(base, exponent):
    """A complex calculation with multiple decorators"""
    print(f"Computing {base}^{exponent}")
    result = base ** exponent
    return result

print("Testing combined decorators:")
print(f"Result 1: {complex_calculation(2, 10)}")  # Cache miss, full execution
print(f"Result 2: {complex_calculation(2, 10)}")  # Cache hit, faster execution
print()

print("=== DECORATOR TUTORIAL COMPLETE ===")
print("Key takeaways:")
print("• Decorators modify function behavior without changing the function itself")
print("• Use @ syntax to apply decorators cleanly")
print("• *args and **kwargs handle functions with any arguments")
print("• functools.wraps preserves original function metadata")
print("• Decorators can be parameterized using decorator factories")
print("• Multiple decorators can be stacked (applied bottom-to-top)")
print("• Class-based decorators use __call__ method")
print("• Common uses: logging, timing, authentication, caching, validation")
print("• Decorators make code more modular and reusable")