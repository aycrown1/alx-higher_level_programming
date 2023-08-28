## 0x05. Python - Exceptions

PYTHON EXCEPTION

**Errors vs. Exceptions:**
In programming, both errors and exceptions represent situations where the normal flow of a program is disrupted. However, there's a distinction between the two:

1. **Errors:** These are problems that prevent the program from running correctly and might be caused by external factors like hardware issues, invalid inputs, or improper setup. Examples include syntax errors and logical errors.

2. **Exceptions:** These are events that occur during the execution of a program and disrupt the normal flow, but they can be managed and handled by the program. Exceptions are typically caused by factors such as invalid data or unforeseen conditions.

**Exceptions and How to Use Them:**
An exception is a way to handle unexpected situations in your code. In many programming languages, including Python, exceptions are objects that represent errors or exceptional situations. When an exceptional situation occurs, an exception object is created and propagated up the call stack until it's caught and handled by appropriate code.

**When to Use Exceptions:**
Exceptions should be used when you encounter situations that are unexpected but can be managed gracefully without crashing the entire program. They are particularly useful when dealing with input validation, file operations, network connections, and other situations where external factors could lead to unexpected issues.

**How to Correctly Handle an Exception:**
Exception handling involves three main parts:

1. **Try:** This block encloses the code that might raise an exception.

2. **Except:** Here, you define how to handle the exception. You can specify the type of exception you're catching or use a more general `except` block to catch any exception.

3. **Finally (optional):** This block contains code that should be executed regardless of whether an exception was raised or not. It's often used for cleanup tasks.

```python
try:
    # code that might raise an exception
except SomeExceptionType:
    # handle the exception
finally:
    # optional cleanup code
```

**Purpose of Catching Exceptions:**
Catching exceptions allows your program to gracefully handle errors and continue execution, rather than abruptly crashing. It enables you to provide feedback to users, log errors for debugging, and implement recovery mechanisms.

**Raising a Built-in Exception:**
In Python, you can raise exceptions using the `raise` statement. You can raise built-in exceptions or create custom ones. For example:
```python
if some_condition:
    raise ValueError("This is a custom error message")
```

**Implementing Cleanup After an Exception:**
In situations where resources need to be released or cleanup actions need to be taken after an exception, you can use the `finally` block. For example, closing a file or releasing a network connection should be done in the `finally` block to ensure proper cleanup even if an exception occurs.

```python
file = None
try:
    file = open("example.txt", "r")
    # perform operations on the file
except IOError:
    print("An error occurred while working with the file")
finally:
    if file:
        file.close()  # Close the file regardless of exceptions
```
