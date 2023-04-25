Python Standards Manifesto
=====================
Docstrings and Commenting
=====================

This chapter is about docstrings and commenting in Python.

Docstrings should be frequently used in a class and at the start of 
the function since this allows a documentation to developer. 
This topic is controversial by nature since there are lots of opinion surrounding this topic. 

I think a short summary of a function in a docstring should be used regardless of how expressive the function may be. 

### Docstrings should be enclosed with """ """ ###

There are multiple ways to make a docstring in Python, there is no standard way to do it.

* Method 1: Short sentence in the docstring. The first sentence should be the summary of the function. If a developer wants to add additional information to docstring, then it should be added in the newline.
```python
from functools import wraps
from time import perf_counter


def get_time(func):
    """ Finds total execution time of a function """

    @wraps(func)
    def wrapper(*args, **kwargs):
        """ 
        Wraps the function and returns the total execution time 
        
        Takes function as an input with all of its parameters and
        returns the total execution time of a function
        """
        start_time = perf_counter()

        return_value = func(*args, **kwargs)

        end_time = perf_counter()
        total_time = round(end_time - start_time, 4)

        print(f"{func.__name__} took Time: {total_time} seconds")

        return return_value

    return wrapper

```
* * Advantage: It is short and easy to read.
* * Drawback: The docstring gives a summarized version of the function, it doesn't explain the arguments and the return value's data type.
* Method 2: Epydoc / Epytext format
```python
"""
This is a javadoc style.

@param param1: this is a first param
@param param2: this is a second param
@return: this is a description of what is returned
@raise keyError: raises an exception
"""
```
* * Advantage: It is more detailed than the first method.
* * Drawback: It is longer than the first method.
* Method 3: Google format
```python
"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""
```
* * Advantage: It is more detailed than the first method.
* * Drawback: It is longer than the first method.

I prefer the Google format since it is more pythonic compared to other Epydoc and more expressive than short sentence method.

### Inline comments should be used rarely since they cloud the source code ###

If you need to use inline comments, PEP 8 recommends the followings:
1) Each line of a block comment starts with a # and a single space (unless it is indented text inside the comment).
```python
# This is a block comment
print('Something')
```
2) Inline comments should be separated by at least two spaces from the statement. They should start with a # and a single space.
```python
print('Something')  # This prints something
```
