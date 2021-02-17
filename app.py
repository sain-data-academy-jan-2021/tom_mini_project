# v.0.19
import sys
import util
import pymysql
import tabulate


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

def start_app():
    contents = input(
        """
    1: Product Menu... 
    2: Courier Screen...
    3: Order Menu....
    0: Exit App...
    
    Please enter your choice:
    """
    )
    if contents == "1":
        util.header("Product Screen")
        menu("Product","price", "products")
        
    elif contents == "2":
        util.header("Courier Screen")
        menu("Courier", "number", "couriers")
        
    elif contents == "3":
        util.header("Order Screen")
        menu("Order", "Status", "orders")
        
    elif contents == "0":
        exit_app()
        
    else:
        start_app_return_option()

def menu(what, val, table):

    start_option = input(
        f"""Please select from the following options:
        
    0)   Return to Main Menu
    1)   Print Out {what} List
    2)   Create {what}
    3)   Update {what} {val}
    4)   Replace {what}
    5)   Delete {what}
    6)   Exit App
            """
    )
    if start_option == "0":
        util.header("Main Screen")
        start_app()
    elif start_option == "1":
        print_from_db_menu(table)
        return_option(what, val, table)
    elif start_option == "2":
        add_item_to_db(what, val, table)
    elif start_option == "3":
        update_item_from_db(what, val, table)
    elif start_option == "4":
        replace_item_in_db(what, val, table)
    elif start_option == "5":
        delete_item_from_db(what, val, table)
    elif start_option == "6":
        exit_app()
    else:
        menu_return_option_with_error(what, val, table)

def print_from_db_menu(table):
    if table == 'products':
        util.header("Product Menu")
        print_from_list_using_tabulate(products_list)
    elif table == 'couriers':
        util.header("Courier List")
        print_from_list_using_tabulate(couriers_list)
    elif table == 'orders':
        util.header("Order List")
        print_from_list_using_tabulate(orders_list)

def print_from_list_using_tabulate(list):
    if list == products_list:
        header = ["Product ID", "Product Name", "Price"]
    elif list == couriers_list:
        header = ["Courier ID", "Courier Name", "Phone Number"]
    elif list == orders_list:
        header = ["Order ID", "Customer Name", "Customer Address", "Customer Number", "Order Status", "Assigned Courier", "Item's Ordered"]
    rows = [x.values() for x in list]
    print(tabulate.tabulate(rows, header, tablefmt = 'pretty'))

def add_item_to_db(what, val, table):
    if table == 'products':
        add_product_menu(what, val, table)
    elif table == 'couriers':
        add_courier_to_db(what, val, table)
    elif table == 'orders':
        add_order_to_db(what, val, table)
    return_option(what, val, table)

def add_product_menu(what, val, table):
    added_item = input('Please enter the name of the product you wish to add...\n \nPlease press 0 if you wish to return to the previous menu...')
    if added_item == "0":
        util.header("Product Screen")
        menu_return_option(what, val, table)
    else:
        add_product_write_to_db(what, val, table, added_item)
        
def add_product_write_to_db(what, val, table, added_item):
    added_price = input(f'Please enter the price of the {added_item} you wish to add...')
    while added_price:
        try:
            cursor = connection.cursor()
            added_price = float(added_price)
            cursor.execute(f'INSERT INTO products (product_name, product_price) VALUES ("{added_item}", {added_price})')
            cursor.close()
            connection.commit()
            connection.close()
            menu_return_option(what, val, table)
        except ValueError:
            print('The input you entered is not a valid price, please try again...')
            add_product_write_to_db(what, val, table, added_item)

def add_courier_to_db(what, val, table): 
    added_item = input('Please enter the name of the courier you wish to add...\n \nPlease press 0 if you wish to return to the previous menu...')
    if added_item == "0":
        util.header("Courier Screen")
        menu_return_option(what, val, table)
    else:
        cursor = connection.cursor()
        added_number = input(f'Please enter the phone number of the {added_item} you wish to add...')
        cursor.execute(f'INSERT INTO couriers (courier_name, courier_number) VALUES ("{added_item}", "{added_number}")')
        cursor.close()
        connection.commit()
        connection.close()
        menu_return_option(what, val, table)

