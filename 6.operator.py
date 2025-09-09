# Arithmetic operators
a = 10
b = 5

add = a + b 
sub = a - b
mul = a * b
div = a / b
mol = a % b
exp = a ** b 
floor_div = a // b

print(f"Add: {add}")
print(f"Sub: {sub}")
print(f"Mul: {mul}")
print(f"Div: {div}")
print(f"Mod: {mol}")
print(f"Exp: {exp}")
print(f"Floor Div: {floor_div}")

# Comparison operators
x = 15
y = 10

print(f"\nComparison operators:")
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} > {y}: {x > y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} >= {y}: {x >= y}")
print(f"{x} <= {y}: {x <= y}")

# Logical operators
p = True
q = False

print(f"\nLogical operators:")
print(f"{p} and {q}: {p and q}")
print(f"{p} or {q}: {p or q}")
print(f"not {p}: {not p}")
print(f"not {q}: {not q}")

# Assignment operators
num = 20
print(f"\nAssignment operators:")
print(f"Initial value: {num}")

num += 5
print(f"After += 5: {num}")

num -= 3
print(f"After -= 3: {num}")

num *= 2
print(f"After *= 2: {num}")

num /= 4
print(f"After /= 4: {num}")

num %= 7
print(f"After %= 7: {num}")

num **= 2
print(f"After **= 2: {num}")

# Identity operators
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"\nIdentity operators:")
print(f"list1 is list2: {list1 is list2}")
print(f"list1 is list3: {list1 is list3}")
print(f"list1 is not list2: {list1 is not list2}")

# Membership operators
fruits = ["apple", "banana", "orange"]
print(f"\nMembership operators:")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'apple' not in fruits: {'apple' not in fruits}")

# Bitwise operators
m = 10  # Binary: 1010
n = 4   # Binary: 0100

print(f"\nBitwise operators:")

print(f"{m} & {n} (AND): {m & n}")
print(f"{m} | {n} (OR): {m | n}")
print(f"{m} ^ {n} (XOR): {m ^ n}")
print(f"~{m} (NOT): {~m}")
print(f"{m} << 2 (Left shift): {m << 2}")
print(f"{m} >> 1 (Right shift): {m >> 1}")