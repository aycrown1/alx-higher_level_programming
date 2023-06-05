## 0x00-python-hello_world

Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python’s elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.

The Python interpreter and the extensive standard library are freely available in source or binary form for all major platforms from the Python Web site, https://www.python.org/, and may be freely distributed. The same site also contains distributions of and pointers to many free third party Python modules, programs and tools, and additional documentation.

The Python interpreter is easily extended with new functions and data types implemented in C or C++ (or other languages callable from C). Python is also suitable as an extension language for customizable applications.


### Python Interactive Shells

Python interactive mode, also known as the Python REPL (Read-Eval-Print Loop), allows you to interactively run Python code and get immediate feedback. It is a convenient way to experiment, test code snippets, and quickly try out Python language features without the need to write a complete script.

To start the Python interactive mode, follow these steps:

1. Open a terminal or command prompt on your computer.
2. Type `python` or `python3` (depending on your Python installation) and press Enter. This launches the Python interpreter in interactive mode.
3. You will see the Python prompt, typically represented by `>>>`, indicating that you can start entering Python code.

For example, let's try some simple Python commands in the interactive mode:

```python
>>> print("Hello, World!")
Hello, World!

>>> x = 5
>>> y = 3
>>> x + y
8

>>> import math
>>> math.sqrt(25)
5.0
```

In the interactive mode, you can type Python statements or expressions, and they will be executed immediately. The output of expressions will be displayed directly after you press Enter.

The interactive mode is useful for quickly testing code snippets, debugging, or exploring Python libraries. It provides a convenient way to experiment with Python code and get immediate results, making it an excellent tool for learning and development. To exit the interactive mode, you can type `exit()` or press Ctrl + Z (Windows) or Ctrl + D (Unix-like systems).


### Python Script Mode
Python script mode allows you to write and execute Python code in a script file rather than interacting with the interpreter interactively. In this mode, you write your Python code in a file with a `.py` extension and execute the script using the Python interpreter.

To use Python script mode, follow these steps:

1. Open a text editor or an integrated development environment (IDE) and create a new file.
2. Write your Python code in the file, saving it with a `.py` extension. For example, let's create a file called `my_script.py` with the following code:

```python
print("Hello, World!")
x = 5
y = 3
print(x + y)
```

3. Save the file.

To execute the Python script, you have a few options:

##### Shell
Run the Script from the Terminal or Command Prompt
- Open a terminal or command prompt.
- Navigate to the directory where your script is located using the `cd` command.
- Type `python` or `python3` (depending on your Python installation) followed by the script's filename, and press Enter. For example:

```bash
python my_script.py
```
##### Integrated Development Environment (IDE)

Open your preferred Python IDE (e.g., PyCharm, Visual Studio Code, IDLE).
Open the script file in the IDE.
Look for the run or execute button/icon, typically represented by a play button or something similar. Click it to run the script.
The script will be executed, and the output (if any) will be displayed in the terminal or the output window of your IDE.
