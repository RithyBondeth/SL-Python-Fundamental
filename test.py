# from time import sleep


# class Car:
#     pass

# car1 = Car()
# car2 = Car()

# print(type(car1))
# print(type(car2))
# print(f"Object 1: {car1}")
# print (f"Object 2: {car2}")
# print(f"Are they the same object? {car1 is car2}")

# class Dog:
#     species = "Canis Lupus"
#     total_dog = 0

#     def bark(self):
#         return "Woof! Woof!"

#     def get_species(self):
#         return f"I'm a {self.species}"

# dog1 = Dog()
# dog2 = Dog()

# print(Dog.species)
# print(dog1.species)
# print(dog2.species)
# print(dog1.bark())
# print(dog1.get_species())

# dog1.name = "Buddy"
# dog1.age = 3
# dog1.breed = "Golden Retriever"

# print(f"\ndog1: {dog1.name}, {dog1.age}, {dog1.breed}")

# class Person:
#     human_species = "Homo sapiens"

#     def __init__(self, name, age, city):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.is_adult = age >= 18

#     def introduce(self):
#         status = "adult" if self.is_adult else "minor"  
#         return f"Hi I'm {self.name}, {self.age} years old from {self.city}. I'm an {status}"

#     def have_birthday(self):
#         self.age += 1
#         self.is_adult = self.age >= 18
#         return f"Happy Birthday {self.name}! Now {self.age} years old."

#     def move_to(self, new_city):
#         old_city = self.city
#         self.city = new_city
#         return f"{self.name} moved from {old_city} to {new_city}"
    
#     def get_info(self):
#         return {
#             "name": self.name,
#             "age": self.age,
#             "city": self.city,
#             "is_adult": self.is_adult,
#             "species": self.human_species
#         }

# person = Person(name="Bondeth", age=23, city="Phnom Penh")
# print(person.introduce())
# print(person.have_birthday())
# print(person.move_to(new_city="Perth, Australia"))

# info = person.get_info()
# print(info['name'])

# print("Complex Example - Bank Account")

# class BankAccount:
#     bank_name = 'Python Bank'
#     interest_rate = 0.02

#     def __init__(self, account_holder, initial_balance=0):
#         self.account_holder = account_holder
#         self.balance = initial_balance
#         self.transaction_history = []
#         self.account_number = self._generate_account_number()
#         self._add_transaction("Account Opened", initial_balance)


#     def _generate_account_number(self):
#         import random
#         return f"PB{random.randint(100000, 999999)}"

#     def _add_transaction(self, description, amount):
#         self.transaction_history.append({
#           "description": description  ,
#           "amount": amount,
#           "balance_after": self.balance,
#         })

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self._add_transaction("Deposit", amount)
#             return f"Deposited ${amount}. New balance ${self.balance}"
#         else:
#             return "Invalid withdrawal amount or insufficient funds"

#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             self._add_transaction("Withdraw", -amount)
#             return f"Deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "Invalid withdrawal amount or insufficient funds"


#     def get_balance(self):
#         return f"Your current balance is: ${self.balance}"

#     def get_account_info(self):
#         return f"""
#             Account Information:
#             - Bank: {self.bank_name}
#             - Account Holder: {self.account_holder}
#             - Account Number: {self.account_number}
#             - Current Balance: ${self.balance}
#             - Interest Rate: {self.interest_rate * 100}%
#         """

# bondeth = BankAccount('Bondeth')
# bondeth.deposit(100000)
# bondeth.withdraw(50000)
# print(bondeth.get_account_info())
# bondeth.withdraw(40000)
# print(bondeth.get_balance())

# class Counter:
#     def __init__(self, start_value=0):
#         self.value = start_value

#     def increment(self):
#         self.value += 1
#         return self.value
    
#     def decrement(self):
#         self.value -= 1
#         return self.value

#     def reset(self):
#         self.value = 0
#         return "Counter reset to 0"
    
#     def get_value(self):
#         return self.value

# counter1 = Counter(10)

# print(f"Counter 1 initial: {counter1.get_value()}")
# print(f"Counter 1 increment: {counter1.increment()}")
# print(f"Counter 1 decrement: {counter1.decrement()}")
# print(f"Counter 1 decrement: {counter1.decrement()}")

# print(f"Final Value of Counter 1: {counter1.get_value()}")

# class Student:
#     school_name = "Python Highschool"
#     total_student = 0

#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade
#         self.subjects = []
#         Student.total_student += 1

#     def add_subject(self, subject):
#         self.subjects.append(subject)
#         return f"{subject} add to {self.name}'s student"

#     def get_info(self):
#         return f"{self.name} - Grade {self.grade} at {self.school_name}. Subjects: {self.subjects}"

#     @classmethod
#     def get_total_students(cls):
#         return f"Total students in {cls.school_name}: {cls.total_student}"

    
# stu_bondeth = Student("Bondeth", "Bachelor's Degree")
# stu_emily = Student("Emily", "Master's Degree")
# stu_salyna = Student('Salyna', 'Diploma')

# stu_bondeth.add_subject("Data Structure and Algorithms")
# stu_emily.add_subject(['NumPy', 'Matplotlib'])

# print(stu_bondeth.get_info())
# print(stu_salyna.get_info())
# print(stu_emily.get_info())

# print(Student.get_total_students())

from symbol import decorators


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


class Dog(Animal):

    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def make_sound(self):
        return f"{self.name} barks: Woof! Woof!"

    def eat(self):
        return f"{self.name} is eating as dog"

    def get_dog_info(self):
        return f"{self.get_info()} and breed: {self.breed}"

    
dog = Dog(name='Lucky', species='Orange' ,breed='Orange')

print(f"{dog.get_info()}")
print(dog.make_sound())
print(dog.eat())

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        self.is_running = True
        return f"{self.brand} {self.model} is running"

    def stop(self):
        self.is_running = False
        return f"{self.brand} {self.model} stopped"

    def get_info(self):
        return f"Year: {self.year} - Brand: {self.brand} - Model: {self.model}"


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
        self.fuel_travel = 100

    def drive(self):
        if self.is_running: 
            self.fuel_travel -= 10
            return f"Driving the {self.brand} {self.model}. Fuel: {self.fuel_travel}%"
        return "Car needs to be started first"

    def refuel(self):
        self.fuel_travel = 100
        return f"{self.brand} {self.model} refueled to 100%"

v1 = Vehicle('Toyota', 'Bz4x', 2025)
print(v1.get_info())
print(v1.start())

bmw = Car('BMW', 'BMW M4', 2024, 2)
bmw.start()
print(bmw.drive())
print(bmw.refuel())
print(bmw.get_info())

class SuperCar(Car):   
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
        return f"{self.brand} {self.model} racing at normal speed!"

    def get_super_car_info(self):
        return f"{self.get_info()} - Door: {self.doors} - Max Speed: {self.max_speed}"

    
xiaomi_su7_max = SuperCar('Xiaomi', 'SU7 Max', 2025, 4, 500)
print(xiaomi_su7_max.get_super_car_info())
xiaomi_su7_max.activate_turbo()
print(f"Racing After Activated Turbo: {xiaomi_su7_max.race()}")
        
xiaomi_su7_max.deactivate_turbo()
print(f"Racing After Deactivated Turbo: {xiaomi_su7_max.race()}")


class Flyable:
    def __init__(self):
        self.can_fly = True
    
    def fly(self):
        return "Flying through the sky"
    
    def land(self):
        return "Landing safely"
    
class Swimmable:
    def __init__(self) -> None:
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


duck = Duck(name="Donald")

