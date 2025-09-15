import math

def cal_2nd_degree_equation(a, b, c):
    if b % 2 == 0:
        b_prime = b/2
        delta_prime = b_prime**2 - a*c
        
        if delta_prime > 0:
            return (-b_prime - math.sqrt(delta_prime))/a, (-b_prime + math.sqrt(delta_prime))/a
        elif delta_prime == 0:
            return -b_prime/a, b_prime/a
        else:
            return "Equation has no root"
    else:
        delta = b**2 - 4*a*c

        if delta > 0:
            return (-b - math.sqrt(delta))/(2*a), (-b + math.sqrt(delta))/(2*a)
        elif delta == 0:
            return -b/(2*a), b/(2*a)
        else:
           return "Equation has no root"

    
root1, root2 = cal_2nd_degree_equation(1, 2, 1)
print(f"Equation root1 x1={root1}")
print(f"Equation root2 x2={root2}")
        

def cal_rectangle_area(x, y=5):
    return x * y

rectangle1 = (10, 20)
x, y = rectangle1

print(f"Area of rectangle (x={x}, y={y}) = {cal_rectangle_area(x)}")
 
square = lambda x: x **2
add = lambda x=1, y=1: x + y
print(f"Square of 5: {square(5)}")
print(f"Add {add()}")

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(lambda x: x**2, numbers)
print(list(squared_numbers))

even_numbers = list(filter(lambda x: x%2==0, numbers))
print(f"Even numbers: {even_numbers}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(f"factorial of 5: {factorial(3)}")


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(6):
    print(f"F({i}) = {fibonacci(i)}")


def apply_operation(numbers, operation):
    return [operation(num) for num in numbers]

def double(x):
    return x*2

def cube(x): 
    return x**3

doubled = apply_operation([1, 2, 3], double)
cubed = apply_operation([1, 2, 3], cube)

print(f"Doubled: {doubled}")
print(f"Cube: {cubed}")

def add_numbers(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")

add_numbers(10, 20)


def create_profile(name="null", age=0, profession="null"):
    print("="*30)
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Profession: {profession}")
    print("="*30)


create_profile(name="Bondeth", age=22, profession="AI and ML Engineer")
create_profile(age=18, name="Benx", profession="Web Developer")
create_profile()

def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(f"1 + 2 + 3 = {sum_numbers(1, 2, 3)}")
print(f"1 + 2 + 3 + 4 + 5= {sum_numbers(1, 2, 3, 4, 5)}")


def create_info_student(**details):
    print("Student Detail")
    for key, value in details.items():
        print(f"{key}: {value}")

create_info_student(name="Bondeth", age=22)
create_info_student(name="Bondeth", age=22, profession="AI and ML Engineer")

def flexible_function(required_param, *args, **kwargs):
    print(f"Required parameter: {required_param}")
    print(f"Additional arguments: {args}")
    print(f"Keyword arguments:")
    for key, value in kwargs.items():
        print(f"{key} = {value}")

flexible_function("Detail Information", 1, 2, 3, 4, 5, name="Bondeth", profession="AI and ML Engineer")

nums = [1, 2, 3, 4, 5]
nums_add_2 = map(lambda x: x + 2, nums)
print(f"nums after add 2: {list(nums_add_2)}")

print(list(map(lambda i: i**2, nums)))

def validate_email(email):
    return "@" in email and "." in email

emails = ["user@example.com", "invalid-email", "another@test.org"]

for email in emails:
    print(f"{email} is an email => {validate_email(email)}")

def format_currency(amount, currency="USD"):
    print(f"{currency} {amount:.2f}")

format_currency(100)
format_currency(100000, "AUD")