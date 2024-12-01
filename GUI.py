from tkinter import *
from Book import Book
from customer import Customer 
from order import Order

class BookstoreApp(Tk):
    def __init__(self, *args, **kwargs):
        global system
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
        inventoryBtn = Button(menu, text = "Inventory", font = BtnFont,
                              command = self.Inventory)
        customerBtn = Button(menu, text = "Customers", font = BtnFont,
                             command = self.Customers)
        statusBtn = Button(menu, text = "Status", font = BtnFont,
                           command = self.Status)
        
        header.grid(row = 0, column = 0, columnspan = 10)
        logo.grid(row = 0, column = 0, columnspan = 10, sticky = 'w', padx = 5, pady = 5)
        
        greet.grid(row = 1, column = 0, sticky = 'ew')
        date.grid(row = 1, column = 1, sticky = 'ew')
        clock.grid(row = 1, column = 2, sticky = 'ew')
        update_time()

        menu.grid(row = 1, column = 0, sticky = 'ew')
        menuLabel.grid(row = 0, column = 0, sticky = 'ew')
        inventoryBtn.grid(row = 1, column = 0, sticky = 'ew')
        customerBtn.grid(row = 2, column = 0, sticky = 'ew')
        statusBtn.grid(row = 3, column = 0, sticky = 'ew')

        system = Frame(self)
        system.grid(row = 1, column = 1, sticky = 'n')

    def Inventory(self):
        text = Label(system, text = "It worked!!!!")
        text.grid(row = 0, column = 0)

    def Customers(self):
        text = Label(system, text = "Something different...")
        text.grid(row = 0, column = 0)
        
    def Status(self):
        pass

if __name__ == "__main__":
    app = BookstoreApp()
    app.mainloop()

