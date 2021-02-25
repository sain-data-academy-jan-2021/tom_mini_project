import pymysql
import util
import tabulate
import matplotlib.pyplot as plt 
import numpy as np
from collections import Counter

import pandas as pd
from pandas import Series, DataFrame


# Run at start of app
connection = pymysql.connect("localhost", "root", "password", "miniproject")

def ReadFromDatabase(table):
    result = []
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    field_names = [i[0] for i in cursor.description]
    for row in rows:
        outerdict = {}
        j = 0
        for x in row:
            outerdict[field_names[j]] = x
            j += 1
        result.append(outerdict)
    cursor.close()
    return result

products_list = ReadFromDatabase('products')
couriers_list = ReadFromDatabase('couriers')
orders_list = ReadFromDatabase('orders')

#print(orders_list)

def print_from_list_using_tabulate(list):
    if list == products_list:
        header = ["Product ID", "Product Name", "Price"]
    elif list == couriers_list:
        header = ["Courier ID", "Courier Name", "Phone Number"]
    elif list == orders_list:
        header = ["Order ID", "Customer Name", "Customer Address", "Customer Number", "Order Status", "Assigned Courier", "Item's Ordered"]
    rows = [x.values() for x in list]
    print(tabulate.tabulate(rows, header, tablefmt = 'fancy_grid'))

