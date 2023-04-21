Python Standards Manifesto
=====================
Type Hinting
=====================

This chapter is about docstrings and commenting in Python.

* Type hinting allows developers to understand and maintain a function better.

```python
def add(a: int, b: int) -> int:
    """ Adds two numbers together """
    return a + b
```
* * In this example, if we are returning string by accident, Pycharm will warn us to correct the wrong data type. Also, it is clear that add takes 2 integers and returns integer in the end.


* In this example, if we are returning string by accident. Try this code at Pycharm.
```python
def add(a: int, b: int) -> int:
    """ Adds two numbers together """
    return str(a + b)
```