def add_order_to_db(what, val, table):
    cursor = connection.cursor()
    cust_name = input(f"Please enter the customer's name...\n \nPlease press 0 if you wish to return to the previous menu...")
    if cust_name == "0":
        util.header("Order Screen")
        menu_return_option(what, val, table)
    else:
        cust_address = input("Please enter the customer's address...").title()
        cust_num = input("Please enter the customer's number...")
        util.header("Product List")
        print_from_list_using_tabulate(products_list)
        cust_order = input("What would the customer like to order?")
        status = ('Order Received')
        util.header("Courier List")
        print_from_list_using_tabulate(couriers_list)
        courier_assigned = input("Please enter a courier you want to assign to the order...")
        cursor.execute(f'INSERT INTO orders (customer_name, customer_address, phone_number, order_status,   courier_assigned, customer_order) VALUES ("{cust_name}", "{cust_address}", "{cust_num}", "{status}", "    {courier_assigned}", "{cust_order}")')    
        cursor.close()
        connection.commit()
        connection.close()

def update_item_from_db(what, val, table):
    if table == 'products':
        update_product_price_in_db(what, val, table)
    elif table == 'couriers':
        update_courier_number_in_db(what, val, table)
    elif table == 'orders':
        update_order_courier_status_in_db(what, val, table)
    return_option(what, val, table)
    
# NEED TO READ THROUGH LIST OF IDS TO DETERMINE WHETHER EXISTS OR NOT 
def update_product_price_in_db(what, val, table):
    cursor = connection.cursor()
    print_from_db_menu(table)
    product_to_change = input('Please enter the ID for the product you want to update the price for...\n \nPlease press 0 if you wish to return to the previous menu...')
    if product_to_change == "0":
        util.header("Product Screen")
        menu_return_option(what, val, table)
    else:  
    #THIS NEEDS FIXING - OUTPUTS NO AND YES VALUES FOR ALL ITEMS IN DICTIONARY
        for x in products_list:
            if x['product_id'] == id:
                new_price = input(f'Please enter the new price for the product...')
                cursor.execute(f'UPDATE products SET product_price = {new_price} WHERE  product_id = {product_to_change}')
                cursor.close()
                connection.commit()
                connection.close() 
            elif x['product_id'] != id:
                print(" You chose an invalid ID.")
                return_option(what, val, table)

def update_courier_number_in_db(what, val, table):
    print_from_db_menu(table)
    print()
    courier_to_change = input('Please enter the ID for the courier whose number you want to update...\n \nPlease press 0 if you wish to return to the previous menu...')
    if courier_to_change == "0":
        util.header("Courier Screen")
        menu_return_option(what, val, table)
    else:
        update_courier_number_write_to_db(what, val, table, courier_to_change)

def update_courier_number_write_to_db(what, val, table, courier_to_change):
    new_number = input(f'Please enter the new phone number...')
    while new_number: 
        try:
            cursor = connection.cursor()
            new_number = int(new_number)
            new_new_number = '0' + str(new_number)
            cursor.execute(f'UPDATE {table} SET courier_number = ("{new_new_number}") WHERE   courier_id = {courier_to_change}')
            cursor.close()
            connection.commit()
            menu_return_option(what, val, table)
        except ValueError:
            print('The input you entered is not a valid phone number, please try again...')
            update_courier_number_write_to_db(what, val, table, courier_to_change)

# NEED TO READ THROUGH LIST OF IDS TO DETERMINE WHETHER EXISTS OR NOT 
def update_order_courier_status_in_db(what, val, table):
    cursor = connection.cursor()
    util.header("Order List")
    print_from_list_using_tabulate(orders_list)
    id_for_status_change = input('Please enter the ID of the order you wish to change...\n \nPlease press 0 if you wish to return to the previous menu...')
    if id_for_status_change == "0":
        util.header("Order Screen")
        menu_return_option(what, val, table)
    else:
        updated_status = input('Please enter the updated Status...').title()
        cursor.execute(f'UPDATE {table} SET order_status = "{updated_status}" WHERE     order_id ={id_for_status_change}')
        cursor.close()
        connection.commit()
        connection.close()

def replace_item_in_db(what, val, table):
    if table == 'products':
        replace_product_menu(what, val, table)
    elif table == 'couriers':
        replace_courier_in_db(what, val, table)
    elif table == 'orders':
        replace_order_options_in_db(what, val, table)
    return_option(what, val, table)
    
