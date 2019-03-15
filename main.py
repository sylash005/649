"""
Module to read data from CSV files and HTML file
to populate an SQL database

ITEC649 2019
"""

import csv
import sqlite3
from bs4 import BeautifulSoup
from database import DATABASE_NAME, create_tables


def read_relations(db, filename):
    """Read the relations.csv file and store records in the database"""
    pass


def read_locations(db, filename):
    """Read locations.csv and store records in the database"""
    pass


def read_stock(db, filename):
    """Read stock information from the HTML file and store in the database"""
    pass


def report(db, outfile):
    """Run the required report over the database"""
    pass


if __name__=='__main__':
    db = sqlite3.connect(DATABASE_NAME)
    create_tables(db)
    # Add your 'main' code here to call your functions
