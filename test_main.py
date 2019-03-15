import unittest
import sqlite3

import database
import main


class BasicTests(unittest.TestCase):

    def setUp(self):
        self.db = sqlite3.connect(":memory:")

    def test_read_relations(self):
        database.create_tables(self.db)
        main.read_relations(self.db, "relations.csv")
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM relations")
        result = cursor.fetchall()
        self.assertEqual(len(result), 20)
        self.assertEqual(result[1][1], 1)
        self.assertEqual(result[8][2], 2)

    def test_read_locations(self):
        database.create_tables(self.db)
        main.read_locations(self.db, "locations.csv")
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM locations")
        result = cursor.fetchall()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0][1], "12")
        self.assertEqual(result[1][2], "Mary Street")
        self.assertEqual(result[1][3], "Brisbane")
        self.assertEqual(result[2][4], "VIC")

    def test_read_stock(self):
        database.create_tables(self.db)
        main.read_stock(self.db, "index.html")
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM products")
        result = cursor.fetchall()
        self.assertEqual(len(result), 20)
        self.assertEqual(result[2][0], 2)
        self.assertEqual(result[3][1], "Floral White Top")
        self.assertEqual(result[4][2], 86)
        self.assertEqual(result[5][3], 94.26)
        self.assertEqual(result[6][4], '$')

if __name__ == '__main__':
    unittest.main()
