# Python OOP — Classes, Objects, and the __init__ Method

**Lecture 3 Practice Notes**

---

## Table of Contents

- [What is a Class](#what-is-a-class)
- [What is an Object](#what-is-an-object)
- [The __init__ Method](#the-__init__-method)
- [The self Parameter](#the-self-parameter)
- [What Does print(self) Show](#what-does-printself-show)
- [Today's Practice Code](#todays-practice-code)
- [Code Breakdown Line by Line](#code-breakdown-line-by-line)
- [Output Explained](#output-explained)
- [Extended Examples](#extended-examples)
- [Common Mistakes](#common-mistakes)
- [Key Takeaways](#key-takeaways)

---

## What is a Class

A class is a blueprint or template for creating objects. It defines the structure and behavior that every object created from it will have. Think of a class like a cookie cutter — the cutter is the class, and every cookie made from it is an object.

```python
class Student:
    pass
```

This defines an empty class named `Student`. No attributes, no methods, but it is a valid class.

---

## What is an Object

An object is a real instance created from a class. When you write `s1 = Student()`, Python creates a new object in memory using the `Student` blueprint and assigns it to the variable `s1`.

Every time you call `Student()`, a brand new, separate object is created at a unique memory address.

```python
s1 = Student()
s2 = Student()

print(s1)   # <__main__.Student object at 0x...>
print(s2)   # <__main__.Student object at 0x...>  (different address)
```

`s1` and `s2` are two completely separate objects even though they were created from the same class.

---

## The __init__ Method

`__init__` is a special method in Python classes. It is called a **constructor** or **initializer**. Python calls this method automatically the moment a new object is created. You do not have to call it manually.

Its job is to set up the initial state of the object — assigning starting values to attributes and running any setup code needed when the object first comes into existence.

```python
class Student:
    def __init__(self):
        print("Object was created")
```

When you write `s1 = Student()`, Python internally does two things in order: first it creates the object in memory, then it immediately calls `__init__` on that new object.

The double underscores on both sides (`__init__`) mark it as a **dunder method** (short for double underscore). Python has many such special methods. They are never called by name directly — Python triggers them automatically in response to specific events.

---

## The self Parameter

`self` is a reference to the current object that is being created or used. It is always the first parameter of any method inside a class, including `__init__`.

When you call `Student()`, Python automatically passes the newly created object as the first argument to `__init__`. You do not pass it manually. Python handles it behind the scenes.

The name `self` is a convention, not a keyword. You could technically use any name, but using `self` is a universal standard in Python and you should always follow it.

```python
class Student:
    def __init__(self):
        # here, self refers to the object that was just created
        self.name = "Unknown"   # attaching an attribute to the object
```

---

## What Does print(self) Show

When you write `print(self)` inside `__init__`, Python prints the default string representation of the object. This looks like:

```
<__main__.Student object at 0x000001A3B4C5D6E7>
```

This output tells you three things:

- `__main__` is the module where the class is defined (the current script)
- `Student` is the class name
- `0x000001A3B4C5D6E7` is the memory address where this object is stored in RAM (in hexadecimal)

This is useful for confirming that the object exists in memory at the moment `__init__` runs.

---

## Today's Practice Code

```python
class Student:
    def __init__(self):
        print(self)
        print("object was created")


s1 = Student()
```

---

## Code Breakdown Line by Line

```python
class Student:
```
Defines a new class named `Student`. Everything indented under this belongs to the class.

```python
    def __init__(self):
```
Defines the constructor method. `self` here refers to the new object being built. Python will call this automatically when `Student()` is called.

```python
        print(self)
```
Prints the memory address and class information of the object. At this moment, `self` is the brand new object that Python just created before calling `__init__`.

```python
        print("object was created")
```
A simple confirmation message showing that `__init__` ran successfully.

```python
s1 = Student()
```
This single line does three things in sequence: Python allocates memory for a new `Student` object, calls `__init__` with that object passed as `self`, and then assigns the object to the variable `s1`.

---

## Output Explained

```
<__main__.Student object at 0x7f3a2b1c4d50>
object was created
```

The first line is the result of `print(self)`. The memory address shown will be different every time you run the program because Python allocates memory dynamically. The second line confirms that `__init__` ran to completion.

---

## Extended Examples

### Passing Data into __init__

```python
class Student:
    def __init__(self, name, age):
        print(self)
        print("object was created")
        self.name = name
        self.age = age


s1 = Student("Rahim", 20)
s2 = Student("Karim", 22)

print(s1.name)   # Rahim
print(s2.name)   # Karim
```

Here, each object stores its own `name` and `age`. The data is attached to `self`, meaning it belongs to that specific object alone.

### Creating Multiple Objects

```python
class Student:
    def __init__(self, name):
        self.name = name
        print(f"Student created: {self.name}")


s1 = Student("Alice")
s2 = Student("Bob")
s3 = Student("Charlie")
```

Output:
```
Student created: Alice
Student created: Bob
Student created: Charlie
```

Every call to `Student()` triggers `__init__` independently. Three calls, three executions of `__init__`.

### Verifying self is the Object

```python
class Student:
    def __init__(self):
        print(f"Inside __init__, self is: {self}")


s1 = Student()
print(f"Outside, s1 is: {s1}")
```

Output:
```
Inside __init__, self is: <__main__.Student object at 0x...>
Outside, s1 is: <__main__.Student object at 0x...>
```

Both lines show the exact same memory address. This confirms that `self` inside `__init__` and `s1` outside are pointing to the same object in memory.

---

## Common Mistakes

### Forgetting self as the first parameter

```python
# Wrong
class Student:
    def __init__():          # missing self
        print("created")

s1 = Student()               # TypeError: __init__() takes 0 positional arguments but 1 was given
```

Python always passes the object itself as the first argument. If you forget `self`, there is no parameter to receive it and Python raises a TypeError.

### Calling __init__ manually

```python
class Student:
    def __init__(self):
        print("created")

s1 = Student()
s1.__init__()    # this works but is incorrect practice
```

You should never call `__init__` manually. Python calls it for you automatically when the object is created. Calling it again would re-run initialization logic unnecessarily.

### Confusing the class with the object

```python
class Student:
    pass

print(Student)    # <class '__main__.Student'>   — this is the class itself
s1 = Student()
print(s1)         # <__main__.Student object at 0x...>  — this is an object
```

`Student` is the class (the blueprint). `s1` is an instance (an actual object built from the blueprint). They are different things.

---

## Key Takeaways

A class is a blueprint. An object is a real instance built from that blueprint. `__init__` runs automatically whenever a new object is created. `self` always refers to the specific object being created or used. `print(self)` shows the memory address of the object, proving it exists. Every object created from the same class is independent and stored at a different memory address. You can create as many objects from one class as you need, each with its own data.

---

## Practice Challenge

Try extending today's code with the following additions and observe the output.

```python
class Student:
    def __init__(self, name, roll):
        print(self)
        print(f"New student created: {name}, Roll: {roll}")
        self.name = name
        self.roll = roll


s1 = Student("Rahim", 101)
s2 = Student("Karim", 102)

print(s1.name, s1.roll)
print(s2.name, s2.roll)
```

Questions to answer after running this: Are the memory addresses of `s1` and `s2` the same or different? How many times did `__init__` run? What happens if you create 10 objects in a loop?

---

**Lecture:** L3
**Topic:** Python OOP — Classes, Objects, and the __init__ Method
**Language:** Python 3