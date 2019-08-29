"""Database creation for ITEC649 Python application"""

DATABASE_NAME = "itec649.db"


def create_tables(db):
    """Create and initialise the database tables
    This will have the effect of overwriting any existing
    data."""

    sql = """
DROP TABLE IF EXISTS products;
CREATE TABLE products (
  id integer unique primary key,
  description text,
  stock integer,
  price money
);

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id integer unique primary key,
  first_name text,
  last_name text,
  email text,
  gender text
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
    product_id integer,
    user_id integer,
    quantity integer,
    FOREIGN KEY(product_id) REFERENCES products(id),
    FOREIGN KEY(user_id) REFERENCES users(id)
);
"""
    db.executescript(sql)
    db.commit()


if __name__=='__main__':
    import sqlite3
    # if we call this script directly, create the database and make sample data
    db = sqlite3.connect(DATABASE_NAME)
    create_tables(db)
