# 8. Conditional Statements in Python
# Conditional statements allow you to execute different blocks of code based on conditions

print("=== CONDITIONAL STATEMENTS IN PYTHON ===\n")

# 1. IF STATEMENT
print("1. Basic IF Statement:")
age = 18
if age >= 18:
    print(f"Age {age}: You are an adult!")

temperature = 25
if temperature > 30:
    print("It's hot outside!")
if temperature <= 30:
    print("Temperature is comfortable.")

print()

# 2. IF-ELSE STATEMENT
print("2. IF-ELSE Statement:")
score = 85
if score >= 90:
    print(f"Score {score}: Excellent! Grade A")
else:
    print(f"Score {score}: Good effort! Keep working")

number = 7
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

print()

# 3. IF-ELIF-ELSE STATEMENT
print("3. IF-ELIF-ELSE Statement:")
grade = 88
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
print(f"Grade {grade} = Letter grade: {letter}")

# Weather conditions
weather = "cloudy"
if weather == "sunny":
    print("Perfect day for a picnic!")
elif weather == "rainy":
    print("Better stay inside and read a book.")
elif weather == "cloudy":
    print("Good day for a walk in the park.")
else:
    print("Check the weather forecast.")

print()

# 4. NESTED IF STATEMENTS
print("4. Nested IF Statements:")
user_age = 16
has_license = True

if user_age >= 16:
    if has_license:
        print("You can drive!")
    else:
        print("You're old enough but need a license.")
else:
    print("You're too young to drive.")

# Complex nested example
income = 50000
credit_score = 750
loan_amount = 200000

if income >= 40000:
    if credit_score >= 700:
        if loan_amount <= 300000:
            print("Loan approved!")
        else:
            print("Loan amount too high.")
    else:
        print("Credit score too low.")
else:
    print("Income requirement not met.")

print()

# 5. LOGICAL OPERATORS IN CONDITIONS
print("5. Logical Operators (and, or, not):")

# AND operator
age = 25
has_job = True
if age >= 18 and has_job:
    print("Eligible for credit card")

# OR operator
is_student = False
is_senior = False
age = 30
if is_student or is_senior or age < 12:
    print("Eligible for discount")
else:
    print("Regular pricing applies")

# NOT operator
is_raining = False
if not is_raining:
    print("Good day for outdoor activities")

# Complex logical expressions
username = "admin"
password = "secret123"
is_active = True

if (username == "admin" or username == "root") and password == "secret123" and is_active:
    print("Access granted")
else:
    print("Access denied")

print()

# 6. MEMBERSHIP OPERATORS
print("6. Membership Operators (in, not in):")
fruits = ["apple", "banana", "orange"]
favorite = "apple"

if favorite in fruits:
    print(f"{favorite} is available!")

day = "Sunday"
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if day not in weekdays:
    print(f"{day} is a weekend!")

print()

# 7. IDENTITY OPERATORS
print("7. Identity Operators (is, is not):")
x = None
if x is None:
    print("x is None")

y = []
z = []
if y is not z:
    print("y and z are different objects (even though both are empty lists)")

# Checking boolean values
is_logged_in = True
if is_logged_in is True:
    print("User is logged in")

print()

# 8. TERNARY OPERATOR (CONDITIONAL EXPRESSION)
print("8. Ternary Operator:")
age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age {age}: Status is {status}")

# Multiple ternary operators
number = 0
result = "positive" if number > 0 else "negative" if number < 0 else "zero"
print(f"Number {number} is {result}")

# Ternary with function calls
def get_discount(is_member):
    return 0.1 if is_member else 0.0

member_discount = get_discount(True)
non_member_discount = get_discount(False)
print(f"Member discount: {member_discount * 100}%")
print(f"Non-member discount: {non_member_discount * 100}%")

print()

# 9. TRUTHINESS AND FALSY VALUES
print("9. Truthiness and Falsy Values:")
# Falsy values: False, None, 0, 0.0, "", [], {}, set()
# Everything else is truthy

values_to_test = [True, False, None, 0, 1, "", "hello", [], [1, 2], {}, {"key": "value"}]

for value in values_to_test:
    if value:
        print(f"{repr(value)} is truthy")
    else:
        print(f"{repr(value)} is falsy")

print()

# 10. PRACTICAL EXAMPLES
print("10. Practical Examples:")

# User input validation
def validate_email(email):
    if "@" in email and "." in email:
        return "Valid email format"
    else:
        return "Invalid email format"

test_emails = ["user@example.com", "invalid-email", "test@domain.org"]
for email in test_emails:
    print(f"{email}: {validate_email(email)}")

print()

# Grade calculator
def calculate_grade(assignments, tests, final_exam):
    total_score = (assignments * 0.3) + (tests * 0.4) + (final_exam * 0.3)

    if total_score >= 90:
        return "A"
    elif total_score >= 80:
        return "B"
    elif total_score >= 70:
        return "C"
    elif total_score >= 60:
        return "D"
    else:
        return "F"

student_grade = calculate_grade(85, 78, 92)
print(f"Student final grade: {student_grade}")

