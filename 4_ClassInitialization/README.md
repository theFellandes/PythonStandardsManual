Python Standards Manifesto
=====================
Class Initialization
=====================

This chapter is about class initialization in Python. 

### Abstract
* * In class initialization, use dataclass :)

To initialize a class, class definition should be surrounded with 2 blank lines and method definitions 
inside a class are surrounded by a single blank line.

```python
import os

# 2 blank lines after import statement
class MyClass:
    def __init__(self):
        pass
    
    # Single blank line between methods
    
    def my_method(self):
        pass
# Single blank line in the end of class definition
```

* My suggestion to class initialization is that instead of using `__init__` method, usage of dataclass is preferable.
* This is because dataclass uses type hints and can implement a validation system inside `__post_init__` method. 
* Dataclass offers less boilerplate code, and it is more readable compared to `__init__`

```python
from dataclasses import dataclass


@dataclass
class MyClass:
    attr1: str
    attr2: int

```

* Another suggestion is that, instead of using default constructor, usage of a staticmethod as a constructor with type hints is more understandable.
```python
from dataclasses import dataclass


@dataclass
class MyClass:
    attr1: str
    attr2: int
    
    @staticmethod
    def create_my_class(attr1: str, attr2: int) -> MyClass:
        return MyClass(attr1, attr2)
```

* With dataclass approach, `__eq__` doesn't need to be overridden to compare 2 objects since dataclass handles `__eq__` and `__repr__`

```python
class Person:
    def __init__(self, first_name, last_name, age, job):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job = job
first_person = Person("John", "Doe", 30, "Software Engineer")
second_person = Person("John", "Doe", 30, "Software Engineer")
print(first_person == second_person) # False
```
These 2 objects are not equal since `__eq__` is not overridden.

In the dataclass case, it's not necessary to override `__eq__` since dataclass handles it.
```python
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    job: str

first_person = Person("John", "Doe", 30, "Software Engineer")
second_person = Person("John", "Doe", 30, "Software Engineer")
print(first_person == second_person) # True
```

* Data validation example in Dataclasses
```python
from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int
    job: str
    
    def __post_init__(self):
        if not self.validate_age():
            raise ValueError("Age cannot be negative")
    
    def validate_age(self):
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        return True

```