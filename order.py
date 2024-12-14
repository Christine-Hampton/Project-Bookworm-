import sqlite3

class Order:
    def __init__(self, customer_id, book_id, order_date):
        self.customer_id = customer_id
        self.book_id = book_id
        self.order_date = order_date 

    def save_to_db(self):
        connection = sqlite3.connect('bookstore.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO orders (customer_id, book_id, order_date) VALUES (?, ?, ?)',
                       (self.customer_id, self.book_id, self.order_date))
        connection.commit()
        connection.close()

    def add_order(self):
        # add order to database
        pass
    
    def update_order(self):
        # update order details
        pass

    def remove_order(self):
        # remover order from database
        pass
