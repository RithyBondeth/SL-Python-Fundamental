name = "Bondeth"
print(name)

# Looping through string
for x in name:
    print(x)

# Length of string
length_of_string = len(name)
print("length_of_string: ", length_of_string)

# Check String
print("Bon" in name)
print("Apple" not in name)

if "deth" in name:
    print("Correct")

# Slicing String
sentence = "Hello, World"

print(sentence[:2])
print(sentence[2:])
print(sentence[-5:-2])

# Modify String: upper(), lower(), strip(), split()
greeting = "Hello, I'm Bondeth"
lower_case = greeting.lower()
upper_case = greeting.upper()

print("Uppercase: ", upper_case)
print("Lowercase: ", lower_case)
print("Remove Whitespace: ", greeting.strip())
print("Replace String: ", greeting.replace("H", "D"))

greeting_list = greeting.split(",") 
print("Split String: ", greeting_list[0])
print("Split String: ", greeting_list[1])

# Concatenation String
a = "Rithy"
b = "Bondeth"
print("a + b: ", a+b)
print("a + b: ", a + " " + b)

# Format String
age = 22
name = "Benx"
height = 1.6955

print(f"My name is {name}. I'm {age} years old")
print(f"My height is {height:.2f}m")
print(f"I have {10 * 5} books")

# Escape character
text = "My name is Bondeth. I study at \"CADT\" of MPTC";
print(text)

print(f"Name: {name}\n")
print(f"Age: {age}\n")

# String Methods: capitalize(), center()
txt = "i love cambodia"

print("Capitalize: ", txt.capitalize())
print("Center: ", txt.center(20)) # taking 20 spaces
print(f"Count: {txt.count('love')}") # only 1 "love" in the txt
print(f"Encode: {txt.encode(encoding="ascii",errors="ignore")}")

