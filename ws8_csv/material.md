# Workshop 8 Material: CSV files

## CSV files: the basics

CSV stands for "comma-separated values". It is a pretty basic data format but it is easy to parse in most programming languages, and even Excel knows how to handle it.

Basic CSV files look something like this:

```csv
name,occupation,age,country
Alexis,coder,28,Marocco
Pascal,artist,35,Indonesia
Jo,economist,24,France
```

The first row has the header: what is data in each column?
The rest of the rows are the actual data, separated by commas. 

So e.g.: `Alexis,coder,28,Marocco`
describes one person, with the following information:

name: Alexis
occupation: coder
age: 28
country: Marocco

#### Separator character

As the name of the data format implies, most often the character used to separate the values on a row is a comma. However, most other characters can be used, and other often-used characters and semicolon (;) and tab.



## Reading CSV files with Python

Python comes ready with tools for reading and writing CSV files. We first need to import the csv library using ìmport, then open the file you want to read, and finally create a csv reader to read the CSV file's contents.



```python
import csv

with open('data1.csv', newline='') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',', )
    for row in datareader:
        print(row)
```