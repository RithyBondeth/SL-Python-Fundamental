# Object-Oriented Programming (OOP) - Inheritance in Python

print("=== INHERITANCE IN PYTHON ===\n")

# 1. BASIC INHERITANCE
print("1. Basic Inheritance:")
print("-" * 20)

# Parent class (Base class / Superclass)
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.is_alive = True

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

    def make_sound(self):
        return f"{self.name} makes a sound"

    def get_info(self):
        return f"{self.name} is a {self.species}"

# Child class (Derived class / Subclass)
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed

    def make_sound(self):  # Method overriding
        return f"{self.name} barks: Woof! Woof!"

    def fetch(self):  # New method specific to Dog
        return f"{self.name} fetches the ball"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):  # Method overriding
        return f"{self.name} meows: Meow! Meow!"

    def climb(self):  # New method specific to Cat
        return f"{self.name} climbs the tree"

# Create objects
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Orange")

print(f"Dog info: {dog.get_info()}")
print(f"Dog breed: {dog.breed}")
print(dog.eat())           # Inherited method
print(dog.make_sound())    # Overridden method
print(dog.fetch())         # Dog-specific method

print(f"\nCat info: {cat.get_info()}")
print(f"Cat color: {cat.color}")
print(cat.sleep())         # Inherited method
print(cat.make_sound())    # Overridden method
print(cat.climb())         # Cat-specific method
print()

# 2. MULTILEVEL INHERITANCE
print("2. Multilevel Inheritance:")
print("-" * 27)

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        return f"{self.brand} {self.model} started"

    def stop(self):
        self.is_running = False
        return f"{self.brand} {self.model} stopped"

    def get_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
        self.fuel_level = 100

    def drive(self):
        if self.is_running:
            self.fuel_level -= 10
            return f"Driving the {self.brand} {self.model}. Fuel: {self.fuel_level}%"
        return "Car needs to be started first"

    def refuel(self):
        self.fuel_level = 100
        return f"{self.brand} {self.model} refueled to 100%"

class SportsCar(Car):
    def __init__(self, brand, model, year, doors, max_speed):
        super().__init__(brand, model, year, doors)
        self.max_speed = max_speed
        self.turbo_mode = False

    def activate_turbo(self):
        self.turbo_mode = True
        return f"Turbo mode activated! Max speed: {self.max_speed} mph"

    def deactivate_turbo(self):
        self.turbo_mode = False
        return "Turbo mode deactivated"

    def race(self):
        if self.turbo_mode:
            return f"{self.brand} {self.model} racing at {self.max_speed} mph!"
        return f"{self.brand} {self.model} racing at normal speed"

# Create sports car
sports_car = SportsCar("Ferrari", "488 GTB", 2023, 2, 205)

print(sports_car.get_info())        # From Vehicle
print(sports_car.start())           # From Vehicle
print(sports_car.drive())           # From Car
print(sports_car.activate_turbo())  # From SportsCar
print(sports_car.race())            # From SportsCar
print(sports_car.refuel())          # From Car
print()

# 3. MULTIPLE INHERITANCE
print("3. Multiple Inheritance:")
print("-" * 23)

class Flyable:
    def __init__(self):
        self.can_fly = True

    def fly(self):
        return "Flying through the sky"

    def land(self):
        return "Landing safely"

class Swimmable:
    def __init__(self):
        self.can_swim = True

    def swim(self):
        return "Swimming in the water"

    def dive(self):
        return "Diving underwater"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        Animal.__init__(self, name, "Duck")
        Flyable.__init__(self)
        Swimmable.__init__(self)

    def make_sound(self):
        return f"{self.name} quacks: Quack! Quack!"

    def migrate(self):
        return f"{self.name} is migrating south for winter"

# Create duck
duck = Duck("Donald")

print(duck.get_info())     # From Animal
print(duck.make_sound())   # Overridden
print(duck.fly())          # From Flyable
print(duck.swim())         # From Swimmable
print(duck.eat())          # From Animal
print(duck.migrate())      # Duck-specific
print(f"Can fly: {duck.can_fly}, Can swim: {duck.can_swim}")
print()

# 4. METHOD RESOLUTION ORDER (MRO)
print("4. Method Resolution Order (MRO):")
print("-" * 35)

class A:
    def method(self):
        return "Method from class A"

class B(A):
    def method(self):
        return "Method from class B"

class C(A):
    def method(self):
        return "Method from class C"

class D(B, C):
    pass

# Create object and check MRO
d = D()
print(f"D.mro(): {D.mro()}")
print(f"D.__mro__: {D.__mro__}")
print(f"Method called: {d.method()}")
print()

# 5. SUPER() IN DEPTH
print("5. Using super() in Depth:")
print("-" * 26)

