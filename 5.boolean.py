# BOOLEAN IN PYTHON - COMPLETE EXPLANATION

print("=" * 50)
print("BOOLEAN BASICS")
print("=" * 50)

# Boolean values
print("Basic Boolean values:")
print(f"True: {True}")
print(f"False: {False}")
print(f"Type of True: {type(True)}")
print(f"Type of False: {type(False)}")

print("\n" + "=" * 50)
print("COMPARISON OPERATORS RETURN BOOLEANS")
print("=" * 50)

a = 10
b = 5

print(f"{a} > {b}: {a > b}")
print(f"{a} < {b}: {a < b}")
print(f"{a} == {b}: {a == b}")
print(f"{a} != {b}: {a != b}")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} <= {b}: {a <= b}")

print("\n" + "=" * 50)
print("TRUTHINESS - WHAT EVALUATES TO TRUE/FALSE")
print("=" * 50)

print("Values that are TRUE:")
truthy_values = [
    True,
    1,
    -1,
    3.14,
    "hello",
    "0",  # String "0" is truthy
    [1, 2, 3],
    {"key": "value"},
    (1, 2),
    range(5)
]

for value in truthy_values:
    print(f"bool({repr(value)}): {bool(value)}")

print("\nValues that are FALSE:")
falsy_values = [
    False,
    0,
    0.0,
    "",
    None,
    [],
    {},
    (),
    set(),
    range(0)
]

for value in falsy_values:
    print(f"bool({repr(value)}): {bool(value)}")

print("\n" + "=" * 50)
print("LOGICAL OPERATORS")
print("=" * 50)

x = True
y = False

print(f"{x} and {y}: {x and y}")
print(f"{x} or {y}: {x or y}")
print(f"not {x}: {not x}")
print(f"not {y}: {not y}")

# Short-circuit evaluation
print(f"\nShort-circuit examples:")
print(f"True or (1/0 would error): {True or print('This will not print')}")
print(f"False and (1/0 would error): {False and print('This will not print')}")

print("\n" + "=" * 50)
print("BOOLEAN IN CONDITIONALS")
print("=" * 50)

# If statements
number = 42
if number:
    print(f"Number {number} is truthy")

name = ""
if not name:
    print("Name is empty (falsy)")

# Multiple conditions
age = 25
has_license = True

if age >= 18 and has_license:
    print("Can drive")
else:
    print("Cannot drive")

print("\n" + "=" * 50)
print("BOOLEAN WITH FUNCTIONS")
print("=" * 50)

def is_even(num):
    """Returns True if number is even, False otherwise"""
    return num % 2 == 0

def is_positive(num):
    """Returns True if number is positive"""
    return num > 0

def is_valid_email(email):
    """Simple email validation"""
    return "@" in email and "." in email

# Testing functions
test_numbers = [2, 3, -5, 0]
for num in test_numbers:
    print(f"{num} is even: {is_even(num)}, is positive: {is_positive(num)}")

emails = ["user@example.com", "invalid-email", "test@test.org"]
for email in emails:
    print(f"'{email}' is valid: {is_valid_email(email)}")

print("\n" + "=" * 50)
print("BOOLEAN WITH CLASSES")
print("=" * 50)

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    
    def __bool__(self):
        """Account is truthy if it has positive balance"""
        return self.balance > 0
    
    def __str__(self):
        return f"Account(${self.balance})"

# Testing custom boolean behavior
accounts = [
    BankAccount(100),   # Has money - truthy
    BankAccount(0),     # No money - falsy
    BankAccount(-50)    # Debt - falsy
]

for account in accounts:
    if account:
        print(f"{account} - Account has funds")
    else:
        print(f"{account} - Account is empty or in debt")

print("\n" + "=" * 50)
print("PRACTICAL EXAMPLES")
print("=" * 50)

# Example 1: Input validation
def validate_user_input(name, age, email):
    """Validate user registration data"""
    errors = []
    
    if not name:
        errors.append("Name is required")
    
    if not isinstance(age, int) or age < 0:
        errors.append("Age must be a positive integer")
    
    if not email or "@" not in email:
        errors.append("Valid email is required")
    
    return len(errors) == 0, errors

# Test validation
test_cases = [
    ("John Doe", 25, "john@email.com"),
    ("", 25, "john@email.com"),
    ("Jane", -5, "invalid-email"),
    ("Bob", 30, "")
]

for name, age, email in test_cases:
    is_valid, errors = validate_user_input(name, age, email)
    print(f"Input: {name}, {age}, {email}")
    print(f"Valid: {is_valid}")
    if errors:
        print(f"Errors: {', '.join(errors)}")
    print()

# Example 2: Feature flags
class FeatureFlags:
    def __init__(self):
        self.dark_mode = True
        self.beta_features = False
        self.notifications = True
    
    def can_access_beta(self):
        return self.beta_features
    
    def should_show_notifications(self):
        return self.notifications

flags = FeatureFlags()
print("Feature availability:")
print(f"Dark mode: {flags.dark_mode}")
print(f"Beta features: {flags.can_access_beta()}")
print(f"Notifications: {flags.should_show_notifications()}")

print("\n" + "=" * 50)
print("BOOLEAN CONVERSION TIPS")
print("=" * 50)

print("Converting to boolean explicitly:")
values = [1, 0, "hello", "", [1, 2], [], None]
for val in values:
    print(f"bool({repr(val)}) = {bool(val)}")

print(f"\nRemember:")
print(f"- Use 'is' for None: value is None")
print(f"- Use 'is' for True/False: value is True")
print(f"- Use 'not' for negation: not value")
print(f"- Empty collections are falsy: [], {{}}, (), set()")
print(f"- Zero numbers are falsy: 0, 0.0")
print(f"- Everything else is generally truthy")