Python Standards Manifesto
=====================
Naming Conventions
======================

1) Write self-explanatory variable names, avoid using single letter variable names and abbreviations. Never use l, o or I single-letter names as these can be mistaken for "1" and "0".
```
#  Do:
file_reader

#  Don't:
fr
l
o
I
```
2) Use snake_case for variable names and function names. Use CamelCase for class names. Use UPPERCASE for constants.
```
#  Do:
variable name-function name: file_reader, func_1
class name: UserClass
constant name: CONSTANT_VALUE

#  Don't:
variable name: fr
class name: userClass, user_class, userclass etc.
constant name: constant_value
```
3) Use single underscore for symbolize private attributes-functions for a function. Don't use __ notation to denote private since it causes complications. Explanation: A single leading underscore in front of a variable, a function or a method name means that these objects are used internally, and it's a syntax hint for a developer.
```
#  Do:
_private_attribute

#  Don't:
__private_attribute
```
4) Double leading underscores are called name mangling. Name mangling is a process by which the interpreter changes the attribute name to avoid naming collisions in subclasses. Name mangling breaks the dir() order of an object.
```python
class Car:
    def __init__(self):
        self.color = "red"
        self._speed = 70
        self.__brand = "bmw"
        
class ExtendedCar(Car):
    def __init__(self):
        super(ExtendedCar, self).__init__()
        self.color = "green"
        self._speed = 80
        self.__brand = "audi"
        
extended_car = ExtendedCar()
car = Car()
print(dir(car))
print(dir(extended_car))  #  This will print __brand twice, one for _Car__brand and one for _ExtendedCar__brand
```
5) Don't reuse python's saved keywords. If you need to use one of these reserved keywords, add _ in the end of the variable name.
```
 id is a reserved keyword in Python, if you want to use id as a variable name use it like this:
 
 id_
```
6) Use single underscore if you don't want to assign a value to a variable.
```python
for _ in range(100):
    print('a')


_, err = validate_user()
```