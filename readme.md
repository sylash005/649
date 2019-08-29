# ITEC649 2019 S2 Python Assignment

This assignment involves writing Python code to extract information about product details
from data files and load them into a consistent SQL database. It is an 
example of an Extract-Transform-Load (ETL) task. 

You have been given the task of generating some normalised data on product given some
data files in different formats.   

You are given:

* An HTML file that lists information about products, stock, and prices.
* A CSV spreadsheet containing information about users.
* A CSV spreadsheet containing detailed information about orders. This spreadsheet contains columns for
the product id number and the user id number along with the order quantity.

The fake CSV data was generated using [Mockaroo](https://mockaroo.com/).

Your task is to read the data from all of these files, add it into an SQL database, 
and operate on the database to produce a report.

The schema for the SQL database is provided for you in the file database.py. You can
run this file to create the database.  Your code will then add data to it. Note that  
the HTML file lists the product ID as part of the HTML `href` attribute. This is the 
ID that needs to be used to populate the `products` table in the database.

## Useful Python Modules

Python has many useful modules for this task. You will want to look at:
* the __csv__ module for reading and writing CSV files.
* the __bs4__ module (BeautifulSoup) for reading HTML files.

And of course you will use the __sqlite3__ module for handling the database.

## Required Output

Your file `main.py` needs to generate a CSV file containing a report on the 
orders. The CSV file must contain the following fields:

* `id`: User ID
* `first_name`: User first name
* `last_name`: User last name
* `product`: Product ID number
* `description`: Product description
* `quantity`: the order quantity
* `price`: the order unit price
* `total`: the total for the order (`quantity` * `price`)

In addition, the report must be sorted in alphabetical order of user last name.  

You will also submit the code you have written to solve this problem. 

The template `main.py` includes several functions that you **must** implement as part of your
solution.  Each is described in the doc string. The script calls the function `main` which 
should do all of the work of reading the data files and generating the report. 

The file `test_main.py` contains a set of unit tests for all the functions in `main.py`. Your 
code should pass all of these tests. Note that I will change the data files used for final
marking so your code should not assume that any part of the data is the same as in these
files.  

# Grading

This assignment is worth 15% of the final marks for ITEC649. The marks will be assigned as follows:

- Passing all automated tests: 12%
- Manual assessment of the code quality: 2%
- Manual assessment of documentation: 1%

Code quality means well laid out code, good use of variable names, functions and use of appropriate 
control flow and data structures.

Documentation means that all functions that you write have suitable docstrings (e.g. keep the docstrings 
provided in main.py) and where appropriate you use comments in your code to explain yourself.