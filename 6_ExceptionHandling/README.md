Python Standards Manifesto
=====================
Exception Handling
=====================

This chapter is about exception handling.
## Catch More Specific Exceptions first.


In exception handling, there are 2 approaches: EAFP (Easier to Ask for Forgiveness than Permission) and LBYL (Look Before You Leap).
In the Chapter 6 of "Python in a Nutshell", Alex Martelli states that:

```
A common idiom in other languages, sometimes known as "look before you leap" (LBYL), is to check in advance, before attempting an operation, for all circumstances that might make the operation invalid. This approach is not ideal for several reasons:

1. The checks may diminish the readability and clarity of the common, mainstream cases where everything is okay.
2. The work needed for checking may duplicate a substantial part of the work done in the operation itself.
3. The programmer might easily err by omitting some needed check.
4. The situation might change between the moment the checks are performed and the moment the operation is attempted
```

An example of LBYL:
```python
def do_something(filename):
  if not can_open_file(filename):
    return err(...)
  f = open(filename)
    ...
```
Suppose that can_open_file indicates whether the subsequent open call will succeed. Checking this with previous points:
1) Returning error codes will make crowded.
2) can_open_file definitely duplicates some checking done in open.
3) How can you be sure you've covered every case in can_open_file?
4) Suppose you work in a multiprocessing environment. Between your test with can_open_file and the actual call to open, some other process might have modified the file's properties, opened it, or deleted it. This is a hard-to-debug race condition.

An example of EAFP:
```python
def do_something(filename):
  try:
    f = open(filename)
  except IOError, e:
    raise MyApplicationsExceptionType(e.msg)
````
This approach doesn't suffer previous problems and provides greater flexibility. In Huawei, our exception handling is based on EAFP.

### Never use exceptions for flow-control.
Exceptions exist for exceptional situations: events that are not a part of normal execution.

### Handle exceptions at the level that knows how to handle them.
Always ask "is this the right place to handle this exception?" and be careful with catching all exceptions.

### Do not expose implementation details with exceptions.


#### Do not raise an exception with a string name.
```python
raise "SomeNameOfAnExceptionName"
```

### In most cases, don't catch too broad Exception, catch chunks of Exception, definitely don't catch BaseException.
Catching BaseException will mute out KeyboardInterrupt as well.

Error handling rules:
```
1) Explicit is better than implicit. Write more except, than a broad Exception.
2) Flat is better than nested. Don't use else in the try-except block unless it is necessary.
3) Keep your try/except blocks narrow, because handling too many exceptions is a red flag.
4) Utilize with statement to limit the usage of finally block.
5) Place only minimal code that you want to protect from potential exceptions in the try clause.
```

Usage example code block for try-except-finally:
```python
# Safely open the file
file = open("hello.txt", "w")

try:
    file.write("Hello, World!")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")
finally:
    # Make sure to close the file after using it
    file.close()
```
This can be shortened into:
```python
with open("hello.txt", mode="w") as file:
    file.write("Hello, World!")
```

