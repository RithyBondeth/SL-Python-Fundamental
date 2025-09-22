# 14.4 Polymorphism in Python
# Polymorphism allows objects of different types to be treated as instances of the same type
# through a common interface. It means "many forms" - one interface, multiple implementations.

print("=" * 60)
print("POLYMORPHISM IN PYTHON")
print("=" * 60)

# 1. METHOD OVERRIDING (Runtime Polymorphism)
print("\n1. METHOD OVERRIDING - Runtime Polymorphism")
print("-" * 50)

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some generic animal sound"

    def move(self):
        return f"{self.name} is moving"

class Dog(Animal):
    def make_sound(self):
        return "Woof! Woof!"

    def move(self):
        return f"{self.name} is running on four legs"

class Cat(Animal):
    def make_sound(self):
        return "Meow! Meow!"

    def move(self):
        return f"{self.name} is gracefully walking"

class Bird(Animal):
    def make_sound(self):
        return "Tweet! Tweet!"

    def move(self):
        return f"{self.name} is flying"

# Creating objects
dog = Dog("Buddy")
cat = Cat("Whiskers")
bird = Bird("Tweety")

print(f"Dog sound: {dog.make_sound()}")
print(f"Cat sound: {cat.make_sound()}")
print(f"Bird sound: {bird.make_sound()}")

print(f"Dog movement: {dog.move()}")
print(f"Cat movement: {cat.move()}")
print(f"Bird movement: {bird.move()}")

# 2. POLYMORPHISM WITH FUNCTION
print("\n2. POLYMORPHISM WITH FUNCTION")
print("-" * 50)

def animal_behavior(animal):
    """Function that works with any Animal object"""
    print(f"Animal: {animal.name}")
    print(f"Sound: {animal.make_sound()}")
    print(f"Movement: {animal.move()}")
    print()

print("Demonstrating polymorphism with function:")
animals = [dog, cat, bird]

for animal in animals:
    animal_behavior(animal)

# 3. DUCK TYPING - "If it walks like a duck and quacks like a duck, it's a duck"
print("\n3. DUCK TYPING")
print("-" * 50)

class Duck:
    def quack(self):
        return "Quack quack!"

    def fly(self):
        return "Flying like a duck"

class Airplane:
    def quack(self):
        return "Honk honk! (airplane horn)"

    def fly(self):
        return "Flying with jet engines"

class Robot:
    def quack(self):
        return "Beep beep! (robot sound)"

    def fly(self):
        return "Flying with propellers"

def make_it_quack_and_fly(duck_like_object):
    """This function works with any object that has quack() and fly() methods"""
    print(f"Sound: {duck_like_object.quack()}")
    print(f"Flight: {duck_like_object.fly()}")
    print()

duck = Duck()
plane = Airplane()
robot = Robot()

print("Duck typing in action:")
make_it_quack_and_fly(duck)
make_it_quack_and_fly(plane)
make_it_quack_and_fly(robot)

# 4. POLYMORPHISM WITH ABSTRACT BASE CLASSES
print("\n4. POLYMORPHISM WITH ABSTRACT BASE CLASSES")
print("-" * 50)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return f"This is a {self.__class__.__name__} with area {self.area():.2f} and perimeter {self.perimeter():.2f}"

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

# Creating shape objects
rectangle = Rectangle(5, 4)
circle = Circle(3)
triangle = Triangle(3, 4, 5)

shapes = [rectangle, circle, triangle]

print("Polymorphism with abstract base classes:")
for shape in shapes:
    print(shape.describe())

# 5. OPERATOR OVERLOADING (Special Methods)
print("\n5. OPERATOR OVERLOADING")
print("-" * 50)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload + operator"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overload - operator"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Overload * operator for scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        """String representation"""
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        """Overload == operator"""
        return self.x == other.x and self.y == other.y

    def __len__(self):
        """Overload len() function"""
        return int((self.x**2 + self.y**2)**0.5)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(f"Vector 1: {v1}")
print(f"Vector 2: {v2}")
print(f"Addition: {v1 + v2}")
print(f"Subtraction: {v1 - v2}")
print(f"Scalar multiplication: {v1 * 2}")
print(f"Are they equal? {v1 == v2}")
print(f"Length of v1: {len(v1)}")

