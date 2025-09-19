# Object-Oriented Programming (OOP) - Classes and Objects in Python

print("=== CLASSES AND OBJECTS IN PYTHON ===\n")

# 1. BASIC CLASS DEFINITION
print("1. Basic Class Definition:")
print("-" * 30)

class Car:
    pass

# Create objects (instances)
car1 = Car()
car2 = Car()

print(f"car1 type: {type(car1)}")
print(f"car2 type: {type(car2)}")
print(f"car1 object: {car1}")
print(f"car2 object: {car2}")
print(f"Are they the same object? {car1 is car2}")
print()

# 2. CLASS WITH ATTRIBUTES AND METHODS
print("2. Class with Attributes and Methods:")
print("-" * 40)

class Dog:
    # Class attribute (shared by all instances)
    species = "Canis lupus"
    total_dogs = 0

    def bark(self):
        return "Woof! Woof!"

    def get_species(self):
        return f"I am a {self.species}"

# Create dog objects
dog1 = Dog()
dog2 = Dog()

print(f"Dog species: {Dog.species}")
print(f"dog1 species: {dog1.species}")
print(f"dog2 species: {dog2.species}")
print(f"dog1 barks: {dog1.bark()}")
print(f"dog2 says: {dog2.get_species()}")

# Add instance attributes (unique to each object)
dog1.name = "Buddy"
dog1.age = 3
dog1.breed = "Golden Retriever"

dog2.name = "Max"
dog2.age = 5
dog2.breed = "German Shepherd"

print(f"\ndog1: {dog1.name}, {dog1.age} years old, {dog1.breed}")
print(f"dog2: {dog2.name}, {dog2.age} years old, {dog2.breed}")
print()

# 3. CLASS WITH __init__ METHOD (CONSTRUCTOR)
print("3. Class with __init__ Method (Constructor):")
print("-" * 45)

class Person:
    # Class attribute
    human_species = "Homo sapiens"

    def __init__(self, name, age, city):
        # Instance attributes
        self.name = name
        self.age = age
        self.city = city
        self.is_adult = age >= 18
        print(f"Person object created: {name}")

    def introduce(self):
        status = "adult" if self.is_adult else "minor"
        return f"Hi! I'm {self.name}, {self.age} years old from {self.city}. I'm an {status}."

    def have_birthday(self):
        self.age += 1
        self.is_adult = self.age >= 18
        return f"<� Happy birthday {self.name}! Now {self.age} years old."

    def move_to(self, new_city):
        old_city = self.city
        self.city = new_city
        return f"{self.name} moved from {old_city} to {new_city}"

    def get_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "city": self.city,
            "is_adult": self.is_adult,
            "species": self.human_species
        }

# Create person objects
person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 17, "London")
person3 = Person("Charlie", 30, "Tokyo")

print(f"\nPerson 1: {person1.introduce()}")
print(f"Person 2: {person2.introduce()}")
print(f"Person 3: {person3.introduce()}")

# Demonstrate methods
print(f"\n{person2.have_birthday()}")
print(f"Bob is now adult: {person2.is_adult}")

print(f"{person1.move_to('California')}")
print(f"Alice's new info: {person1.get_info()}")
print()

# 4. MORE COMPLEX EXAMPLE - BANK ACCOUNT
print("4. Complex Example - Bank Account:")
print("-" * 35)