def replace_product_menu(what, val, table):
    print_from_db_menu(table)
    product_to_change = input('Please enter the ID for the product you want to replace...\n \nPlease press 0 if you wish to return to the previous menu...')
    if product_to_change == "0":
        util.header("Product Screen")
        menu_return_option(what, val, table)
    else:
        new_product = input("Please enter the product you wish to add to the menu...").title()
        replace_product_write_to_db(what, val, table, product_to_change, new_product)

def replace_product_write_to_db(what, val, table, product_to_change, new_product):
    new_product_price = input(f"Please enter the price for the {new_product}.")        
    while new_product_price:
        try:
            cursor = connection.cursor()
            new_product_price = float(new_product_price)
            cursor.execute(f'UPDATE products SET product_name = "{new_product}" WHERE product_id = {product_to_change}')
            cursor.execute(f'UPDATE products SET product_price = {new_product_price} WHERE product_id = {product_to_change}')
            cursor.close()
            connection.commit()
            connection.close()  
            menu_return_option(what, val, table)
        except ValueError:
            print('The input you entered is not a valid price, please try again...')
            replace_product_write_to_db(what, val, table, product_to_change, new_product)

def replace_courier_in_db(what, val, table):
    cursor = connection.cursor()
    print_from_db_menu(table)
    courier_to_change = input('Please enter the ID for the courier you want to replace...\n \nPlease press 0 if you wish to return to the previous menu...')
    if courier_to_change == "0":
        util.header("Courier Screen")
        menu_return_option(what, val, table)
    else:
        new_courier = input("Please enter the name of the courier you wish to add to the roster...")
        new_courier_number = str(input(f"Please enter the phone number for the {new_courier}."))
        cursor.execute(f'UPDATE {table} SET courier_name = "{new_courier}" WHERE courier_id = {courier_to_change}')
        cursor.execute(f'UPDATE {table} SET courier_number = "{new_courier_number}" WHERE courier_id = {courier_to_change}')
        cursor.close()
        connection.commit() 
        connection.close()

def replace_order_options_in_db(what, val, table):
    cursor = connection.cursor()
    util.header("Order List")
    print_from_list_using_tabulate(orders_list)
    id_of_order_to_change = input('Please enter the order ID for the order that you want to update...\n \nPlease press 0 if you wish to return to the previous menu...')
    if id_of_order_to_change == "0":
        util.header("Order Screen")
        menu_return_option(what, val, table)
    else: 
        updated_name = input("Enter updated name...").title()
        updated_address = input("Enter updated address...").title()
        updated_number = input("Enter updated number...")
        util.header("Courier Table")
        print_from_db_menu('couriers')
        updated_courier = input("Enter updated courier...")
        updated_status = input("Enter updated status...").title()
        util.header("Product Menu")
        print_from_db_menu('products')
        updated_order = input("Enter updated order...").title()

        if updated_name == "":
            pass
        else:
            cursor.execute(f'UPDATE orders SET customer_name = "{updated_name}" WHERE order_id =    {id_of_order_to_change}')
        if updated_address == "":
            pass
        else:
            cursor.execute(f'UPDATE orders SET customer_address = "{updated_address}" WHERE order_id =  {id_of_order_to_change}')
        if updated_number == "":
            pass
        else: 
            cursor.execute(f'UPDATE orders SET phone_number = "{updated_number}" WHERE order_id =   {id_of_order_to_change}')
        if updated_courier == "":
            pass
        else: 
            cursor.execute(f'UPDATE orders SET courier_assigned = "{updated_courier}" WHERE order_id =  {id_of_order_to_change}')
        if updated_status == "":
            pass
        else:
            cursor.execute(f'UPDATE orders SET order_status = "{updated_status}" WHERE order_id =   {id_of_order_to_change}')
        if updated_order == "":
            pass
        else:
            cursor.execute(f'UPDATE orders SET customer_order = "{updated_order}" WHERE order_id =  {id_of_order_to_change}')
        cursor.close()
        connection.commit()   
        connection.close() 

def delete_item_from_db(what, val, table):
    if table == 'products':
        delete_product_from_db(what, val, table)
    elif table == 'couriers':
        delete_courier_from_db(what, val, table)
    elif table == 'orders':
        delete_order_from_db(what, val, table)
    return_option(what, val, table) 