# 6. POLYMORPHISM WITH BUILT-IN FUNCTIONS
print("\n6. POLYMORPHISM WITH BUILT-IN FUNCTIONS")
print("-" * 50)

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __str__(self):
        return f"Playlist '{self.name}' with {len(self.songs)} songs"

book = Book("Python Programming", 350)
playlist = Playlist("My Favorites", ["Song1", "Song2", "Song3", "Song4"])

print("Polymorphism with built-in functions:")
print(f"Book: {book}")
print(f"Book length: {len(book)} pages")
print(f"Playlist: {playlist}")
print(f"Playlist length: {len(playlist)} songs")

# 7. PRACTICAL EXAMPLE: PAYMENT PROCESSING SYSTEM
print("\n7. PRACTICAL EXAMPLE: PAYMENT PROCESSING SYSTEM")
print("-" * 50)

class PaymentProcessor:
    def process_payment(self, amount):
        raise NotImplementedError("Subclasses must implement process_payment")

class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number):
        self.card_number = card_number

    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via Credit Card ending in {self.card_number[-4:]}"

class PayPalProcessor(PaymentProcessor):
    def __init__(self, email):
        self.email = email

    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via PayPal account {self.email}"

class BankTransferProcessor(PaymentProcessor):
    def __init__(self, account_number):
        self.account_number = account_number

    def process_payment(self, amount):
        return f"Processing ${amount:.2f} via Bank Transfer from account {self.account_number}"

class PaymentSystem:
    def __init__(self):
        self.processors = []

    def add_processor(self, processor):
        self.processors.append(processor)

    def process_all_payments(self, amount):
        for processor in self.processors:
            print(processor.process_payment(amount))

# Creating payment processors
credit_card = CreditCardProcessor("1234567890123456")
paypal = PayPalProcessor("user@example.com")
bank_transfer = BankTransferProcessor("ACC123456")

# Payment system
payment_system = PaymentSystem()
payment_system.add_processor(credit_card)
payment_system.add_processor(paypal)
payment_system.add_processor(bank_transfer)

print("Payment processing with polymorphism:")
payment_system.process_all_payments(99.99)

# 8. POLYMORPHISM BENEFITS AND BEST PRACTICES
print("\n8. POLYMORPHISM BENEFITS AND BEST PRACTICES")
print("-" * 50)

print("Benefits of Polymorphism:")
print("• Code Reusability: Same interface for different implementations")
print("• Flexibility: Easy to add new types without changing existing code")
print("• Maintainability: Changes to implementation don't affect client code")
print("• Extensibility: New classes can be added that work with existing functions")

print("\nBest Practices:")
print("• Use abstract base classes for defining interfaces")
print("• Follow the Liskov Substitution Principle")
print("• Keep interfaces simple and focused")
print("• Use duck typing when appropriate")
print("• Implement special methods for natural integration with Python")

# 9. COMMON POLYMORPHISM PATTERNS
print("\n9. COMMON POLYMORPHISM PATTERNS")
print("-" * 50)

# Strategy Pattern using polymorphism
class SortingStrategy:
    def sort(self, data):
        raise NotImplementedError

class BubbleSort(SortingStrategy):
    def sort(self, data):
        return f"Sorting {data} using Bubble Sort algorithm"

class QuickSort(SortingStrategy):
    def sort(self, data):
        return f"Sorting {data} using Quick Sort algorithm"

class MergeSort(SortingStrategy):
    def sort(self, data):
        return f"Sorting {data} using Merge Sort algorithm"

class SortingContext:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def sort_data(self, data):
        return self.strategy.sort(data)

# Demonstrating strategy pattern
data = [64, 34, 25, 12, 22, 11, 90]
context = SortingContext(BubbleSort())

print("Strategy Pattern with Polymorphism:")
print(context.sort_data(data))

context.set_strategy(QuickSort())
print(context.sort_data(data))

context.set_strategy(MergeSort())
print(context.sort_data(data))

print("\n" + "=" * 60)
print("POLYMORPHISM LESSON COMPLETE")
print("=" * 60)
print("Key Takeaways:")
print("• Polymorphism allows one interface to work with multiple types")
print("• Method overriding enables runtime polymorphism")
print("• Duck typing provides flexible polymorphism")
print("• Abstract base classes enforce interface contracts")
print("• Operator overloading enables natural syntax")
print("• Polymorphism improves code flexibility and maintainability")