class Shape:
    def __init__(self, color):
        self.color = color
        print(f"Shape constructor called with color: {color}")

    def area(self):
        return 0

    def description(self):
        return f"A {self.color} shape"

class Rectangle(Shape):
    def __init__(self, color, width, height):
        print(f"Rectangle constructor called")
        super().__init__(color)  # Call parent constructor
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def description(self):
        return f"{super().description()} - Rectangle with area {self.area()}"

class Square(Rectangle):
    def __init__(self, color, side):
        print(f"Square constructor called")
        super().__init__(color, side, side)  # Call Rectangle constructor
        self.side = side

    def description(self):
        return f"{super().description()} - It's actually a square!"

# Create square
square = Square("red", 5)
print(f"\nSquare area: {square.area()}")
print(square.description())
print()

# 6. ABSTRACT BASE CLASSES AND POLYMORPHISM
print("6. Abstract Base Classes and Polymorphism:")
print("-" * 42)

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    def get_info(self):
        return f"Employee: {self.name} (ID: {self.employee_id})"

class FullTimeEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.annual_salary = annual_salary

    def calculate_salary(self):
        return self.annual_salary / 12  # Monthly salary

    def get_role(self):
        return "Full-time Employee"

class PartTimeEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_per_month):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_per_month = hours_per_month

    def calculate_salary(self):
        return self.hourly_rate * self.hours_per_month

    def get_role(self):
        return "Part-time Employee"

class Contractor(Employee):
    def __init__(self, name, employee_id, project_rate):
        super().__init__(name, employee_id)
        self.project_rate = project_rate

    def calculate_salary(self):
        return self.project_rate

    def get_role(self):
        return "Contractor"

# Create different types of employees
employees = [
    FullTimeEmployee("Alice Johnson", "FT001", 60000),
    PartTimeEmployee("Bob Smith", "PT001", 25, 80),
    Contractor("Charlie Brown", "CT001", 5000)
]

# Polymorphism in action
print("Employee Payroll:")
print("-" * 20)
for employee in employees:
    print(f"{employee.get_info()}")
    print(f"Role: {employee.get_role()}")
    print(f"Monthly Pay: ${employee.calculate_salary():.2f}")
    print("-" * 30)

# 7. CHECKING INHERITANCE RELATIONSHIPS
print("7. Checking Inheritance Relationships:")
print("-" * 37)

print(f"isinstance(dog, Animal): {isinstance(dog, Animal)}")
print(f"isinstance(dog, Dog): {isinstance(dog, Dog)}")
print(f"isinstance(dog, Cat): {isinstance(dog, Cat)}")

print(f"issubclass(Dog, Animal): {issubclass(Dog, Animal)}")
print(f"issubclass(SportsCar, Vehicle): {issubclass(SportsCar, Vehicle)}")
print(f"issubclass(Duck, Flyable): {issubclass(Duck, Flyable)}")
print(f"issubclass(Duck, Swimmable): {issubclass(Duck, Swimmable)}")

print(f"\ndog.__class__.__bases__: {dog.__class__.__bases__}")
print(f"SportsCar.__bases__: {SportsCar.__bases__}")
print(f"Duck.__bases__: {Duck.__bases__}")
print()

# 8. PROPERTY INHERITANCE
print("8. Property Inheritance:")
print("-" * 22)

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance  # Protected attribute

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative")

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount}. New balance: ${self._balance}"

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Invalid withdrawal"

class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest
        return f"Interest added: ${interest:.2f}. New balance: ${self._balance:.2f}"

class CheckingAccount(BankAccount):
    def __init__(self, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if 0 < amount <= (self._balance + self.overdraft_limit):
            self._balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._balance}"
        return "Withdrawal exceeds overdraft limit"

# Create accounts
savings = SavingsAccount("John Doe", 1000, 0.03)
checking = CheckingAccount("Jane Smith", 500, 200)

print(f"Savings balance: ${savings.balance}")
print(savings.add_interest())
print(f"New savings balance: ${savings.balance}")

print(f"\nChecking balance: ${checking.balance}")
print(checking.withdraw(600))  # Uses overdraft
print(f"Checking balance after overdraft: ${checking.balance}")
print()

print("=== INHERITANCE CONCEPTS SUMMARY ===")
print("1. Inheritance: Child class inherits attributes and methods from parent class")
print("2. super(): Calls methods from parent class")
print("3. Method Overriding: Child class can redefine parent class methods")
print("4. Multilevel Inheritance: Class inherits from another inherited class")
print("5. Multiple Inheritance: Class inherits from multiple parent classes")
print("6. MRO: Method Resolution Order determines which method is called")
print("7. Abstract Classes: Classes that cannot be instantiated directly")
print("8. Polymorphism: Same method name behaves differently in different classes")
print("9. isinstance(): Check if object is instance of a class")
print("10. issubclass(): Check if class is subclass of another class")