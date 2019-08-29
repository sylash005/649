"""
Module to read data from CSV files and HTML file
to populate an SQL database

ITEC649 2019
"""

import csv
import sqlite3
from bs4 import BeautifulSoup
from database import DATABASE_NAME, create_tables


def add_user(db, id, first_name, last_name, email, gender):
    """Add a single user record to the database"""


def add_product(db, id, description, stock, price):
    """Add a single product to the database"""


def add_order(db, product_id, user_id, quantity):
    """Add a single order to the database. Verify that the product and user ids are
    valid before adding.
    Return the string "Success" if the record was added, otherwise return
    "Invalid user" or "Invalid product"
    """


def read_users(db, filename):
    """Read user data from the given filename. Populate the `users` table
    in the database with the data read.
     - db      : a connection to a database.
    - filename: the input CSV format file to read data from
    This function does not return a value. It updates the database with user data.
    """


def read_orders(db, filename):
    """Read the orders from the given CSV file and store them in the database
    - db      : a connection to a database.
    - filename: the input CSV format file to read data from
    This function does not return a value. It updates the database with order data.
    If any errors are encountered in the data, a message is printed.
    """


def read_products(db, filename):
    """Read the products from the given HTML file and store them in the database
    - db      : a connection to a database.
    - filename: the input HTML format file to read data from
    This function does not return any values or print anything on screen. After executing this function,
    the products found in the HTML file will be stored as product records in the database.
    """


def report(db, filename):
    """Generate a database report and store it in filename in CSV format
    - db      : a connection to a database
    - filename: the name of the csv file to write to
    This function does not return any values or print anything on screen, it generates
    a report in CSV format and writes it to the given filename.
    """


def main(db, filename):
    """Execute the main code that calls all functions to generate the resulting
    report in `filename` in CSV format.
    """
    # Write your code below


# Do not edit the code below
if __name__=='__main__':
    db = sqlite3.connect(DATABASE_NAME)
    db.row_factory = sqlite3.Row
    create_tables(db)
    main(db, "report.csv")
