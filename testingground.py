import sqlite3

with open("customer.txt") as inputfile:
    while True:
        line = inputfile.readline()
        if not line:
            break
        arr = line.strip().split()
        if len(arr) > 0:
            if arr[0] == 'First_name:':
                first_name = arr[1]
            if arr[0] == 'Last_name:':
                last_name = arr[1]
            if arr[0] == 'Customer_id:':
                cus_id = arr[1]
            if arr[0] == 'Email:':
                email = arr[1]
            if arr[0] == 'Phone':
                phone_number = arr[2] + arr[3]
        else:
            conn = sqlite3.connect('bookstore.db')
            c = conn.cursor()
            c.execute("INSERT INTO customers VALUES (:customer_id, :name, :email, :phone_number)",
                      {
                          'customer_id': cus_id,
                          'name': first_name + " " + last_name,
                          'email': email,
                          'phone_number': phone_number
                          }
                      )
            conn.commit()
            conn.close()

print("Sample data added to Customers")
            
            
