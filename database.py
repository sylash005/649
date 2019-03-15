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
  price money,
  currency varchar
);

DROP TABLE IF EXISTS relations;
CREATE TABLE relations (
  id integer unique primary key autoincrement,
  product integer,
  location integer,
  FOREIGN KEY(product) REFERENCES products(id),
  FOREIGN KEY(location) REFERENCES locations(id)
);

DROP TABLE IF EXISTS locations;
CREATE TABLE locations (
  id integer unique primary key,
  number text,
  street text,
  city text,
  state text
);
"""
    db.executescript(sql)
    db.commit()


if __name__=='__main__':
    import sqlite3
    # if we call this script directly, create the database and make sample data
    db = sqlite3.connect(DATABASE_NAME)
    create_tables(db)
