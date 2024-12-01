import sqlite3

class Customer:
    def __init__(self, first_name, last_name, customer_id, email, phone_number):
        self.first_name = first_name 
        self.last_name = last_name 
        self.customer_id = customer_id
        self.email = email
        self.phone_number = phone_number 
     
    def save_to_db(self):
        connection = sqlite3.connect('bookstore.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO customers (name, customer_id, email, phone_number) VALUES (?, ?, ?, ?,)'
                       (self.name, self.customer_id, self.email, self.phone_number,))

    def add_customer(self):
        # add customer to data base 
        pass

    def update_customer(self):
        # update customer details 
        pass 

    def remove_customer(self):
        # remove customer from database 
        pass

