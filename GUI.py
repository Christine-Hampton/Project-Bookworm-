from tkinter import *
from Book import Book
from customer import Customer 
from order import Order
import sqlite3 

class BookstoreApp(Tk):
    def __init__(self, *args, **kwargs):
        global system
        global data
        import time
        
        Tk.__init__(self, *args, **kwargs)
        self.title("BookWorm Inventory Manager")
        HeaderFont = ("Arial", 30)
        HotbarFont = ("Arial", 15)
        BtnFont = ("Times New Roman", 20, "bold")

        date_format = "%A, %B %d, %Y"
        time_format = "%I:%M:%S%p"
        t = time.localtime()

        def update_time():
            time_format = time.strftime("%I:%M:%S%p")
            clock.config(text=time_format)
            clock.after(1000, update_time)
        
        self.conn = sqlite3.connect('bookstore.db')
        self.cursor = self.conn.cursor()

        # Create the GUI elements here
        # for example
        # self.label = Label(text="Welcome to the BookWorm Inventory Management System")
        # self.label.pack()

        # add additional elements and layout

        # be sure to use grid() so the elements appear!
        # do not use pack()! while simplier, grid() is far more flexible


        header = Frame(self, bg = 'blue')
        logo = Label(header, text = "BookWorm Inventory Manager", font = HeaderFont, bg = "blue", fg = "white")

        greet = Label(header, text = " Welcome to the BookWorm Inventory Manager       ", font = HotbarFont, bg = 'cyan')
        date = Label(header, text = time.strftime(date_format, t) + "       ", font = HotbarFont, bg = 'cyan')
        clock = Label(header, text = time.strftime(time_format, t) + " ", font = HotbarFont, bg = 'cyan')

        menu = Frame(self)
        menuLabel = Label(menu, text = "Menu", font = HotbarFont, bg = 'gray')
        addBookBtn = Button(menu, text="Book", font=BtnFont,
                            command=self.show_add_book_form)
        addCustomerBtn = Button(menu, text="Customer", font=BtnFont,
                                command=self.show_add_customer_form)
        addOrderBtn= Button (menu, text="Order", font=BtnFont,
                             command=self.show_add_order_form)
        quitBtn = Button(menu, text="Quit", font=BtnFont,
                         command=self.quit)
        

        header.grid(row = 0, column = 0, columnspan = 10)
        logo.grid(row = 0, column = 0, columnspan = 10, sticky = 'w', padx = 5, pady = 5)
        
        greet.grid(row = 1, column = 0, sticky = 'ew')
        date.grid(row = 1, column = 1, sticky = 'ew')
        clock.grid(row = 1, column = 2, sticky = 'ew')
        update_time()

        menu.grid(row = 1, column = 0, sticky = 'nsew')
        menuLabel.grid(row = 0, column = 0, sticky = 'nsew')
        addBookBtn.grid(row=1, column=0, sticky='ew')
        addCustomerBtn.grid(row=2, column=0, sticky='ew')
        addOrderBtn.grid(row=3, column=0, sticky='ew')
        quitBtn.grid(row=4, column=0, sticky='ew')
        
        system = Frame(self)
        system.grid(row = 1, column = 1, sticky = 'n')

        data = Frame(self)
        data.grid(row = 1, column = 2)
    
    def show_add_book_form(self):
        #form = Toplevel(self)
        #form.title("Add Book")
        global system
        system.destroy()
        system = Frame(self)
        system.grid(row = 1, column = 1, sticky = 'n')

        Label(system, text="Title").pack()
        title_entry = Entry(system)
        title_entry.pack()

        Label(system, text="Author").pack()
        author_entry = Entry(system)
        author_entry.pack()

        Label(system, text="ISBN").pack()
        isbn_entry = Entry(system)
        isbn_entry.pack()

        Label(system, text="Price").pack()
        price_entry = Entry(system)
        price_entry.pack()

        Label(system, text="Quantity").pack()
        quantity_entry = Entry(system)
        quantity_entry.pack()

        #####

        global data
        data.destroy()
        data = Frame(self)
        data.grid(row = 1, column = 2)

        def add_book():
            title = title_entry.get()
            author = author_entry.get()
            isbn = isbn_entry.get()
            price = float(price_entry.get())
            quantity = int(quantity_entry.get())

            new_book = Book(title, author, isbn, price, quantity)
            new_book.save_to_db()
            print(f"Book Added: {new_book.title}")
            #form.destroy()
            self.view_inventory()

        Button(system, text="Add", command=add_book).pack()
    
    def show_add_customer_form(self):
        #form = Toplevel(self)
        #form.title("Add Customer")

        global system
        system.destroy()
        system = Frame(self)
        system.grid(row = 1, column = 1, sticky = 'n')

        Label(system, text="Name").pack()
        name_entry = Entry(system)
        name_entry.pack()

        Label(system, text="Customer ID").pack()
        customer_id_entry= Entry(system)
        customer_id_entry.pack()

        Label(system, text="Email").pack()
        email_entry = Entry(system)
        email_entry.pack()

        Label(system, text="Phone Number").pack()
        phone_entry = Entry(system)
        phone_entry.pack()

        #####

        global data
        data.destroy()
        data = Frame(self)
        data.grid(row = 1, column = 2)

        def add_customer():
            name = name_entry.get()
            customer_id = customer_id_entry.get()
            email = email_entry.get()
            phone_number = phone_entry.get()

            new_customer = Customer(name, customer_id, email, phone_number)
            new_customer.save_tp_db()
            print(f"Customer Added: {new_customer.name}")
            #form.destroy()
            self.view_customers()

        Button(system, text="Add", command=add_customer).pack()

    def show_add_order_form(self):
        #form = Toplevel(self)
        #form.title("Add Order")

        global system
        system.destroy()
        system = Frame(self)
        system.grid(row = 1, column = 1, sticky = 'n')

        Label(system, text="Customer ID").pack()
        customer_id_entry = Entry(system)
        customer_id_entry.pack()

        Label(system, text="Book ID").pack()
        book_id_entry = Entry(system)
        book_id_entry.pack()

        Label(system, text="Order Date (YYYY-MM-DD)").pack()
        order_date_entry = Entry(system)
        order_date_entry.pack()

        #####

        global data
        data.destroy()
        data = Frame(self)
        data.grid(row = 1, column = 2)

        def add_order():
            customer_id = int(customer_id_entry.get())
            book_id = int(book_id_entry.get())
            order_date = order_date_entry.get()

            new_order = Order(customer_id, book_id, order_date)
            new_order.save_to_db()
            print(f"Order Added: Customer ID {new_order.customer_id}, Book ID {new_order.book_id}")
            #form.destroy()
        
        Button(system, text="Add", command=add_order).pack()

    def quit(self):
        self.destroy()


if __name__ == "__main__":
    app = BookstoreApp()
    app.mainloop()
