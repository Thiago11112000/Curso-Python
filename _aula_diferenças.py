# Integers
x = 5
print(type(x))  # prints: <class 'int'>

# Floats
y = 3.14
print(type(y))  # prints: <class 'float'>

# Strings
hello = "Hello, World!"
print(type(hello))  # prints: <class 'str'>

# Booleans
is_true = True
print(type(is_true))  # prints: <class 'bool'>

# Lists
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # prints: <class 'list'>

# Tuples
numbers = (1, 2, 3, 4, 5)
print(type(numbers))  # prints: <class 'tuple'>

# Dictionaries
person = {"name": "John", "age": 30, "city": "New York"}
print(type(person))  # prints: <class 'dict'>

# Accessing elements
print(fruits[0])  # prints: apple
print(numbers[2])  # prints: 3
print(person["name"])  # prints: John

# Modifying elements
fruits[0] = "orange"
print(fruits)  # prints: ['orange', 'banana', 'cherry']

# Trying to modify a tuple (this will raise an error)
# numbers[0] = 10  # TypeError: 'tuple' object does not support item assignment

# Adding a new key-value pair to a dictionary
person["country"] = "USA"
print(person)  # prints: {'name': 'John', 'age': 30, 'city': 'New York', 'country': 'USA'}