# Function to execute sql queries (from Colin)
def execute_sql_select(connection, statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    cursor.close()
    return cursor.fetchall()

# Function to undertake sql edits (from Colin)
def execute_sql_add_delete_update(statement):
    cursor = connection.cursor()
    cursor.execute(statement)
    cursor.close()
    connection.commit()

# Prints orders out in list of lists
def view_orders():
    for orders in execute_sql_select('select * from orders'):
        print(orders)
#view_orders()

def assign_courier_to_order():
    existing_courier_ids = [courier_id[0] for courier_id in execute_sql_select('SELECT couriers_id from couriers')]
    chosen_courier_id = []
    util.header("Courier List")
    print_from_list_using_tabulate(couriers_list)
    while True: 
        assigned_courier = input("Please enter a courier you want to assign to the order...")
        if int(assigned_courier) not in existing_courier_ids:
            print("Invalid Courier ID, please try again...")
            continue
        elif assigned_courier in existing_courier_ids:
            break
        chosen_courier_id.append(assigned_courier)
        return chosen_courier_id
        
#assign_courier_to_order()

def assign_products_to_order():
    existing_product_ids = [products_id[0] for products_id in execute_sql_select('SELECT products_id from products')]
    chosen_product_id = []
    util.header("Courier List")
    print_from_list_using_tabulate(products_list)
    while True: 
        assigned_product = input("Please enter a product you want to assign to the order...")
        # if assigned_product != int: 
        #     print("Please enter a valid product ID...")
        #     continue
        if int(assigned_product) == 0:
            break
        # SPEAK TO MARCUS REGARDING ENTERING A SPLIT STATEMENT HERE 
        elif int(assigned_product) not in existing_product_ids:
            print("Invalid product ID, please try again...")
            continue
        chosen_product_id.append(assigned_product)
    return chosen_product_id
    


def add_order(): 
    cust_name = input(f"Please enter the customer's name...\n \nPlease press 0 if you wish to return to the previous menu...")
    if cust_name == "0":
        util.header("Order Screen")
        #menu_return_option(what, val, table)
    else:
        cust_address = input("Please enter the customer's address...").title()
        cust_num = input("Please enter the customer's number...")
        courier = assign_courier_to_order()
        cour=courier[0]
        status = 'Order Received'
        products_to_add = assign_products_to_order()
        execute_sql_add_delete_update(f' INSERT INTO orders (customer_name, customer_address, phone_number, order_status, courier_assigned) VALUES ("{cust_name}", "{cust_address}", "{cust_num}", "{status}", "{cour}")') 
        order_id = execute_sql_select('SELECT MAX(orders_id) from orders')[0][0]
        for product in products_to_add:
            execute_sql_add_delete_update(f" INSERT INTO order_product (order_id, product_id) VALUES ('{order_id}', '{product}')")
# add_order()


# def delete_order(): 
#     existing_order_ids = [products_id[0] for products_id in execute_sql_select('SELECT orders_id from orders')]
#     util.header("Order Screen")
#     print_from_list_using_tabulate(orders_list)
#     while True: 
#         order_id_to_delete = input("Please choose which order you wish to delete...")
#         if int(order_id_to_delete) in existing_order_ids:
#             execute_sql_add_delete_update(f'DELETE FROM order_product WHERE order_id = {order_id_to_delete}')
#             execute_sql_add_delete_update(f'DELETE FROM orders WHERE orders_id = {order_id_to_delete}')
#             break
#         else:
#             util.header("Order Screen")
#             print_from_list_using_tabulate(orders_list)
#             print('Please select a valid ID from the orders list...')
            
#delete_order()

# def report_1():
#     # Report to show the customer name, address and list of products in an order.
#     existing_order_ids = [orders_id[0] for orders_id in execute_sql_select('SELECT orders_id from orders')]
#     util.header("Order Screen")
#     print_from_list_using_tabulate(orders_list)
#     while True:
#         id = input("Please choose an order from the list above...")
#         if int(id) in existing_order_ids:
#             results = execute_sql_select(f'SELECT o.customer_name, o.customer_address, p.product_name from order_product op join orders o on op.order_id = o.orders_id join products p on op.product_id = p.products_id where o.orders_id = {id}')
#             name = results[0][0]
#             address = results[0][1]
#             products = []
#             for row in results:
#                 products.append(row[2])
#             print(name)
#             print(address)
#             print(products)
#             break
#         else:
#             print("Please enter a valid ID from the above list...")

# #report_1()

# def report_2():
#     # Report to show the customer name, address, for orders not yet delivered 
#     util.header("Order Screen")
#     results = execute_sql_select(f'SELECT customer_name, customer_address, order_status from orders where order_status = "Order Received" or order_status = "Order Preparing"')
#     name = []
#     address = []
#     order_status = []
#     for row in results:
#         name.append(row[0])    
#     for row in results:
#         address.append(row[1])    
#     for row in results:
#         order_status.append(row[2]) 
#     print("Name","Address","Order Status")
#     for (a,b,c) in zip(name, address, order_status):
#         print(a,b,c)

# #report_2()

# def report_3():
#     # Report to show the customer name, address, for orders cancelled
#     util.header("Order Screen")
#     results = execute_sql_select(f'SELECT customer_name, customer_address, order_status from orders where order_status = "Order Cancelled"')
#     name = []
#     address = []
#     order_status = []
#     for row in results:
#         name.append(row[0])    
#     for row in results:
#         address.append(row[1])    
#     for row in results:
#         order_status.append(row[2]) 
#     print("Name","Address","Order Status")
#     for (a,b,c) in zip(name, address, order_status):
#         print(a,b,c)
        
# #report_3()


# def report_4():
#     # Report to show the customer name, address, for orders delivered
#     util.header("Order Screen")
#     results = execute_sql_select(f'SELECT customer_name, customer_address, order_status from orders where order_status = "Order Delivered"')
#     name = []
#     address = []
#     order_status = []
#     for row in results:
#         name.append(row[0])    
#     for row in results:
#         address.append(row[1])    
#     for row in results:
#         order_status.append(row[2]) 
#     print("Name","Address","Order Status")
#     for (a,b,c) in zip(name, address, order_status):
#         print(a,b,c)
        
# #report_4()



def report_5(connection):
    o_status = execute_sql_select(connection, ('SELECT order_status FROM orders'))

    counts = Counter(x[0] for x in o_status)
    d = (counts['Order Delivered'])
    r = (counts['Order Received'])
    c = (counts['Order Cancelled'])
    p = (counts['Order Preparing'])

    labels = 'Orders Received', 'Orders Preparing', 'Orders Delivered', 'Orders Cancelled'
    sizes = [r, p, d, c]

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.0f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')
    plt.title("Chart showing status of all orders... ")

    plt.show()
    
def report_6(connection):
    o_courier_assigned = execute_sql_select(connection, ('SELECT courier_assigned FROM orders'))
    o_courier_names = execute_sql_select(connection, ('SELECT courier_name FROM couriers'))
    counts = Counter(x[0] for x in o_courier_assigned)
    
    print(counts)
    q = list(counts.values())
    print(q)
    # a = (counts[1])
    # b = (counts[2])
    # c = (counts[3])
    # d = (counts[4])
    # e = (counts[5]) 
    # f = (counts[6])
    # g = (counts[7])
    # h = (counts[8])
    # i = (counts[9])
    # j = (counts[10])
    # k = (counts[11])
    
    count_list = []
    for x in counts:
        count_list.append(x)
    
    print(count_list)
    
    # aa = (o_courier_names[0][0])
    # bb = (o_courier_names[1][0])
    # cc = (o_courier_names[2][0])
    # dd = (o_courier_names[3][0])
    # ee = (o_courier_names[4][0])
    # ff = (o_courier_names[5][0])
    # gg = (o_courier_names[6][0])
    # hh = (o_courier_names[7][0])
    # ii = (o_courier_names[8][0])
    # jj = (o_courier_names[9][0])
    # kk = (o_courier_names[10][0]) 
    name_list = []
    for name in o_courier_names:
        name_list.append(name[0])
        
    print(name_list)
    
    
    # y_axis = name_list
    # x_axis = q
    
    plt.xticks(range(len(name_list)), q)
    plt.xlabel('Courier')
    plt.ylabel('No of deliveries')
    plt.title('Deliveries per courier')
    plt.bar(range(len(name_list)), q) 
    plt.show()
    
#report_6(connection)
import math

def report_7(connection): 
    
    o_courier_assigned = execute_sql_select(connection, ('SELECT courier_assigned FROM orders'))
    o_courier_names = execute_sql_select(connection, ('SELECT courier_name FROM couriers'))
    counts = Counter(x[0] for x in o_courier_assigned)
    
    no_of_deliveries = list(counts.values())
    
    name_list = []
    for name in o_courier_names:
        name_list.append(name[0])
        
    
    #fig = plt.figure(figsize = (10, 5)) 


    plt.bar(name_list, no_of_deliveries, color ='maroon',  
        width = 0.4) 
    yint = range(min(no_of_deliveries), math.ceil(max(no_of_deliveries))+1)
    plt.yticks(yint)
    plt.xlabel("COURIER NAMES") 
    plt.ylabel("NO OF DELIVERIES ASSIGNED") 
    plt.title("Number of Deliveries Assigned per Courier") 
    plt.show()  
    
report_7(connection)