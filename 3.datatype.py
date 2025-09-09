# Text type
name = "Bondeth"
print("Name: ", name)

# Numeric type: int, float, complex
age = 22
height = 1.69
random = 5 + 10j

print("Age: ", age)
print("Height: ", height)
print("Random: ", random)

# Sequence Types: list, tuple, range
list_of_fruits = ["apple", "banana", "coconut"]
tuple_of_fruits = ("apple", "banana", "cherry")
random = range(6)

print("List of Fruits: ", list_of_fruits)
print("Tuple of Fruits: ", tuple_of_fruits)
print("Random: ", random)

# Mapping Type: dict
bondeth = {
    'name': 'Bondeth',
    'age': 22,
    'position': 'Full Stack Developer'
}
print("Person 1: ", bondeth)

# Set Types: set, frozenset
set_of_fruits = {"apple", "banana", "coconut"}
frozenset_of_fruits = frozenset({"apple", "banana", "cherry"})

print("set_of_fruits: ", set_of_fruits)
print("frozenset_of_fruits: ", frozenset_of_fruits)

# Boolean Type: bool
x = True
y = False

print("Value of x: ", x)
print("Value of y: ", y)

# Binary Types: bytes, bytearray, memoryview
a = bytes(5)
b = bytearray(5)
c =  memoryview(bytes(5))

print("Value of a: ", a)
print("Value of b: ", b)
print("Value of c: ", c)

# None Type
none = None

print("none: ", none)
print("Type of none: ", type(none))