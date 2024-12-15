import sqlite3

def create_tables():
    connection = sqlite3.connect('bookstore.db')
    cursor = connection.cursor()

    # Create books table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        book_id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        isbn TEXT,
        price REAL,
        quantity INTEGER
    )
''')
    
    # Create cusomters table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers(
        customer_id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        phone_number TEXT
    )
''')
    
    # Create orders table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        order_id INTEGER PRIMARY KEY,
        book_id INTEGER,
        customer_id INTEGER,
        order_date TEXT,
        FOREIGN KEY (book_id) REFERENCES books (book_id),
        FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
    )
''')
    
    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_tables()
