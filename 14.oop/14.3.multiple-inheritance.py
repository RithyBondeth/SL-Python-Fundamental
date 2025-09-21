# Multiple Inheritance in Python
# Multiple inheritance allows a class to inherit from more than one parent class

print("=== Multiple Inheritance Examples ===\n")

# Example 1: Basic Multiple Inheritance
print("1. Basic Multiple Inheritance:")

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal constructor called for {name}")

    def eat(self):
        return f"{self.name} is eating"

    def sleep(self):
        return f"{self.name} is sleeping"

class Mammal:
    def __init__(self, warm_blooded=True):
        self.warm_blooded = warm_blooded
        print(f"Mammal constructor called")

    def give_birth(self):
        return "Giving birth to live babies"

    def breathe(self):
        return "Breathing air through lungs"

class Bird:
    def __init__(self, can_fly=True):
        self.can_fly = can_fly
        print(f"Bird constructor called")

    def lay_eggs(self):
        return "Laying eggs"

    def fly(self):
        return "Flying in the sky" if self.can_fly else "Cannot fly"

# Multiple inheritance: inheriting from both Mammal and Bird
class Bat(Animal, Mammal, Bird):
    def __init__(self, name, can_fly=True):
        Animal.__init__(self, name)
        Mammal.__init__(self, warm_blooded=True)
        Bird.__init__(self, can_fly)
        self.nocturnal = True

    def echolocate(self):
        return f"{self.name} is using echolocation"

# Create a bat instance
fruit_bat = Bat("Fruit Bat")
print(f"Created: {fruit_bat.name}")
print(f"Warm blooded: {fruit_bat.warm_blooded}")
print(f"Can fly: {fruit_bat.can_fly}")
print(f"Animal behavior: {fruit_bat.eat()}")
print(f"Mammal behavior: {fruit_bat.give_birth()}")
print(f"Bird behavior: {fruit_bat.fly()}")
print(f"Unique behavior: {fruit_bat.echolocate()}")
print()

# Example 2: Method Resolution Order (MRO)
print("2. Method Resolution Order (MRO):")

class A:
    def show(self):
        return "Class A"

class B(A):
    def show(self):
        return "Class B"

class C(A):
    def show(self):
        return "Class C"

class D(B, C):
    pass

class E(C, B):
    pass

# Check MRO for different inheritance orders
d = D()
e = E()

print(f"D inherits from B, C (in that order)")
print(f"D.show() returns: {d.show()}")
print(f"D MRO: {[cls.__name__ for cls in D.mro()]}")
print()

print(f"E inherits from C, B (in that order)")
print(f"E.show() returns: {e.show()}")
print(f"E MRO: {[cls.__name__ for cls in E.mro()]}")
print()

# Example 3: Diamond Problem
print("3. Diamond Problem Resolution:")

class Vehicle:
    def __init__(self):
        print("Vehicle constructor")
        self.engine = "Generic Engine"

    def start(self):
        return "Vehicle starting..."

class LandVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        print("LandVehicle constructor")
        self.wheels = 4

    def drive(self):
        return "Driving on land"

class WaterVehicle(Vehicle):
    def __init__(self):
        super().__init__()
        print("WaterVehicle constructor")
        self.propeller = True

    def sail(self):
        return "Sailing on water"

# Amphibious vehicle inherits from both LandVehicle and WaterVehicle
class AmphibiousVehicle(LandVehicle, WaterVehicle):
    def __init__(self):
        super().__init__()  # Uses MRO to call constructors properly
        print("AmphibiousVehicle constructor")
        self.amphibious = True

    def start(self):
        base_start = super().start()
        return f"{base_start} (Amphibious mode)"

print("Creating amphibious vehicle:")
amphibious = AmphibiousVehicle()
print(f"Engine: {amphibious.engine}")
print(f"Wheels: {amphibious.wheels}")
print(f"Propeller: {amphibious.propeller}")
print(f"Land capability: {amphibious.drive()}")
print(f"Water capability: {amphibious.sail()}")
print(f"Starting: {amphibious.start()}")
print(f"MRO: {[cls.__name__ for cls in AmphibiousVehicle.mro()]}")
print()

