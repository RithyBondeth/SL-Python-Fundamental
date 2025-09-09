print(10 > 9)
print(10 <= 9)
print(5 == 5)

x = 10 
y = 5
if x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is smaller than {y}")

a = "Hello"
b = 15

print(bool(a))
print(bool(b))

# Must values are return True. But the following values are return False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class MyClass():
    def __len__(self):
        return 0


myObj = MyClass() 
print("My Object: ", bool(myObj))

# Function can return boolean
def myFunction():
    return True


if myFunction():
    print("YES")
else:
    print("NO")

num = 20
print(isinstance(num, int))
print(isinstance(num, float))
print(isinstance(num, bool))