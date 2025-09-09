# STRING DEMONSTRATION IN PYTHON

print("=" * 60)
print("STRING CREATION AND BASIC OPERATIONS")
print("=" * 60)

# Different ways to create strings
single_quote = 'Hello Python'
double_quote = "Hello World"
triple_quote = """This is a
multi-line string
that spans several lines"""

print("Single quotes:", single_quote)
print("Double quotes:", double_quote)
print("Triple quotes:")
print(triple_quote)

print("\n" + "=" * 60)
print("STRING LENGTH AND ITERATION")
print("=" * 60)

name = "Python Programming"
print(f"String: '{name}'")
print(f"Length: {len(name)} characters")

print("Iterating through each character:")
for i, char in enumerate(name):
    print(f"Index {i}: '{char}'")

print("\n" + "=" * 60)
print("STRING INDEXING AND SLICING")
print("=" * 60)

text = "Hello, World!"
print(f"Original string: '{text}'")
print(f"First character: '{text[0]}'")
print(f"Last character: '{text[-1]}'")
print(f"Characters 0-4: '{text[0:5]}'")
print(f"Characters 7 to end: '{text[7:]}'")
print(f"Last 6 characters: '{text[-6:]}'")
print(f"Every 2nd character: '{text[::2]}'")
print(f"Reversed string: '{text[::-1]}'")

print("\n" + "=" * 60)
print("STRING CHECKING AND SEARCHING")
print("=" * 60)

sentence = "Python is amazing and powerful"
print(f"Original: '{sentence}'")
print(f"'Python' in sentence: {'Python' in sentence}")
print(f"'Java' not in sentence: {'Java' not in sentence}")
print(f"Starts with 'Python': {sentence.startswith('Python')}")
print(f"Ends with 'powerful': {sentence.endswith('powerful')}")
print(f"Position of 'amazing': {sentence.find('amazing')}")
print(f"Count of 'a': {sentence.count('a')}")

print("\n" + "=" * 60)
print("STRING CASE METHODS")
print("=" * 60)

mixed_case = "hELLo WoRLd PyThOn"
print(f"Original: '{mixed_case}'")
print(f"Upper case: '{mixed_case.upper()}'")
print(f"Lower case: '{mixed_case.lower()}'")
print(f"Title case: '{mixed_case.title()}'")
print(f"Capitalize: '{mixed_case.capitalize()}'")
print(f"Swap case: '{mixed_case.swapcase()}'")

print("\n" + "=" * 60)
print("STRING CLEANING AND MODIFICATION")
print("=" * 60)

messy_string = "   Hello, Python World!   "
print(f"Original: '{messy_string}'")
print(f"Strip whitespace: '{messy_string.strip()}'")
print(f"Left strip: '{messy_string.lstrip()}'")
print(f"Right strip: '{messy_string.rstrip()}'")
print(f"Replace 'Python' with 'Amazing': '{messy_string.replace('Python', 'Amazing')}'")

print("\n" + "=" * 60)
print("STRING SPLITTING AND JOINING")
print("=" * 60)

data = "apple,banana,orange,grape"
print(f"Original: '{data}'")
fruits = data.split(',')
print(f"Split by comma: {fruits}")

sentence_words = "Python is awesome"
words = sentence_words.split()
print(f"Split by spaces: {words}")

# Joining strings
joined = " | ".join(fruits)
print(f"Joined with ' | ': '{joined}'")

print("\n" + "=" * 60)
print("STRING FORMATTING - F-STRINGS")
print("=" * 60)

name = "Alice"
age = 28
height = 5.6
balance = 1234.567

print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"Height: {height:.1f} feet")
print(f"Balance: ${balance:.2f}")
print(f"In 5 years, {name} will be {age + 5}")

# Advanced f-string formatting
print(f"Name in uppercase: {name.upper()}")
print(f"Balance with commas: ${balance:,.2f}")

print("\n" + "=" * 60)
print("STRING FORMATTING - FORMAT METHOD")
print("=" * 60)

template = "Hello, my name is {name} and I am {age} years old"
formatted = template.format(name="Bob", age=25)
print(formatted)

# Positional arguments
template2 = "Name: {0}, Age: {1}, City: {2}"
print(template2.format("Charlie", 30, "New York"))

# Number formatting with format method
number = 123456.789
print("Formatted number: {:.2f}".format(number))
print("With commas: {:,.2f}".format(number))

print("\n" + "=" * 60)
print("ESCAPE CHARACTERS")
print("=" * 60)

print("Quote inside string: \"Hello World\"")
print("Single quote: 'It's a beautiful day'")
print("Newline example:\nThis is line 1\nThis is line 2")
print("Tab example: Name:\tJohn\tAge:\t25")
print("Backslash: C:\\Users\\Documents")

print("\n" + "=" * 60)
print("STRING CONCATENATION")
print("=" * 60)

first = "Hello"
second = "World"
number = 42

# Different concatenation methods
print("Plus operator: " + first + " " + second)
print("F-string: " + f"{first} {second}")
print("Format method: " + "{} {}".format(first, second))
print("Join method: " + " ".join([first, second]))

# Concatenating strings with numbers
print(f"String with number: {first} {number}")

print("\n" + "=" * 60)
print("STRING VALIDATION METHODS")
print("=" * 60)

test_strings = ["Hello123", "123456", "hello", "HELLO", "Hello World", "   "]

for test_str in test_strings:
    print(f"\nTesting: '{test_str}'")
    print(f"  Is alphanumeric: {test_str.isalnum()}")
    print(f"  Is alphabetic: {test_str.isalpha()}")
    print(f"  Is digit: {test_str.isdigit()}")
    print(f"  Is lowercase: {test_str.islower()}")
    print(f"  Is uppercase: {test_str.isupper()}")
    print(f"  Is space: {test_str.isspace()}")

print("\n" + "=" * 60)
print("PRACTICAL STRING EXAMPLES")
print("=" * 60)

# Email validation (simple)
def is_valid_email(email):
    return "@" in email and "." in email and len(email) > 5

emails = ["user@example.com", "invalid.email", "test@test.org", "@invalid.com"]
for email in emails:
    print(f"'{email}' is valid: {is_valid_email(email)}")

print()

# Password strength checker
def check_password_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in "!@#$%^&*" for c in password)
    
    strength = sum([has_upper, has_lower, has_digit, has_special])
    
    if len(password) < 8:
        return "Too short"
    elif strength < 2:
        return "Weak"
    elif strength < 3:
        return "Medium"
    else:
        return "Strong"

passwords = ["abc", "Password", "Password123", "P@ssw0rd!", "mypassword"]
for pwd in passwords:
    print(f"'{pwd}' strength: {check_password_strength(pwd)}")

print("\n" + "=" * 60)
print("STRING IMMUTABILITY DEMONSTRATION")
print("=" * 60)

original = "Hello"
print(f"Original string: '{original}'")
print(f"ID of original: {id(original)}")

# Attempting to "modify" creates a new string
modified = original + " World"
print(f"Modified string: '{modified}'")
print(f"ID of modified: {id(modified)}")
print(f"IDs are different: {id(original) != id(modified)}")

print(f"\nOriginal string unchanged: '{original}'")
print("Strings are immutable in Python!")