class BankAccount:
    # Class attributes
    bank_name = "Python Bank"
    interest_rate = 0.02

    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transaction_history = []
        self.account_number = self._generate_account_number()
        self._add_transaction("Account opened", initial_balance)

    def _generate_account_number(self):
        import random
        return f"PB{random.randint(100000, 999999)}"

    def _add_transaction(self, description, amount):
        self.transaction_history.append({
            "description": description,
            "amount": amount,
            "balance_after": self.balance
        })

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self._add_transaction(f"Deposit", amount)
            return f"Deposited ${amount}. New balance: ${self.balance}"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self._add_transaction(f"Withdrawal", -amount)
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Invalid withdrawal amount or insufficient funds"

    def get_balance(self):
        return f"Account balance: ${self.balance}"

    def get_account_info(self):
        return f"""
Account Information:
- Bank: {self.bank_name}
- Account Holder: {self.account_holder}
- Account Number: {self.account_number}
- Current Balance: ${self.balance}
- Interest Rate: {self.interest_rate * 100}%
        """

    def get_transaction_history(self):
        print(f"Transaction History for {self.account_holder}:")
        for i, transaction in enumerate(self.transaction_history, 1):
            print(f"{i}. {transaction['description']}: ${transaction['amount']} (Balance: ${transaction['balance_after']})")

# Create bank accounts
account1 = BankAccount("John Smith", 1000)
account2 = BankAccount("Jane Doe", 500)

print(account1.get_account_info())
print(account1.deposit(250))
print(account1.withdraw(100))
print(account1.get_balance())

print(f"\n{account2.get_account_info()}")
print(account2.deposit(300))
print(account2.withdraw(50))

print("\n" + "="*50)
account1.get_transaction_history()
print()

# 5. UNDERSTANDING 'self' KEYWORD
print("5. Understanding 'self' Keyword:")
print("-" * 32)

class Counter:
    def __init__(self, start_value=0):
        self.value = start_value

    def increment(self):
        self.value += 1
        return self.value

    def decrement(self):
        self.value -= 1
        return self.value

    def reset(self):
        self.value = 0
        return "Counter reset to 0"

    def get_value(self):
        return self.value

# Create multiple counters
counter1 = Counter(10)
counter2 = Counter(100)

print(f"Counter 1 initial: {counter1.get_value()}")
print(f"Counter 2 initial: {counter2.get_value()}")

print(f"Counter 1 increment: {counter1.increment()}")
print(f"Counter 1 increment: {counter1.increment()}")
print(f"Counter 2 decrement: {counter2.decrement()}")

print(f"Counter 1 final: {counter1.get_value()}")
print(f"Counter 2 final: {counter2.get_value()}")
print()

# 6. CLASS VS INSTANCE ATTRIBUTES
print("6. Class vs Instance Attributes:")
print("-" * 33)

class Student:
    # Class attributes (shared by all instances)
    school_name = "Python High School"
    total_students = 0

    def __init__(self, name, grade):
        # Instance attributes (unique to each object)
        self.name = name
        self.grade = grade
        self.subjects = []
        Student.total_students += 1  # Modify class attribute

    def add_subject(self, subject):
        self.subjects.append(subject)
        return f"{subject} added to {self.name}'s subjects"

    def get_info(self):
        return f"{self.name} - Grade {self.grade} at {self.school_name}"

    @classmethod
    def get_total_students(cls):
        return f"Total students in {cls.school_name}: {cls.total_students}"

# Create students
student1 = Student("Emma", 10)
student2 = Student("Liam", 11)
student3 = Student("Olivia", 9)

print(f"School: {Student.school_name}")
print(Student.get_total_students())

student1.add_subject("Math")
student1.add_subject("Science")
student2.add_subject("English")
student2.add_subject("History")

print(f"\n{student1.get_info()}")
print(f"Emma's subjects: {student1.subjects}")
print(f"\n{student2.get_info()}")
print(f"Liam's subjects: {student2.subjects}")

print(f"\nTotal students: {Student.total_students}")
print()

print("=== KEY CONCEPTS SUMMARY ===")
print("1. Class: Blueprint/template for creating objects")
print("2. Object: Instance of a class with its own data")
print("3. self: Refers to the current instance")
print("4. __init__: Constructor method called when object is created")
print("5. Instance attributes: Unique to each object")
print("6. Class attributes: Shared by all objects of the class")
print("7. Methods: Functions that belong to the class")