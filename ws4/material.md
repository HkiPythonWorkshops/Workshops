# Workshop 4 Material

Start from Workshop 1 if you're completely new to programming and Python!

* Functions & running your program
* More data structures
  * Lists - list comprehensions, sort/reverse, in-place, zip
  * Dictionaries
* Data I/O
  * Reading a file
  * Writing to a file


### Functions

Make a new Python file, e.g. called exercises.py
Run this file with the command `python exercises.py`

A function is a re-usable bit of code that's very useful when we want to use the do the same thing many times in the same program. Instead of repeating the code, we make a function that can be called.

Let's make a function (notice the indentation): 

```python
def print_hello():
	print "Hello!"
```
Now call the function: 

```python
print_hello()
```

A fuction can be given parameters (or arguments): 

```python
def print_hello_with_name(name):
	print "Hello " + name + "!"

>>> print_hello_with_name("Python")
Hello Python!
```
A fuction can be given any amount of parameters, but usually the fewer the better.

A function can *return* something, which can then e.g. be saved into a variable: 
```python
def addition(num_1, num_2):
	return num_1 + num_2

>>> addition(10, 20)
30
>>> sum = addition(10, 20)
>>> sum
30
```

### Classes and objects

Objects in Python are instances of a *class*. An object has properties and methods attached to it. Here's a sample Dog class (again, notice the indentation):


```python

class Dog():
	
	def __init__(self, breed):
		self.breed = breed

	def bark(self):
		print "Woof!"

spotty = Dog("Golden retriever")
print spotty.breed

spotty.bark()
```

Exercises:

* Create methods for subtraction, multiplication and division. Each method should have two parameters and return the result.

* Create a class called Student which is given a name and a student number as parameters.




## Python Data Types

### Strings, integers, floats

Just a reminder of the basic data types: 

```python
>>> my_string = "This is a string"
>>> my_int = 3
>>> my_float = 1.0
```

### Lists

Lists (sometimes called arrays in other languages) are one of the most basic data types. A list is an ordered collection of any items. A list can contain any kind of data, like strings, ints, floats, other lists, objects, etc.

You can access items in a list by their index, starting from 0, and also change the values of items in the list: 

```python
>>> my_list = [1, 2, 3]
>>> my_list[0]
1
>>> my_list[0] = 5
>>> my_list[0]
5
```

You can ask for the list's length, reverse the list and sort it (in-place):
```python
>>> len(my_list)
3
>>> my_list.reverse()
>>> my_list
[3, 2, 1]
>>> my_list.sort()
>>> my_list
[1, 2, 3]
```

Iterating over a list of items is a very common task: 
```python
>>> numbers = [1, 2, 3]
>>> for number in numbers: 
...     print number
... 
1
2
3
```

So is iterating over a list based on the indexes: 
```python
>>> my_list = ["a", "b", "c"]
>>> for i in range (0, len(my_list)): 
...     print my_list[i]
a
b
c
```
Checking if an item is in the list: 
```python
>>> my_list = ["a", "b", "c"]
>>> "a" in my_list
True
>>> "d" in my_list
False
```

Exercises:


### Dictionaries

A dictionary is a collection of pairs of *keys* and *values*, useful for storing many kinds of information. Here's an example of a mini-dictionary and how to look up an item with a key:

```python
>>> my_dictionary = {"red": "punainen", "blue": "sininen", "yellow": "keltainen"}
>>> my_dictionary["red"]
punainen
```

Adding a new item is easy:
```python
>>> my_dictionary["black"] = "musta"
```
Checking if an item is in the dictionary works the same way as with lists: 
```python
>>> "yellow" in my_dictionary
True
>>> "purple" in my_dictionary
False
```



