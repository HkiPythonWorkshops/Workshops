# Workshop 4 Material

Start from Workshop 1 if you're completely new to programming and Python!

* Functions & running your program
* More data structures
  * Lists - basic list operations, sort/reverse in-place, list comprehensions
  * Dictionaries
* Data I/O
  * Reading a file
  * Writing to a file
  * Appending to a file

Note: `>>>` shows what the program will look like when typed into the Python command line interpreter. You can also save any of the sample code into a file and run it with `python your_file_name.py`. 

### Functions

Make a new Python file, e.g. called exercises.py
Run this file with the command `python exercises.py`

A function is a re-usable bit of code that's very useful when we want to use the do the same thing many times in the same program. Instead of repeating the code, we make a function that can be called. :bangbang: *should there be an example*

Let's make a function (notice the indentation): 

```python
>>> def print_hello():
...	print "Hello!"
```
Now call the function: 

```python
>>> print_hello()
```

A fuction can be given parameters (or arguments): 

```python
>>> def print_hello_with_name(name):
...	print "Hello " + name + "!"
...
>>> print_hello_with_name("Python")
Hello Python!
```
A fuction can be given any amount of parameters, but usually the fewer the better.

A function can *return* something, which can then e.g. be saved into a variable: 
```python
>>> def addition(num_1, num_2):
...	return num_1 + num_2
...
>>> addition(10, 20)
30
>>> sum = addition(10, 20)
>>> sum
30
```

### Classes and objects

Class can be thought as an template to hold some re-usable functionality. Objects in Python are instances of that *class*. An object has properties and methods attached to it. Here's a sample Dog class (again, notice the indentation):


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
Checking if an item is in the list is most easily done by using *in*: 
```python
>>> my_list = ["a", "b", "c"]
>>> "a" in my_list
True
>>> "d" in my_list
False
```

