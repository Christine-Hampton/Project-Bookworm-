from tkinter import *
root = Tk()

import tkinter as TK 
from Book import Book
from customer import Customer 
from order import Order

class BookstoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bookstore Inventory Management")

        # Create the GUI elements here
        # for example
        self.label = Tk.Label(root, text="welcome to the Bookstore Inventory Management System")

        # add aditional elements and layout

        def run(self):
            self.root.mainloop()

if __name__ == "__main__":
    root = Tk.TK()
    app = BookstoreApp(root)
    app.run()
