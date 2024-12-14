from tkinter import *
from tkinter import ttk
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

        hotbar = Frame(self, bg = 'cyan')
        greet = Label(hotbar, text = " Welcome to the BookWorm Inventory Manager       ", font = HotbarFont, bg = 'cyan')
        date = Label(hotbar, text = time.strftime(date_format, t) + "       ", font = HotbarFont, bg = 'cyan')
        clock = Label(hotbar, text = time.strftime(time_format, t) + " ", font = HotbarFont, bg = 'cyan')

        menu = Frame(self, bg = 'gray')
        menuLabel = Label(menu, text = "Menu", font = HotbarFont, bg = 'gray')
        addBookBtn = Button(menu, text="Book", font=BtnFont,
                            command=self.show_add_book_form)
        addCustomerBtn = Button(menu, text="Customer", font=BtnFont,
                                command=self.show_add_customer_form)
        addOrderBtn= Button (menu, text="Order", font=BtnFont,
                             command=self.show_add_order_form)
        quitBtn = Button(menu, text="Quit", font=BtnFont,
                         command=self.quit)
        

        header.grid(row = 0, column = 0, columnspan = 20, sticky = 'nsew')
        logo.grid(row = 0, column = 0, columnspan = 20, sticky = 'w', padx = 5, pady = 5)

        hotbar.grid(row=1, column=0, columnspan=20, sticky='ew')
        greet.grid(row = 1, column = 0, sticky = 'ew')
        date.grid(row = 1, column = 1, sticky = 'ew')
        clock.grid(row = 1, column = 2, sticky = 'ew')
        update_time()

        menu.grid(row = 2, column = 0, rowspan = 20, sticky = 'nsw')
        menuLabel.grid(row = 0, column = 0, sticky = 'ew')
        addBookBtn.grid(row=1, column=0, sticky='ew')
        addCustomerBtn.grid(row=2, column=0, sticky='ew')
        addOrderBtn.grid(row=3, column=0, sticky='ew')
        quitBtn.grid(row=4, column=0, sticky='ew')
        
        system = Frame(self)
        system.grid(row = 2, column = 1, sticky = 'n')

        data = Frame(self)
        data.grid(row = 2, column = 2)
    
    def show_add_book_form(self):
        #form = Toplevel(self)
        #form.title("Add Book")
        global system
        system.destroy()
        system = Frame(self)
        system.grid(row = 2, column = 1, sticky = 'n', padx = 10, pady = 10)

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
        data.grid(row = 2, column = 2, pady = 10)

        columns = ('book_id', 'title', 'author', 'isbn', 'price', 'quantity')

        base = ttk.Treeview(data, selectmode='browse', columns=columns, show='headings')
        base.pack(side='left')

        vscroll = Scrollbar(data, orient='vertical', command=base.yview)
        vscroll.pack(side='right', fill='x')
        base.configure(xscrollcommand=vscroll.set)

        base.heading('book_id', text='Book ID')
        base.heading('title', text='Title')
        base.heading('author', text='Author')
        base.heading('isbn', text='ISBN')
        base.heading('price', text='Price')
        base.heading('quantity', text='Quantity')

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
            view_inventory()

        def view_inventory():
            for record in base.get_children():
                base.delete(record)
            conn = sqlite3.connect('bookstore.db')
            c = conn.cursor()
            c.execute("SELECT * FROM books")
            records = c.fetchall()
            for record in records:
                base.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3], record[4], record[5]))
            conn.commit()
            conn.close()
                
        Button(system, text="Add", command=add_book).pack()
        view_inventory()
    
    def show_add_customer_form(self):
        #form = Toplevel(self)
        #form.title("Add Customer")

        global system
        system.destroy()
        system = Frame(self)
        system.grid(row = 2, column = 1, sticky = 'n', padx = 10, pady = 10)

        Label(system, text="Name").pack()
        name_entry = Entry(system)
        name_entry.pack()

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
        data.grid(row = 2, column = 2, pady = 10)

        columns = ('cust_id', 'name', 'email', 'phone_num')

        base = ttk.Treeview(data, selectmode='browse', columns=columns, show='headings')
        base.pack(side='left')

        vscroll = Scrollbar(data, orient='vertical', command=base.yview)
        vscroll.pack(side='right', fill='x')
        base.configure(xscrollcommand=vscroll.set)

        base.heading('cust_id', text='Customer ID')
        base.heading('name', text='Name')
        base.heading('email', text='Email')
        base.heading('phone_num', text='Phone Number')

        def add_customer():
            name = name_entry.get()
            email = email_entry.get()
            phone_number = phone_entry.get()

            new_customer = Customer(name, email, phone_number)
            new_customer.save_to_db()
            print(f"Customer Added: {new_customer.name}")
            #form.destroy()
            view_customers()

        def view_customers():
            for record in base.get_children():
                base.delete(record)
            conn = sqlite3.connect('bookstore.db')
            c = conn.cursor()
            c.execute("SELECT * FROM customers")
            records = c.fetchall()
            for record in records:
                base.insert(parent='', index='end', text='', values=(record[0], record[1], record[2], record[3]))
            conn.commit()
            conn.close()

        Button(system, text="Add", command=add_customer).pack()
        view_customers()

    def show_add_order_form(self):
        #form = Toplevel(self)
        #form.title("Add Order")

        global system
        system.destroy()
        system = Frame(self)
        system.grid(row = 2, column = 1, sticky = 'n', padx = 10, pady = 10)

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
        data.grid(row = 2, column = 2, pady = 10)

        columns = ('cust_id', 'book_id', 'order_date')

        base = ttk.Treeview(data, selectmode='browse', columns=columns, show='headings')
        base.pack(side='left')

        vscroll = Scrollbar(data, orient='vertical', command=base.yview)
        vscroll.pack(side='right', fill='x')
        base.configure(xscrollcommand=vscroll.set)

        base.heading('cust_id', text='Customer ID')
        base.heading('book_id', text='Book ID')
        base.heading('order_date', text='Order Date')

        def add_order():
            customer_id = int(customer_id_entry.get())
            book_id = int(book_id_entry.get())
            order_date = order_date_entry.get()

            new_order = Order(customer_id, book_id, order_date)
            new_order.save_to_db()
            print(f"Order Added: Customer ID {new_order.customer_id}, Book ID {new_order.book_id}")
            #form.destroy()
            view_orders()

        def view_orders():
            for record in base.get_children():
                base.delete(record)
            conn = sqlite3.connect('bookstore.db')
            c = conn.cursor()
            c.execute("SELECT * FROM orders")
            records = c.fetchall()
            for record in records:
                base.insert(parent='', index='end', text='', values=(record[1], record[2], record[3]))
            conn.commit()
            conn.close()

        view_orders()
        Button(system, text="Add", command=add_order).pack()

    def quit(self):
        self.destroy()


if __name__ == "__main__":
    app = BookstoreApp()
    app.mainloop()

