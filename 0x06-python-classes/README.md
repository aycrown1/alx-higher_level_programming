## 0x06. Python - Classes and Objects

**Object-Oriented Programming (OOP)** is a programming paradigm that uses objects and classes to structure and organize code. It revolves around the concept of "objects" representing real-world entities and "classes" defining their blueprints.


*First-Class Everything:* This phrase refers to the idea that in some programming languages, like Python, everything is treated as an object. This means you can assign functions to variables, pass them as arguments, and return them from other functions.

*Class:* A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that the objects created from it will have.

*Object and Instance:* An object is a specific instance of a class. When you create an object from a class, you're instantiating that class to create a unique entity with its own data and behavior.

*Difference between Class and Object/Instance:* A class is like a blueprint, while an object or instance is a concrete instantiation of that blueprint. The class defines the structure, and objects/instances are created based on that structure.

*Attribute:* An attribute is a variable that holds data within a class or an object. Attributes define the characteristics or properties of an object.

*Public, Protected, and Private Attributes:* In Python, you can control the visibility and access to attributes using naming conventions. Public attributes are accessible from anywhere, protected attributes have a single underscore prefix (e.g., `_my_var`), and private attributes have a double underscore prefix (e.g., `__my_var`). It's a convention; Python doesn't enforce strict access control.

*Self:* `self` is a reference to the current instance of a class in Python. It's typically the first parameter of methods within a class and is used to access and modify the object's attributes.

*Method:* A method is a function defined within a class. Methods define the behavior or actions that objects of the class can perform.

*Special `__init__` Method:* It is the constructor method in Python classes. It's automatically called when an object is created from a class and is used to initialize the object's attributes.

*Data Abstraction, Data Encapsulation, and Information Hiding:* These are OOP concepts. Data abstraction refers to hiding the complex implementation details and showing only the necessary features of an object. Data encapsulation involves bundling the data (attributes) and methods (functions) that operate on it into a single unit (a class). Information hiding is the practice of restricting access to certain details of an object, often by making attributes private.

*Property:* A property is a special kind of attribute that is accessed like an attribute but has methods associated with it, typically to get, set, or delete its value.

*The Difference between Attribute and Property in Python:* Attributes are straightforward data members of a class, while properties have getter, setter, and deleter methods associated with them, allowing you to control access and modification of the attribute

* The Pythonic Way to Write Getters and Setters:* Use the `@property`, `@attribute_name.setter`, and `@attribute_name.deleter` decorators to define getters, setters, and deleters for properties. This helps maintain a clean and intuitive interface for attribute access.

*Dynamically Create Arbitrary New Attributes:* Attribute can dynamically create for an instance by simply assigning a value to a new attribute name like `instance.new_attribute = value`.

*Bind Attributes to Objects and Classes:* Attributes can be bind to an object instance by using the dot notation (`object.attribute_name`) or to a class by defining them within the class but outside of any method.

*`__dict__` of a Class/Instance:* The `__dict__` attribute of a class or instance is a dictionary that contains the attributes and their values for that class or instance.

 *How Python Finds Attributes:* Python looks for attributes first in the instance's namespace, then in the class's namespace, and finally in the namespaces of the base classes (in case of inheritance).

*Using `getattr` Function:* `getattr(object, 'attribute_name')` is a built-in Python function used to dynamically access attributes of an object. It allows you to retrieve the value of an attribute if it exists, with an optional default value if it doesn't.
