import unittest
import sqlite3

import database
import main
from io import StringIO

import csv


class BasicTests(unittest.TestCase):

    def setUp(self):
        self.db = sqlite3.connect(":memory:")

    def test_read_relations_1(self):
        database.create_tables(self.db)
        with open("relations.csv") as f:
            main.read_relations(self.db, f)
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM relations")
        result = cursor.fetchall()
        self.assertEqual(20, len(result))
        self.assertSequenceEqual((1, 2), result[1][1:])
        self.assertSequenceEqual((8, 2), result[8][1:])

    def test_read_relations_2(self):
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
        self.assertSequenceEqual((0, 1), result[0][1:])
        self.assertSequenceEqual((1, 0), result[1][1:])
        self.assertSequenceEqual((2, 1), result[2][1:])

    def test_read_locations_1(self):
        database.create_tables(self.db)
        with open("locations.csv") as f:
            main.read_locations(self.db, f)
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM locations")
        result = cursor.fetchall()
        self.assertEqual(len(result), 3)
        self.assertSequenceEqual((0, "12", "George Street", "Sydney", "NSW"), result[0])
        self.assertSequenceEqual((1, "24", "Mary Street", "Brisbane", "QLD"), result[1])
        self.assertSequenceEqual((2, "43", "Queen Street", "Melbourne", "VIC"), result[2])

    def test_read_locations_2(self):
        database.create_tables(self.db)
        my_locations = """id,number,street,city,state
0,2,"Peter Rd",Adelaide,SA
1,31,"Pitt Ave",Perth,WA"""
        main.read_locations(self.db,StringIO(my_locations))
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM locations")
        result = cursor.fetchall()
        self.assertEqual(len(result), 2)
        self.assertSequenceEqual((0, "2", "Peter Rd", "Adelaide", "SA"), result[0])
        self.assertSequenceEqual((1, "31", "Pitt Ave", "Perth", "WA"), result[1])

    def test_read_stock_1(self):
        database.create_tables(self.db)
        with open("index.html") as f:
            main.read_stock(self.db, f)
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        self.assertEqual(len(result), 20)
        self.assertSequenceEqual((2, "Yellow Wool Jumper", 81, 175.31, "$"), result[2])
        self.assertSequenceEqual((6, "Dark Denim Top", 78, 90.31, "$"), result[6])

    def test_read_stock_2(self):
        database.create_tables(self.db)
        with open("index2.html") as f:
            main.read_stock(self.db, f)
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        self.assertEqual(len(result), 6)
        self.assertSequenceEqual((4, "Zipped Jacket", 95, 56.73, "$"), result[4])
        self.assertSequenceEqual((5, "Silk Summer Top", 63, 36.56,'£'), result[5])

    def test_report_1(self):
        database.create_tables(self.db)
        my_relations = """product,location
0,0
1,1
2,0"""
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
        self.assertDictEqual({'description': 'Zipped Jacket',
                             'price': '56.73',
                             'currency': '£',
                             'stock': '95',
                             'location': "3, Macquarie St, Melbourne, VIC"},
                             dict(records[0]))
        self.assertDictEqual({'description': 'Soft Winter Jacket',
                             'price': '111.23',
                             'currency': '$',
                             'stock': '38',
                             'location': "6, John Rd, Bourke, NSW"},
                             dict(records[1]))
        self.assertDictEqual({'description': 'Navy Sports Jacket',
                             'price': '149.05',
                             'currency': '$',
                             'stock': '25',
                             'location': "6, John Rd, Bourke, NSW"},
                             dict(records[2]))

    def test_main_1(self):
        with open("report.csv", "w") as f:
            pass
        main.main()
        with open("report.csv") as f:
            reader = csv.DictReader(f)
            records = [r for r in reader]
        self.assertEqual(20, len(records))
        self.assertDictEqual({'description': 'White Cotton Shirt',
                             'price': '14.63',
                             'currency': '$',
                             'stock': '13',
                             'location': "12, George Street, Sydney, NSW"},
                             dict(records[0]))
        self.assertDictEqual({'description': 'Blue Silk Tuxedo',
                             'price': '26.48',
                             'currency': '$',
                             'stock': '84',
                             'location': "24, Mary Street, Brisbane, QLD"},
                             dict(records[3]))
        self.assertDictEqual({'description': 'Black Leather Bag',
                             'price': '67.2',
                             'currency': '$',
                             'stock': '24',
                             'location': "43, Queen Street, Melbourne, VIC"},
                             dict(records[9]))



if __name__ == '__main__':
    unittest.main()
