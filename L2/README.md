In object-oriented programming, a constructor is a special method used to initialize the state of an object when it is created. It sets up initial values for the object's attributes and performs any other setup tasks. In Python, the constructor is defined using the __init__() method.

---

1. What is a Constructor?

- constructor is automatically called when you create an instance (object) of a class.
- Its main purpose is to initialize the instance members (attributes) of the class.
- Every class must have a constructor; if you don't define one, Python provides a default (empty) constructor.
- You can have multiple constructors? No – Python does not support multiple constructors directly, but you can simulate them using default arguments or class methods.

Types of Constructors

1. Non-parameterized (Default) Constructor
   - Takes no arguments (except self).
   - If you don't define any __init__, Python automatically provides one that does nothing.
2. Parameterized Constructor
   - Takes one or more arguments (besides self).
   - Used to initialize object attributes with specific values at creation time.

---

2. Python's __init__ Method

- __init__ is a reserved method in Python classes.
- It is called immediately after the object is created (but before it is returned to the caller).
- The first parameter is always self, which refers to the current instance.
- You can pass any number of additional arguments when creating an object; these must match the __init__ method's signature (except self).

Example of a Parameterized Constructor

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

# Creating objects – the __init__ method is called automatically
emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)

print(emp1.name, emp1.salary)  # Alice 50000
print(emp2.name, emp2.salary)  # Bob 60000
```

---

3. Non-parameterized (Default) Constructor

If you do not define an __init__ method, Python provides a default constructor that takes no arguments (except self) and performs no initialization.

Example (Implicit Default Constructor)

```python
class Employee:
    pass   # No constructor defined

emp1 = Employee()   # Works fine – uses the default constructor
emp2 = Employee()
```

Even though we didn't write a constructor, the objects are created. However, they have no attributes unless you add them later:

```python
emp1.name = "Alice"   # Adding attribute manually
print(emp1.name)      # Alice
```

If you define an __init__ that requires parameters but try to create an object without them, you'll get an error:

```python
class Employee:
    def __init__(self, name):
        self.name = name

# emp = Employee()   # TypeError: __init__ missing 1 argument
```

So a non-parameterized constructor is either the one you explicitly write with only self, or the implicit one provided by Python.

---

4. Parameterized Constructor

A parameterized constructor allows you to pass values at the time of object creation. These values are typically used to initialize the object's attributes.

Example

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(10, 5)
print(rect.area())   # 50
```

You can also provide default values to make some parameters optional:

```python
class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

r1 = Rectangle()        # uses defaults: length=1, width=1
r2 = Rectangle(5)       # length=5, width=1
r3 = Rectangle(5, 10)   # length=5, width=10
```

---

5. Instance Methods

- Instance methods are functions defined inside a class that operate on instances of that class.
- They always take self as the first parameter, which gives them access to the instance's attributes and other methods.
- They can modify object state or perform actions using the object's data.

Example

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # Instance method
    def display_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

    # Another instance method
    def give_raise(self, amount):
        self.salary += amount

emp = Employee("Alice", 50000)
emp.display_info()      # Name: Alice, Salary: 50000
emp.give_raise(5000)
emp.display_info()      # Name: Alice, Salary: 55000
```

Instance methods are the most common type of methods in Python classes.

---


| **Concept** | **Description** | **Example** |
|-------------|-------------|-------------|
| **Constructor** | Special method `__init__` called at object creation. Initializes attributes. | `def __init__(self, ...):` |
| **Non‑parameterized Constructor** | Constructor with no extra parameters (only self). | `def __init__(self):` or implicit default |
| **Parameterized Constructor** | Constructor that accepts arguments to set initial values. | `def __init__(self, name, age):` |
| **Instance Method** | Regular method that works on an instance; first parameter is self. | `def method(self):` |
