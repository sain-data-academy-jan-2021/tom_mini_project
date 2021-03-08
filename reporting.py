from collections import Counter 
import matplotlib.pyplot as plt 
import math
from util import app_header
from database import connect_to_db, execute_sql_crud, execute_sql_select, execute_sql_select_
from printing import print_from_db_menu,report_table

def report_1(table):
    # Report to show the customer name, address and list of products in an order.
    connection = connect_to_db()
    existing_order_ids = [orders_id[0] for orders_id in execute_sql_select(connection, ('SELECT orders_id from orders'))]
    app_header("Reporting Screen")
    print_from_db_menu(table)
    while True:
        id = input("Please choose an order from the list above...")
        if int(id) in existing_order_ids:
            results = execute_sql_select(connection, (f'SELECT o.customer_name, o.customer_address, p.product_name from order_product op join orders o on op.order_id = o.orders_id join products p on op.product_id = p.products_id where o.orders_id = {id}'))
            name = results[0][0]
            address = results[0][1]
            products = []
            for row in results:
                products.append(row[2])
            app_header(f"{name}'s Order")
            print(f'''
                    Customer Name
            *|---------------------------|*
                    {name}
            *|---------------------------|*
            
            
                    Customer Address
            *|---------------------------|*
                    {address}
            *|---------------------------|*
            
            
                    Ordered Items
            *|---------------------------|*''')
            for x in products:
                print("              ",x)
            print("            *|---------------------------|*")
            print()
            print()
            break
        else:
            print("Please enter a valid ID from the above list...")

def report_2():
    # Report to show the customer name, address, for orders not yet delivered 
    connection = connect_to_db()
    app_header("Orders yet to be delivered...")
    results = execute_sql_select(connection, (f'SELECT customer_name, customer_address, order_status from orders where order_status = "Order Received" or order_status = "Order Preparing"'))
    name = []
    address = []
    order_status = []
    for row in results:
        name.append(row[0])    
    for row in results:
        address.append(row[1])    
    for row in results:
        order_status.append(row[2]) 
    report_table(name, address, order_status)

def report_3():
    # Report to show the customer name, address, for orders delivered
    connection = connect_to_db()
    app_header("Delivered Orders Screen")
    results = execute_sql_select(connection, (f'SELECT customer_name, customer_address, order_status from orders where order_status = "Order Delivered"'))
    name = []
    address = []
    order_status = []
    for row in results:
        name.append(row[0])    
    for row in results:
        address.append(row[1])    
    for row in results:
        order_status.append(row[2]) 
    report_table(name, address, order_status)

    
def report_4():
    # Report to show the customer name, address, for orders cancelled
    connection = connect_to_db()
    app_header("Cancelled Orders")
    results = execute_sql_select(connection, (f'SELECT customer_name, customer_address, order_status from orders where order_status = "Order Cancelled"'))
    name = []
    address = []
    order_status = []
    for row in results:
        name.append(row[0])    
    for row in results:
        address.append(row[1])    
    for row in results:
        order_status.append(row[2]) 
    report_table(name, address, order_status)

# Pie chart depicting Order status percentages 
def report_5():
    connection = connect_to_db()
    o_status = execute_sql_select(connection, ('SELECT order_status FROM orders'))

    counts = Counter(x[0] for x in o_status)
    d = (counts['Order Delivered'])
    r = (counts['Order R
    c = (counts['Order Canceleceived'])led'])
    p = (counts['Order Preparing'])

    labels = 'Orders Received', 'Orders Preparing', 'Orders Delivered', 'Orders Cancelled'
    sizes = [r, p, d, c]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.0f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')
    plt.title("Pie Chart showing status of all orders (%)")

    plt.show()

# Bar chart showing number of orders assigned per courier 
def report_6(): 
    connection = connect_to_db()
    o_courier_assigned = execute_sql_select(connection, ('SELECT courier_assigned FROM orders'))
    o_courier_names = execute_sql_select(connection, ('SELECT courier_name FROM couriers'))
    counts = Counter(x[0] for x in o_courier_assigned)
    
    no_of_deliveries = list(counts.values())
    
    name_list = []
    for name in o_courier_names:
        name_list.append(name[0])

    plt.bar(name_list, no_of_deliveries, color ='maroon',  
        width = 0.4) 
    
    yint = range(min(no_of_deliveries), math.ceil(max(no_of_deliveries))+1)
    plt.yticks(yint)
    
    plt.xlabel("COURIER NAMES") 
    plt.ylabel("NO OF DELIVERIES ASSIGNED") 
    plt.title("Number of Deliveries Assigned per Courier") 
    plt.show()  