def delete_product_from_db(what, val, table):
    cursor = connection.cursor()
    print_from_db_menu(table)
    id_to_delete = input('Please enter the ID of the product you wish to delete...\n \nPlease press 0 if you wish to return to the previous menu...')
    if id_to_delete == "0":
        util.header("Product Screen")
        menu_return_option(what, val, table)
    else:
        cursor.execute(f'DELETE FROM products where product_id = {id_to_delete}')
        cursor.close()
        connection.commit()
        connection.close()

def delete_courier_from_db(what, val, table):
    cursor = connection.cursor()
    print_from_db_menu(table)
    id_to_delete = input("Please enter the ID of the courier you wish to delete...\n \nPlease press 0 if you wish to return to the previous menu...")
    if id_to_delete == "0":
        util.header("Courier Screen")
        menu_return_option(what, val, table)
    else:
        cursor.execute(f'DELETE FROM couriers where courier_id = {id_to_delete}')
        cursor.close()
        connection.commit()
        connection.close()

def delete_order_from_db(what, val, table):
    cursor = connection.cursor()
    print_from_db_menu(table)
    id_to_delete = input('Please enter the ID of the order you wish to delete...\n \nPlease press 0 if you wish to return to the previous menu...')
    if id_to_delete == "0":
        util.header("Order Screen")
        menu_return_option(what, val, table)
    else:
        cursor.execute(f'DELETE FROM orders where order_id = {id_to_delete}')
        cursor.close()
        connection.commit()
        connection.close()


def return_option(what, val, table):
    print()
    while True:
        rtn_input = input("Would you like to return to the " + what + " screen? Y/N")
        
        if rtn_input.upper() == "Y" or rtn_input.upper() == "YES":
            util.header(what+" Screen")
            menu(what, val, table)
            
        elif rtn_input.upper() == "N" or rtn_input.upper() == "NO":
            exit_app()
            
        else:
            print("You have not choosen a suitable option, please try again...")
            continue

def start_app_return_option(): 
    util.header("Main Screen")
    print("You must make a selection from 0 - 3")
    print("Please try another selection")
    start_app()

def menu_return_option_with_error(what, val, table): 
    util.header(f"{what} Screen")
    print("You must make a selection from 0 - 6")
    print("Please try another selection")
    print()
    menu(what, val, table)
    
def menu_return_option(what, val, table): 
    util.header(f"{what} Screen")
    print()
    menu(what, val, table)

def exit_app():
    util.header("Cheerio!")
    print("You are now exiting Tominoes, have a nice day!")
    print()
    sys.exit()

util.header("Main Screen")
start_app()


# def add_order_to_db(what, val, table):
#     cursor = connection.cursor()
#     cust_name = input(f"Please enter the customer's name...\n \nPlease press 0 if you wish to return to the previous menu...")
#     if cust_name == "0":
#         util.header("Order Screen")
#         menu_return_option(what, val, table)
#     else:
#         cust_address = input("Please enter the customer's address...").title()
#         cust_num = input("Please enter the customer's number...")
#         util.header("Product List")
#         print_from_list_using_tabulate(products_list)
#         cust_order = input("What would the customer like to order?")
#         status = ('Order Received')
#         util.header("Courier List")
#         print_from_list_using_tabulate(couriers_list)
#         courier_assigned = input("Please enter a courier you want to assign to the order...")
#         cursor.execute(f'INSERT INTO orders (customer_name, customer_address, phone_number, order_status,   courier_assigned, customer_order) VALUES ("{cust_name}", "{cust_address}", "{cust_num}", "{status}", "    {courier_assigned}", "{cust_order}")')    
#         cursor.close()
#         connection.commit()
#         connection.close()



def create_a_new_order(what, val, table):
    cursor = connection.cursor()
    cust_name = input(f"Please enter the customer's name...\n \nPlease press 0 if you wish to return to the previous menu...")
    if cust_name == "0":
        util.header("Order Screen")
        menu_return_option(what, val, table)
    else:
        cust_address = input("Please enter the customer's address...").title()
        cust_num = input("Please enter the customer's number...")
        
        
        
        
        cursor.close()
        connection.commit()
        connection.close()