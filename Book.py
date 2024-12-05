import sqlite3

class Book: 
    def __init__(self, title, author, genre, isbn, price, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.price = price
        self.quantity = quantity
   
    def save_to_db(self):
        connection = sqlite3.connect('bookstore.db')
        cursor = connection.cursor()
        cursor.execute('INSERT INTO books (title, author, isbn, price, quantity) VALUES (?, ?, ?, ?, ?)',
                        (self.title, self.author, self.isbn, self.price, self.quantity))
        connection.commit()
        connection.close()
   

    def add_book(self):
        #add book to inventory
        pass

    def update_book(self):
        # update book details
        pass

    def remove_book(self):
        # remove book from inventory
        pass
