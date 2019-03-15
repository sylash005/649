# ITEC649 2019 Python Assignment

This assignment involves writing Python code to extract information about product details
from data files and load them into a consistent SQL database. It is an 
example of an Extract-Transform-Load (ETL) task. 

You have been given the task of generating some normalised data on product given some
data files in different formats.   

You are given:

* An HTML file that lists information about products, stock, and prices.
* A CSV spreadsheet containing information about the location of each product.
* A CSV spreadsheet containing detailed information about store locations. This 
spreadsheet relates the ID of the product with the ID of the location.

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

Your file `main.py` needs to generate a CSV file. The CSV file must 
contain the following fields:

* Description
* Price (including the currency symbol)
* Amount in stock
* Store location (all the location information in one string)

In addition, the report must be sorted in **numerical** ascending order by the stock price.

You will also submit the code you have written to solve this problem.  Your code **must** 
use functions and every function **must** include a suitable docstring that describes 
what it does.  Each function should implement a logical part of the overall ETL process.

The template `main.py` includes several functions that you **must** implement and they must 
pass unittests provided. In addition, you need to add the main code that generates the CSV file 
as specified above.