:bangbang: *python shallow-copy for lists?*
```python
>>> my_list = ['a', 'b', 'c']
>>> new_list = my_list
>>> new_list
['a', 'b', 'c']
>>> new_list.append('d')
>>> new_list
['a', 'b', 'c', 'd']
>>> my_list
['a', 'b', 'c', 'd']
```
Last but not least, Python offers something called *list comprehensions* where you do the same action for all members of a list, and get the a new list with the modified items returned.
```python
>>> my_list = ["a", "b", "c"]
>>> [letter.upper() for letter in my_list]
['A', 'B', 'C']
>>> ascii_codes = [ord(letter) for letter in my_list]
>>> ascii_codes
[97, 98, 99]
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

:bangbang: Iterating items with keys is also easy using the `items()` method provided by the built-in Dictionary-class, which returns a list of the keys and values in the dictionary, as tuples: 
```python3
>>> my_dict = {'a':1, 'b':2, 'c':3}
>>> my_dict.items()
[('a', 1), ('c', 3), ('b', 2)]
>>> for key, value in my_dict.items():
...   print(key, value)
... 
c 3
a 1
b 2
```
You can probably guess what the methods `keys()` and `values()` do. 

Notice that the keys are not returned in any specific order. Dictionaries are *unordered*, meaning that the data in them is not stored in any particular order.

Exercises:

* Count how many of each letter there are in the string "Time And Relative Dimension In Space" using a dictionary to keep count of each letter's appearances. 
 * Hint: Iterate over the string  (strings can be iterated the same way as lists with a `for` loop). For each character, check if it's in your dictionary. If not, add a new item and put the value as 1. If it is, add 1 to the value. 

* Create a dictionary with keys 1-15 with a loop, assign None as the value. Then get the keys, sort them and iterate over them.

Read more about data structures in Python: 
* [Python 2 docs](https://docs.python.org/2/tutorial/datastructures.html)
* [Python 3 docs](https://docs.python.org/3/tutorial/datastructures.html)
 
 ## File I/O

Check that you have the file "sonnet.txt" in the folder you're running these commands from!

### Reading file content

Before doing any file operations like reading, we need to open a file object in a specific mode. To open a file object for reading, use the method `open()` with the flag "r" (read):

```python
>>> my_file = open("sonnet.txt", "r")
>>> my_file
<open file 'sonnet.txt', mode 'r' at 0x105eb06f0>
```
Now that we have an opened file object, we can read all the contents in one go:

```python
>>> whole_file = my_file.read()
>>> my_file.close()
>>> whole_file
"Shall I compare thee to a summer's day?\nThou art more lov"... and so on
```
As you can see, the whole file is just one long string, with the line breaks (\n) in the middle of the string. If you print `whole_file` it looks ok, because the line breaks are printed nicely.

We also *closed* the file after reading it. After finishing with a file, you should always close the file to free up system resources taken up by the open file and to make sure the file won't get corrupted in case something goes wrong with your program. After closing it, you will get an error if you try to read it again.

You can also read all the lines of the file and have them returned as a list. Here is a nicer way of opening a file that will make sure it gets closed when we're done:
```python
>>> with open("sonnet.txt", "r") as my_file:
...	lines = my_file.readlines()
...
>>> lines
["Shall I compare thee to a summer's day?\n", 'Thou art more lov'.... and so on
```
Now we have the lines in a nice list. However, both of these operations are *risky* because the file is read into memory as a whole. So if your file happens to be 5 times bigger than the available memory on the machine, you might freeze or crash Python, or the whole machine in the worst case. Also, `readlines()`reads the whole file, creates strings of all the lines and puts them in a list, processing a large file will take a long time before you can do anything with the contents. So for small files these methods work fine, but if the input file's size is large or unknown, they might be very inefficient or even dangerous. 

A better way to read a file is line by line.
```python
>>> with open("sonnet.txt", "r") as my_file:
...	line = my_file.readline()
...     print(line)
...     line2 = my_file.readline()
...     print(line2)
Shall I compare thee to a summer's day?

Thou art more lovely and more temperate:
```
Using `readline()` is nice because it remembers where you are in the file and will always return the next line. When end of file is reached, an empty string ('') is returned. 

An even easier way to read the whole file line by line is with a for loop: 
```python
>>> with open("sonnet.txt", "r") as my_file:
...	for line in my_file:
...	    print(line)
Shall I compare thee to a summer's day?

Thou art more lovely and more temperate:
... and so on
```
The loop will take care of going over all the lines and stopping when the end of file is reached.

Exercises
* Read the contents of the sonnet file into a list using the for loop. Sort the list in reverse alphabetical order.
* Read the contents of the sonnet file into a dictionary using the line number as key and the line's text as the value.

### Writing to a file

To write to a file, we have two ways: overwriting everything or appending to the end. Let's first cover writing and overwriting. 

Start by opening the file for writing. Be careful: *this will remove any existing file contents!*

```python
>>> with open("newfile.txt", "w") as my_file:
...	my_file.write("This string is awesome")
```
Now we have created a new file and written something in it. Open the file and read its contents to check it's there.
If you do it again, what happens? 
```python
>>> with open("newfile.txt", "w") as my_file:
...	my_file.write("A second awesome string")
```

Exercises:
* Save the contents of sonnet.txt to a list line by line, then write them line by line to a file sonnet2.txt.
* Add line numbers in front of the lines in sonnet.txt. (Remember that opening a file in "w" mode will destroy its contents!)


#### Appending

Often we don't want to destroy the contents of a file, but instead add something to the end. For this purpose, you can open a file in the *append* mode: 
```python
>>> with open("newfile.txt", "a") as my_file:
...	my_file.write("Adding something to the end")
```
If you now inspect the contents, you should have the old contents plus the new string. 

Exercises:
* Create a new file, and write the numbers 1-10 on their own rows. Note that you can only write strings into a file, so you might need to convert the numbers to strings first!
* Append the numbers 11-20 to the end of this file. 

## Project

