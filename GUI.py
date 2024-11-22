from tkinter import *
from Book import Book
from customer import Customer 
from order import Order

class BookstoreApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Bookstore Inventory Management")

        # Create the GUI elements here
        # for example
        self.label = Label(text="Welcome to the BookWorm Inventory Management System")
        self.label.pack()

        # add additional elements and layout

        # be sure to use grid() so the elements appear!
        # do not use pack()! while simplier, grid() is far more flexible

if __name__ == "__main__":
    app = BookstoreApp()
    app.mainloop()