# Shopping cart discount system
def calculate_discount(total_amount, is_member, item_count):
    discount = 0

    if is_member:
        discount += 0.1  # 10% member discount

    if total_amount > 100:
        discount += 0.05  # 5% for orders over $100

    if item_count >= 5:
        discount += 0.02  # 2% for 5+ items

    # Maximum discount is 20%
    if discount > 0.2:
        discount = 0.2

    return discount

# Test the discount system
cart_total = 150
is_premium_member = True
items_in_cart = 6

discount_rate = calculate_discount(cart_total, is_premium_member, items_in_cart)
final_price = cart_total * (1 - discount_rate)

print(f"Cart total: ${cart_total}")
print(f"Discount applied: {discount_rate * 100}%")
print(f"Final price: ${final_price:.2f}")

print()

# 11. COMMON PATTERNS AND BEST PRACTICES
print("11. Best Practices:")

# Use parentheses for complex conditions
age = 25
income = 50000
employment_status = "employed"

# Good: Clear and readable
if (age >= 18 and age <= 65) and (income > 30000) and (employment_status == "employed"):
    print("Eligible for premium account")

# Multiple conditions - use variables for clarity
is_adult = age >= 18
has_good_income = income > 30000
is_employed = employment_status == "employed"

if is_adult and has_good_income and is_employed:
    print("All requirements met")

# Avoid deeply nested conditions - use early returns in functions
def check_eligibility(age, income, employment):
    if age < 18:
        return "Too young"
    if income < 30000:
        return "Income too low"
    if employment != "employed":
        return "Must be employed"
    return "Eligible"

print(f"Eligibility status: {check_eligibility(25, 45000, 'employed')}")

# 12. SWITCH-CASE ALTERNATIVES (Python 3.9 compatible)
print("12. Switch-Case Alternatives:")

# Basic if-elif-else (equivalent to match-case)
def handle_http_status(status_code):
    if status_code == 200:
        return "OK"
    elif status_code == 404:
        return "Not Found"
    elif status_code == 500:
        return "Internal Server Error"
    else:  # Default case
        return "Unknown Status"

print(f"Status 200: {handle_http_status(200)}")
print(f"Status 404: {handle_http_status(404)}")
print(f"Status 999: {handle_http_status(999)}")

# Multiple values with if-elif-else
def check_day_type(day):
    if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        return "Weekday"
    elif day in ["Saturday", "Sunday"]:
        return "Weekend"
    else:
        return "Invalid day"

print(f"Monday is a {check_day_type('Monday')}")
print(f"Saturday is a {check_day_type('Saturday')}")

# Conditions with if-elif-else
def categorize_number(x):
    if x < 0:
        return "Negative"
    elif x == 0:
        return "Zero"
    elif x > 0 and x <= 10:
        return "Small positive"
    elif x > 10:
        return "Large positive"

print(f"Number -5: {categorize_number(-5)}")
print(f"Number 0: {categorize_number(0)}")
print(f"Number 7: {categorize_number(7)}")
print(f"Number 15: {categorize_number(15)}")

# Data structure handling with if-elif-else
def process_data(data):
    if isinstance(data, dict) and data.get("type") == "user" and "name" in data:
        return f"Processing user: {data['name']}"
    elif isinstance(data, dict) and data.get("type") == "admin" and "permissions" in data:
        perms = data["permissions"]
        return f"Admin with permissions: {', '.join(perms)}"
    elif isinstance(data, list) and len(data) > 1:
        return f"List starting with {data[0]}, has {len(data)-1} more items"
    elif isinstance(data, list) and len(data) == 1:
        return f"Single item list: {data[0]}"
    else:
        return "Unknown data format"

test_data = [
    {"type": "user", "name": "Alice"},
    {"type": "admin", "permissions": ["read", "write", "delete"]},
    [1, 2, 3, 4, 5],
    ["single"],
    "unknown"
]

for data in test_data:
    print(f"Data {data}: {process_data(data)}")

print()

# 13. DICTIONARY-BASED SWITCH ALTERNATIVES
print("13. Dictionary-Based Switch Alternatives:")

# Dictionary mapping (most common alternative)
def get_month_name_dict(month_num):
    month_dict = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return month_dict.get(month_num, "Invalid month")

print(f"Month 3: {get_month_name_dict(3)}")
print(f"Month 13: {get_month_name_dict(13)}")

# Dictionary with functions
def summer_activity():
    return "Go swimming"

def winter_activity():
    return "Go skiing"

def spring_activity():
    return "Go hiking"

def fall_activity():
    return "Go apple picking"

def get_seasonal_activity(season):
    activities = {
        "summer": summer_activity,
        "winter": winter_activity,
        "spring": spring_activity,
        "fall": fall_activity
    }
    activity_func = activities.get(season.lower())
    return activity_func() if activity_func else "Stay indoors"

print(f"Summer activity: {get_seasonal_activity('summer')}")
print(f"Invalid season: {get_seasonal_activity('invalid')}")

# Class-based approach
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b if b != 0 else "Cannot divide by zero"

    def calculate(self, operation, a, b):
        operations = {
            "+": self.add,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }
        func = operations.get(operation)
        return func(a, b) if func else "Invalid operation"

calc = Calculator()
print(f"5 + 3 = {calc.calculate('+', 5, 3)}")
print(f"10 / 2 = {calc.calculate('/', 10, 2)}")
print(f"Invalid op: {calc.calculate('%', 5, 3)}")