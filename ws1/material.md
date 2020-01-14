# Workshop 1 Material


## Interacting with Python

To check that you have installed Python successfully, type: 

`python --version`

You should see something like:
`Python 3.7.5`

To start interacting with Python in interactive mode, type: 
`python`

You should see something like: 
```
Python 3.6 (#1, Dec 19 2019, 00:02:06)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can now write commands after the >>> and press enter: 
```python
>>> 1+1
2
>>> print(“Hello world!”)
Hello world!
```

To exit this mode, type: 
`>>> exit()`

Another way to interact with Python is to save commands in a separate Python file and tell Python to run it. 
Save the following in a file **hello.py**:
```python
print(“Hello world!”)
```

Then run the program from the same folder from the command line with: 
`python hello.py`

You should see the following as the output:
`Hello world!`

## Basic data types: Numbers

The most common numbers are **int** (integers) and **floats**. Ints are integers whereas floats have a fractional part.

You can use the Python interactive interpreter as a calculator to test how ints and floats behave with basic operations:

```python
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5.0*6) / 4
5.0
>>> 8 / 5.0
1.6
```

**Note**: Some operations behave differently based on whether numbers are **int** or **float**.

```python
>>> 8 / 3
2
>>> 8.0 / 3
2.6666666666666665
```

The order of calculation is the same as in normal math, e.g. parenthesis take precedence over other calculations: 
```python
>>> 2 * 3 + 3
9
>>> 2 * (3 + 3)
12
```

A more exotic operation is the **modulo** or **%**: it returns the remainder of a division.

```python
>>> 10 % 3
1
>>> 15 % 6
3
>>>
```

Exponents can be calculated with __**__:
```python
>>> 2 ** 3
8
>>> 9 ** 0.5
3.0
```

## Basic data types: Strings

A string is a piece of text, or some letters and characters. 
```python
>>> print("Hello world!")
Hello world!
>>> print('John Smith')
John Smith
>>> print("He said 'hello'.")
He said 'hello'.
>>> print('She said "hi".')
She said "hi".
```

As you can see, strings can be surrounded by single **'** or double **"** quotes, and can contain the other type of quote inside it. 

Strings can also contain special characters, most common are **\n** or line break: 
```python
>>> print("One\nTwo\nThree")
One
Two
Three
```

You can use some of the mathematical operators to **concatenate** (add together) strings:
```python
>>> print("awe" + "some")
awesome
>>> print("?" * 4)
????
>>> print("Yipp" + "e" * 5 + "!")
Yippeeeee!
```

Python comes with a lot of inbuilt methods for manipulating strings:

```python
>>> "hello".capitalize()
'Hello'
>>> "hello".upper()
'HELLO'
>>> "HELLO".lower()
'hello'
```
You can also easily get the length of a string: 
```python
>>> len("hello")
5
```

## Converting between strings, ints and floats

You can force conversions between data types, and sometimes you have to do it for your program to behave correctly. 

```python
>>> 5 + 5.05
10.05
>>> float(8/3)
2.0
>>> float(8)/3
2.6666666666666665
>>> int("5")
5
```

You have to convert numbers to strings before you can concatenate them with strings. 
```python
>>> 5 + "I'm a string"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(5)
'5'
>>> str(5) + "I'm a string"
"5I'm a string"
```

## Variables

So far we've just been typing things, but what if we want to save some of the information for later?

A **variable** can be used to store a number, a string, or most other things. The **=** character is used to assign a value to a variable.

```python
>>> name = "John Smith"
>>> print name
John Smith
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
```
Variables point to an item, which can be almost anything, except another variable.

```python
var1 = 1
var2 = var1
var1 = 2
print(var2)
```

What’s the value of *var2*? It's still 1,  since it's actually pointing to number 1 and not to *var1*.


## Booleans and comparisons

A **boolean** can either be **True** or **False**. In Python, making different kinds of comparisons returns a boolean value: 
```python
>>> 5 == 5
True
>>> 5 != 6
True
>>> 3 <= -2
False
>>> 10 > 5
True
```

1. **==** means **is equal to**
2. **!=** means **not equal to**
3. **>** and **<** mean greater or less than
4. **>=** and **<=** mean greater/less than or equal to. 

Note that **==** is for making comparisons and it's different from **=** which is used to assign a value to a variable. 

You can also save a boolean value into a variable: 
```python
>>> a = True
>>> a
True
```

## Conditionals

Often in programs you need to do different things based on the situation. In these cases you can use an **if** clause: 

```python
>>> number = 1
>>> if number > 0:
...     print("Your number is positive!")
...
Your number is positive!
```
Note the indentation. The content of an **if** clause has to be indented. 

You might have to do something else in case the **if** clause returns a False value: 
```python
>>> number = -1
>>> if number > 0:
...     print("Your number is positive!")
...else:
...     print("Your number is negative!")
Your number is negative!
```

Sometimes you have to take into account even more possibilities: 
```python
>>> number = 0
>>> if number > 0:
...     print("Positive!")
... elif number == 0:
...     print("Zero!")
... else:
...     print("Negative!")
...
Zero!
```

These are one type of **flow control** or **branching**, meaning the program can take many different paths depending on the situation. 

## Data types: List

A list in Python is a collection of items and can contain almost anything. 

```python
>>> shopping_list = ["eggs", "milk", "bread"]
>>> print(shopping_list)
['eggs', 'milk', 'bread']
>>> my_variable = 5
>>> my_list = [1, 2.0, "a string", True, my_variable]
>>> len(my_list)
5
```

Items in a list can be accessed based on their **index** or place in the list. The first item has the index 0, the second one 1, etc.

```python
>>> books = ["Fellowship of the Ring", "The Two Towers", "Return of the King"]
>>> books[0]
'Fellowship of the Ring'
>>> books[1]
'The Two Towers'
>>> books[2]
'Return of the King'
```

What happens when you try to access an index that doesn't exist? 
```python
>>> books[3]
```

You can create an empty list and add things to it: 
```python
>>> colors = []
>>> colors.append("blue")
>>> colors.append("red")
>>> colors
['blue', 'red']
```

You can also **join** a list of items by defining what you want to add between the items (in this case a comma and a space): 
```python
>>> animals = ["cats", "dogs", "horses"]
>>> ", ".join(animals)
'cats, dogs, horses'
```

You can easily sort a list (this happens **in-place**, meaning your original list is changed forever):
```python
>>> numbers = [6, 2, 4, 9, 10]
>>> numbers.sort()
>>> numbers
[2, 4, 6, 9, 10]
```

## Loops

Often we need to do things many times. A **for** loop allows us to do something once for each item in a list or range.

```python
>>> books = ["Fellowship of the Ring", "The Two Towers", "Return of the King"]
>>> for book in books:
...     print(book)
...
Fellowship of the Ring
The Two Towers
Return of the King
```

When you need to do something a certain amount of times, you can use range(x, y): 
```python
>>> for i in range(1, 5):
...     print(i)
...
1
2
3
4
```

A **while** loop, on the other hand, allows us to repeat an action until the condition we give returns a **False**.
```python
>>> i = 1
>>> while i < 5:
...     print(i)
...     i = i + 1
...
1
2
3
4
```

It's important to have a condition that will eventually return **False**! Otherwise your program will get stuck. Don't try this (or if you do, click ctrl+c to stop the loop): 
```python
>>> while 10 > 5:
...     print("This is an infinite loop!")
...
This is an infinite loop!
This is an infinite loop!
This is an infinite loop!
...```

