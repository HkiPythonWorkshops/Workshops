# Workshop 1 Material


## Interacting with Python

To check that you have installed Python successfully, type: 

`python --version`

You should see something like:
`Python 2.7.9`

To start interacting with Python in interactive mode, type: 
`python`

You should see something like: 
```
Python 2.7 (#1, Feb 28 2010, 00:02:06)
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

You can now write commands after the >>> and press enter: 
```python
>>> 1+1
2
>>> print “Hello world!”
Hello world!
```

To exit this mode, type: 
`>>> exit()`

Another way to interact with Python is to save commands in a separate Python file and tell Python to run it. 
Save the following in a file **hello.py**:
```python
print “Hello world!”
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
>>> print "Hello world!"
Hello world!
>>> print 'John Smith'
John Smith
>>> print "He said 'hello'."
He said 'hello'.
>>> print 'She said "hi".'
She said "hi".
```

As you can see, strings can be surrounded by single **'** or double **"** quotes, and can contain the other type of quote inside it. 

Strings can also contain special characters, most common are **\n** or line break: 
```python
>>> print "One\nTwo\nThree"
One
Two
Three
```

You can use some of the mathematical operators to **concatenate** (add together) strings:
```python
>>> print "awe" + "some"
awesome
>>> print "?" * 4
????
>>> print "Yipp" + "e" * 5 + "!"
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
print var2
```

What’s the value of *var2*? It's still 1,  since it's actually pointing to number 1 and not to *var1*.


