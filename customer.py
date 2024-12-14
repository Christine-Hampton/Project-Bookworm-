import sqlite3

class Customer:
    def __init__(self, name, email, phone_number):
        self.name = name
        self.email = email
        self.phone_number = phone_number 
     
    def save_to_db(self):
        connection = sqlite3.connect('bookstore.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO customers (name, email, phone_number) VALUES (?, ?, ?)',
                       (self.name, self.email, self.phone_number))
        connection.commit()
        connection.close()

    def add_customer(self):
        # add customer to data base 
        pass

    def update_customer(self):
        # update customer details 
        pass 

    def remove_customer(self):
        # remove customer from database 
        pass

