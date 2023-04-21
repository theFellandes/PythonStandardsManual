Python Standards Manifesto
=====================
Tips and Tricks
=====================

This chapter is about some tips and tricks in Python.

Usage of wrappers can save a lot of time and effort. Also, they look clean

* Wrapper example:
```python
from functools import wraps
from time import perf_counter


def get_time(func):
    """Finds total execution time of a function"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = perf_counter()

        return_value = func(*args, **kwargs)

        end_time = perf_counter()
        total_time = round(end_time - start_time, 4)

        print(f"{func.__name__} took Time: {total_time} seconds")

        return return_value

    return wrapper
 
```
* Here, wraps decorator/wrapper is used to get the name of the function that have been wrapped.
