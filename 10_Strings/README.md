Python Standards Manifesto
=====================
Strings
=====================

This chapter is about strings.

Strings are immutable in Python. This means that you can't change a string once it's created.

1) In the creation of a string, use single quotes instead of double quotes. This is because single quotes are easier to type, and it's easier to distinguish between single quotes and double quotes.
In the case of a string that contains single quotes, use double quotes.
```python
#  Don't
wrong = 'I \'m in need of a single quote'

#  Do
correct = "I'm in need of a single quote"
```

2) Use f-strings instead of .format. This is because f-strings are easier to read and write. Also, f-strings are faster than both %-formatting and str.format()
This is because at runtime, each expression inside the curly braces gets evaluated within its own scope, and then it's put together into the final string. str.format()
performs a function call. This means that str.format() is slower than f-strings.


3) Don't use backslashes (\) when you need to split a string into multiple lines. Instead, use parentheses. This is because backslashes are hard to read and write.
```python
# Bad
my_very_big_string = """For a long time I used to go to bed early. Sometimes, \
    when I had put out my candle, my eyes would close so quickly that I had not even \
    time to say “I’m going to sleep.”"""

from some.deep.module.inside.a.module import a_nice_function, another_nice_function, \
    yet_another_nice_function
##############################################
# Good
my_very_big_string = (
    "For a long time I used to go to bed early. Sometimes, "
    "when I had put out my candle, my eyes would close so quickly "
    "that I had not even time to say “I’m going to sleep.”"
)

from some.deep.module.inside.a.module import (
    a_nice_function, another_nice_function, yet_another_nice_function)
```

Here is a figure from Real Python that explains the decision-making process of using string formatting methods:
![String Decision Tree](Figures/python-string-formatting-flowchart.png)
