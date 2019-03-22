import unittest
import sqlite3

import database
import main
from io import StringIO

import csv


class BasicTests(unittest.TestCase):

    def setUp(self):
        self.db = sqlite3.connect(":memory:")

    def test_read_relations(self):
        database.create_tables(self.db)
        with open("relations.csv") as f:
            main.read_relations(self.db, f)
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM relations")
        result = cursor.fetchall()
        self.assertEqual(20, len(result))
        self.assertEqual(1, result[1][1])
        self.assertEqual(2, result[8][2])

        database.create_tables(self.db)
        my_relations = """product,location
0,1
1,0
2,1"""
        main.read_relations(self.db, StringIO(my_relations))
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM relations")
        result = cursor.fetchall()
        self.assertEqual(3, len(result))
        self.assertEqual(1, result[0][2])
        self.assertEqual(2, result[2][1])

    def test_read_locations(self):
        database.create_tables(self.db)
        with open("locations.csv") as f:
            main.read_locations(self.db, f)
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM locations")
        result = cursor.fetchall()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][1], "12")
        self.assertEqual(result[1][2], "Mary Street")
        self.assertEqual(result[1][3], "Brisbane")
        self.assertEqual(result[2][4], "VIC")

        database.create_tables(self.db)
        my_locations = """id,number,street,city,state
0,2,"Peter Rd",Adelaide,SA
1,31,"Pitt Ave",Perth,WA"""
        main.read_locations(self.db,StringIO(my_locations))
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM locations")
        result = cursor.fetchall()
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0][1], "2")
        self.assertEqual(result[1][2], "Pitt Ave")
        self.assertEqual(result[1][3], "Perth")
        self.assertEqual(result[0][4], "SA")


    def test_read_stock(self):
        database.create_tables(self.db)
        with open("index.html") as f:
            main.read_stock(self.db, f)
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        self.assertEqual(len(result), 20)
        self.assertEqual(result[2][0], 2)
        self.assertEqual(result[3][1], "Floral White Top")
        self.assertEqual(result[4][2], 86)
        self.assertEqual(result[5][3], 94.26)
        self.assertEqual(result[6][4], '$')

        database.create_tables(self.db)
        with open("index2.html") as f:
            main.read_stock(self.db, f)
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        self.assertEqual(len(result), 6)
        self.assertEqual(result[4][0], 4)
        self.assertEqual(result[3][1], "Black Leather Bag")
        self.assertEqual(result[4][2], 95)
        self.assertEqual(result[5][3], 36.56)
        self.assertEqual(result[5][4], '£')

    def test_report(self):
        database.create_tables(self.db)
        my_relations = """product,location
0,0
1,1
2,0
3,1"""
        my_locations = """id,number,street,city,state
0,6,"John Rd",Bourke,NSW
1,3,"Macquarie St",Melbourne,VIC"""
        main.read_relations(self.db, StringIO(my_relations))
        main.read_locations(self.db, StringIO(my_locations))
        with open("index3.html") as f:
            main.read_stock(self.db, f)
        with StringIO() as f:
            main.report(self.db, f)
            output = f.getvalue()

        #print(output)
        reader = csv.DictReader(StringIO(output))
        records = [r for r in reader]
        self.assertEqual(3, len(records))
        self.assertEqual('Soft Winter Jacket', records[1]['description'])
        self.assertEqual("6, John Rd, Bourke, NSW", records[2]['location'])
        self.assertEqual('111.23', records[1]['price'])
        self.assertEqual('25', records[2]['stock'])
        self.assertEqual('$', records[1]['currency'])
        self.assertEqual('£', records[0]['currency'])
        # Expected output:
        # description,price,currency,stock,location
        #Zipped Jacket,56.73,£,95,"3, Macquarie St, Melbourne, VIC"
        #Soft Winter Jacket,111.23,$,38,"6, John Rd, Bourke, NSW"
        #Navy Sports Jacket,149.05,$,25,"6, John Rd, Bourke, NSW"



if __name__ == '__main__':
    unittest.main()
