import unittest
import sqlite3
import os
import csv

import database
import main


class BasicTests(unittest.TestCase):

    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.db.row_factory = sqlite3.Row
        database.create_tables(self.db)

    def get_user(self, id):
        """Get a user from the database for testing"""
        cur = self.db.cursor()
        cur.execute("select * from users where id=?", [id])
        return cur.fetchone()

    def get_product(self, id):
        """Get a product from the database for testing"""
        cur = self.db.cursor()
        cur.execute("select * from products where id=?", [id])
        return cur.fetchone()

    def get_order(self, user_id, product_id):
        """Get an order from the database for testing"""
        cur = self.db.cursor()
        cur.execute("select * from orders where user_id=? and product_id=?", [user_id, product_id])
        return cur.fetchone()

    def test_add_user(self):
        """We can add a user to the database"""

        main.add_user(self.db, 1, 'Steve', 'Cassidy', 'Steve@here.com', 'Male')

        user = self.get_user(1)
        self.assertIsNotNone(user)
        self.assertEqual(user['first_name'], 'Steve')

    def test_add_product(self):
        """We can add a product to the database"""

        main.add_product(self.db, 1, "description", 123, 45)

        product = self.get_product(1)
        self.assertIsNotNone(product)
        self.assertEqual(product['stock'], 123)

    def test_add_order(self):
        """We can add an order to the database (if the ids are valid)"""

        main.add_user(self.db, 1, 'Steve', 'Cassidy', 'Steve@here.com', 'Male')
        main.add_product(self.db, 98, "description", 123, 45)
        msg = main.add_order(self.db, 98, 1, 3)
        self.assertEqual("Success", msg)

        order = self.get_order(1, 98)
        self.assertIsNotNone(order)
        self.assertEqual(order['quantity'], 3)

        msg = main.add_order(self.db, 98, 2, 3)
        self.assertEqual("Invalid user", msg)

        msg = main.add_order(self.db, 99, 1, 3)
        self.assertEqual("Invalid product", msg)

    def test_read_users(self):
        """We can read the users CSV file"""

        main.read_users(self.db, "users.csv")

        # check for some users
        # 19,Dyanna,Caffery,dcafferyi@smh.com.au,Female
        user = self.get_user(19)
        self.assertIsNotNone(user)
        self.assertEqual(user['first_name'], 'Dyanna')
        self.assertEqual(user['gender'], 'Female')

        # verify number of users
        cur = self.db.cursor()
        cur.execute("select count(id) as count from users")
        result = cur.fetchone()
        self.assertEqual(100, result['count'])

    def test_read_products(self):
        """We can read the products from the HTML file"""

        main.read_products(self.db, "index.html")

        prod = self.get_product(2)
        self.assertIsNotNone(prod)
        self.assertEqual(prod['description'], 'Yellow Wool Jumper')
        self.assertEqual(prod['price'], 175.31)

        # verify number of products
        cur = self.db.cursor()
        cur.execute("select count(id) as count from products")
        result = cur.fetchone()
        self.assertEqual(20, result['count'])

    def test_read_orders(self):
        """"We can read the orders from the CSV file"""

        # need to read products and users first to create valid ids
        main.read_users(self.db, "users.csv")
        main.read_products(self.db, "index.html")
        main.read_orders(self.db, "orders.csv")

        order = self.get_order(22, 18)
        self.assertIsNotNone(order)
        self.assertEqual(order['quantity'], 9)

        # should not have this order, invalid product
        order = self.get_order(47, 33)
        self.assertIsNone(order)

        # verify number of orders
        cur = self.db.cursor()
        cur.execute("select count(quantity) as count from orders")
        result = cur.fetchone()
        self.assertEqual(999, result['count'])

    def test_report(self):
        """We can generate the final report CSV file"""

        outfile = "testoutputfile.csv"

        main.main(self.db, outfile)
        self.assertTrue(os.path.exists(outfile))
        with open(outfile) as fd:
            reader = csv.DictReader(fd)
            report = list(reader)
        os.unlink(outfile)  # remove the output file
        self.assertEqual(999, len(report))

        # check the first row
        row = report[0]
        self.assertEqual(row['first_name'], 'Renard')
        self.assertEqual(row['total'], '377.04')  # change to string


if __name__ == '__main__':
    unittest.main()
