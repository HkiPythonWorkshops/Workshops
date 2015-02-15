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

Exponents can be calculated with ******:
```python
>>> 2 ** 3
8
>>> 9 ** 0.5
3.0
```


