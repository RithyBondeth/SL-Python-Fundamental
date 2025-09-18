def add_regular(a, b): 
    return a + b

print(f"add regular: {add_regular(10, 20)}")

add_lambda = lambda a, b: a + b
print(f"add lambda: {add_lambda(10, 20)}")

mul_lambda = (lambda x, y, z: x * y * z)(1, 2, 3)
print(f"mul lambda inline: {mul_lambda}")

upperStr = lambda str: str.upper()
print(f"upper string: {upperStr('bondeth')}")

divide = lambda x, y: x / y if y != 0 else "Cannot Divide By Zero"

print(f"10/2: {divide(10, 2)}")
print(f"10/0: {divide(10, 0)}")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

celsius_temps = [0, 20, 25, 30, 37, 100]
celsius = list(map(lambda c: f"{c}C", celsius_temps))
fahrenheit = list(map(lambda c: f"{(c * 9/5) + 32}F", celsius_temps))

print(f"Celsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

even_numbers = list(filter(lambda num: num % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

odd_numbers = [num for num in numbers if num % 2 != 0]
print(f"Odd numbers: {odd_numbers}")

students = [
    {"name": "Alice", "age": 23, "grade": 88},
    {"name": "Bob", "age": 20, "grade": 92},
    {"name": "Charlie", "age": 22, "grade": 85},
    {"name": "Diana", "age": 21, "grade": 95}
]

sort_by_age = sorted(students, key=lambda x: x['age'], reverse=True)
sort_by_length = sorted(students, key=lambda x: len(x['name']))

for student in sort_by_age:
    print(f"Name: {student['name']}, Age: {student['age']}")


print("="*20)
for student in sort_by_length:
     print(f"Name: {student['name']}")

points = [(1, 3), (3, 1), (2, 2), (4, 0)]
sort_by_y_coordinate = sorted(points, key=lambda point: point[1], reverse=True)
print(f"Coordinate: {sort_by_y_coordinate}")

nums = [1, 2, 3, 4, 5]
transformed = [(lambda x: x**2 + 2*x + 1)(n) for n in numbers]
print(f"Before Transformed: {nums}")
print(f"Transformed using lambda: {transformed}")

data = [1, -2, 3, -4, 5, -6]
processed = [(lambda x: abs(x) + 1)(y) for y in data]
print(f"Data: {data}")
print(f"Processed: {processed}")

test = [1, 3, 5, 7]
all_even = all(lambda x: x % 2 == 0 for x in test)
print(f"All Even: {all_even}")