# Example 4: Mixins Pattern
print("4. Mixins Pattern:")

class SerializableMixin:
    def to_dict(self):
        return {key: value for key, value in self.__dict__.items()
                if not key.startswith('_')}

    def to_string(self):
        items = [f"{k}={v}" for k, v in self.to_dict().items()]
        return f"{self.__class__.__name__}({', '.join(items)})"

class LoggableMixin:
    def log(self, message):
        return f"[{self.__class__.__name__}] {message}"

class TimestampMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        import datetime
        self.created_at = datetime.datetime.now()

    def age(self):
        import datetime
        delta = datetime.datetime.now() - self.created_at
        return f"Created {delta.total_seconds():.2f} seconds ago"

class User(SerializableMixin, LoggableMixin, TimestampMixin):
    def __init__(self, name, email):
        super().__init__()
        self.name = name
        self.email = email

    def greet(self):
        return f"Hello, I'm {self.name}"

# Create user with multiple mixin capabilities
user = User("Alice", "alice@example.com")
print(f"User greeting: {user.greet()}")
print(f"Serialized: {user.to_string()}")
print(f"Logging: {user.log('User created successfully')}")
print(f"Timestamp: {user.age()}")
print()

# Example 5: Cooperative Inheritance with super()
print("5. Cooperative Inheritance:")

class Shape:
    def __init__(self, color="white"):
        print(f"Shape.__init__ called with color: {color}")
        self.color = color

class Rectangle(Shape):
    def __init__(self, width, height, **kwargs):
        print(f"Rectangle.__init__ called with width: {width}, height: {height}")
        super().__init__(**kwargs)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Drawable:
    def __init__(self, line_style="solid", **kwargs):
        print(f"Drawable.__init__ called with line_style: {line_style}")
        super().__init__(**kwargs)
        self.line_style = line_style

    def draw(self):
        return f"Drawing with {self.line_style} lines"

class DrawableRectangle(Rectangle, Drawable):
    def __init__(self, width, height, **kwargs):
        print(f"DrawableRectangle.__init__ called")
        super().__init__(width, height, **kwargs)

    def render(self):
        return f"Rendering {self.color} rectangle ({self.width}x{self.height}) with {self.line_style} lines"

# Create drawable rectangle using cooperative inheritance
print("Creating drawable rectangle:")
drawable_rect = DrawableRectangle(10, 5, color="blue", line_style="dashed")
print(f"Area: {drawable_rect.area()}")
print(f"Drawing: {drawable_rect.draw()}")
print(f"Rendering: {drawable_rect.render()}")
print(f"MRO: {[cls.__name__ for cls in DrawableRectangle.mro()]}")
print()

# Example 6: Multiple Inheritance Best Practices
print("6. Best Practices:")

# Use isinstance() and hasattr() for type checking
print("Type checking with multiple inheritance:")
print(f"fruit_bat is Animal: {isinstance(fruit_bat, Animal)}")
print(f"fruit_bat is Mammal: {isinstance(fruit_bat, Mammal)}")
print(f"fruit_bat is Bird: {isinstance(fruit_bat, Bird)}")
print(f"fruit_bat has echolocate: {hasattr(fruit_bat, 'echolocate')}")
print(f"fruit_bat has lay_eggs: {hasattr(fruit_bat, 'lay_eggs')}")
print()

# Demonstrate method resolution
print("Method resolution in action:")
class Base1:
    def method(self):
        return "Base1.method"

class Base2:
    def method(self):
        return "Base2.method"

class Child(Base1, Base2):
    pass

child = Child()
print(f"Child inherits from Base1, Base2")
print(f"child.method() returns: {child.method()}")
print(f"First parent's method is called due to MRO")
print()

print("=== Multiple Inheritance Summary ===")
print("Key Points:")
print("1. A class can inherit from multiple parent classes")
print("2. Method Resolution Order (MRO) determines which method is called")
print("3. Use super() for cooperative inheritance")
print("4. Mixins provide a way to add functionality to classes")
print("5. Diamond problem is resolved automatically by Python's MRO")
print("6. Always use isinstance() for type checking with multiple inheritance")