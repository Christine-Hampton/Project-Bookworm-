class Order:
    def __init__(self, order_id, customer_id, list_of_books, order_date):
        self.order_id = order_id
        self.customer_id = customer_id
        self.list_of_books = list_of_books
        self.order_date = order_date 

    def add_order(self):
        # add order to database
        pass
    
    def update_order(self):
        # update order details
        pass

    def remove_order(self):
        # remover order from database
        pass
