import tabulate
from util import app_header
from database import *

# Read from database to dictionary for print_from_db_function

def read_from_database(table):
    connection = connect_to_db()
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
    connection.close()
    return result

# Print function using tabulate

def print_from_db_menu(table):
    list = read_from_database(table)
    if table == 'products':
        app_header("Product Menu")
        header = ["Product ID", "Product Name", "Price"]
    elif table == 'couriers':
        app_header("Courier List")
        header = ["Courier ID", "Courier Name", "Phone Number"]
    elif table == 'orders':
        app_header("Order List")
        header = ["Order ID", "Customer Name", "Customer Address", "Customer Number", "Order Status", "Assigned Courier", "Item's Ordered"]
    rows = [x.values() for x in list]
    print(tabulate.tabulate(rows, header, tablefmt = 'fancy_grid'))
    
def report_table(name, address, order_status):
    for (a,b,c) in zip(name, address, order_status):
        print("*|---------------------------|*")
        print("       ",a)
        print("       ",b)
        print("       ",c)
    print("*|---------------------------|*")
