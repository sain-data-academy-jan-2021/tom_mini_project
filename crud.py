from util import app_header, validate_number
from printing import print_from_db_menu
from database import connect_to_db, execute_sql_crud, execute_sql_select, execute_sql_select_
import database

# Create a new courier/product 
def add_item_write_to_db(what, val, table, added_item):
    connection = database.connect_to_db()
    while True:
        if what == "Product":
            try:
                added_val = float(input(f'Please enter the {val} of the {added_item} you wish to add...'))
                database.execute_sql_crud(connection, f'INSERT INTO products (product_name, product_price) VALUES ("{added_item}", {added_val})')
            except ValueError:
                print("You have not entered a price, please try again...")
                continue
        elif what == "Courier":
            added_number = validate_number('courier')
            database.execute_sql_crud(connection, f'INSERT INTO couriers (courier_name, courier_number) VALUES ("{added_item}", "{added_number}")')
        break
    

# Create a new order
def add_order(connection, what, val, table): 
    while True: 
        connection = connect_to_db()
        app_header("Create New Order")
        cust_name = input(f"Please enter the customer's name...\n \nPlease press 0 if you wish to return to the previous menu...")
        if cust_name == "0":
            break
        else:
            cust_address = input("Please enter the customer's address...").title()
            cust_num = validate_number('customer')
            courier = assign_courier_to_order(connection)
            cour=courier[0]
            status = 'Order Received'
            products_to_add = assign_products_to_order(connection)
            execute_sql_crud(connection, (f' INSERT INTO orders (customer_name, customer_address, phone_number, order_status, courier_assigned) VALUES ("{cust_name}", "{cust_address}", "{cust_num}", "{status}", "{cour}")')) 
            order_id = execute_sql_select_('SELECT MAX(orders_id) from orders')[0][0]
            for product in products_to_add:
                execute_sql_crud(connection,(f" INSERT INTO order_product (order_id, product_id) VALUES ('{order_id}', '{product}')"))
            break

# Replace product / courier function
def replace_item_write_to_db(connection, what, val, table, item_to_replace):
    connection = connect_to_db()
    while True:
        if what == "Product":
            new_product = input("Please enter the product you wish to add to the menu...").title()
            new_product_price = float(input(f"Please enter the price for the {new_product}...    £"))
            execute_sql_crud(connection, (f'UPDATE products SET product_name = "{new_product}" WHERE products_id = {item_to_replace}'))
            execute_sql_crud(connection, (f'UPDATE products SET product_price = {new_product_price} WHERE products_id = {item_to_replace}'))
            break
        elif what == "Courier":
            new_courier = input("Please enter the name of the courier you wish to add to the roster...")
            new_courier_number = validate_number('courier')
            execute_sql_crud(connection, (f'UPDATE {table} SET courier_name = "{new_courier}" WHERE couriers_id = {item_to_replace}'))
            execute_sql_crud(connection, (f'UPDATE {table} SET courier_number = "{new_courier_number}" WHERE couriers_id = {item_to_replace}'))
            connection.close()
            break

# Replace function for orders 
def replace_order_options_in_db(connection, what, val, table):
    while True: 
        app_header("Order List")
        print_from_db_menu('orders')
        id_of_order_to_change = input('Please enter the order ID for the order that you want to update...\n \nPlease press 0 if you wish to return to the previous menu...')
        if id_of_order_to_change == "0":
            break
        else: 
            updated_name = input("Enter updated name...").title()
            updated_address = input("Enter updated address...").title()
            updated_number = input("Enter updated number...")
            app_header("Courier Table")
            print_from_db_menu('couriers')
            updated_courier = input("Enter updated courier...")
            updated_status = choose_order_status()
            products_to_add = assign_products_to_order(connection)

            if updated_name == "":
                pass
            else:
                execute_sql_crud(connection, (f'UPDATE orders SET customer_name = "{updated_name}" WHERE orders_id = {id_of_order_to_change}'))
            if updated_address == "":
                pass
            else:
                execute_sql_crud(connection, (f'UPDATE orders SET customer_address = "{updated_address}" WHERE orders_id = {id_of_order_to_change}'))
            if updated_number == "":
                pass
            else: 
                execute_sql_crud(connection, (f'UPDATE orders SET phone_number = "{updated_number}" WHERE orders_id = {id_of_order_to_change}'))
            if updated_courier == "":
                pass
            else: 
                execute_sql_crud(connection, (f'UPDATE orders SET courier_assigned = "{updated_courier}" WHERE orders_id =  {id_of_order_to_change}'))
            if updated_status == "":
                pass
            else:
                execute_sql_crud(connection, (f'UPDATE orders SET order_status = "{updated_status}" WHERE orders_id =   {id_of_order_to_change}'))
            if products_to_add == "":
                pass
            else:
                execute_sql_crud(connection, (f'DELETE FROM order_product WHERE order_id = {id_of_order_to_change}'))
                for product in products_to_add:
                    execute_sql_crud(connection,(f" INSERT INTO order_product (order_id, product_id) VALUES ('{id_of_order_to_change}', '{product}')"))
                break


# Update an item generic write to database function
def update_item_write_to_db(what, val, table, update_item):
    connection = connect_to_db()
    while True:
        if what == "Product":
            try:
                new_price = float(input(f'Please enter the new price for the product {update_item}...    £'))
            except ValueError:
                print("You have not entered a price, please try again...")
                continue
            else:
                execute_sql_crud(connection, (f'UPDATE products SET product_price = {new_price} WHERE products_id = {update_item}'))
        elif what == "Courier":
            added_number = validate_number('courier')
            execute_sql_crud(connection, (f'UPDATE {table} SET courier_number = "{added_number}" WHERE couriers_id = {update_item}'))
        elif what == "Order":
            updated_status = choose_order_status()
            execute_sql_crud(connection, (f'UPDATE {table} SET order_status = "{updated_status}" WHERE orders_id ={update_item}'))
        connection.close() 
        break

# Delete function - generic for products, couriers and orders 
def delete_row(connection, what, val, table): 
    existing_ids = [id[0] for id in execute_sql_select(connection, (f'SELECT {table}_id from {table}'))]
    app_header(f"{what} Screen")
    print_from_db_menu(table)
    while True: 
        try:
            item_to_delete = input(f"Please choose which {what} you wish to delete...")
            if int(item_to_delete) not in existing_ids:
                print(f"You did not choose a valid {what} ID, please try again...")
                continue
            else:
                if what == "Product":
                    execute_sql_crud(connection, (f'DELETE FROM products where products_id = {item_to_delete}'))
                elif what ==  "Courier":
                    execute_sql_crud(connection, (f'DELETE FROM couriers where couriers_id = {item_to_delete}'))
                elif what == "Order":
                    execute_sql_crud(connection, (f'DELETE FROM order_product WHERE order_id = {item_to_delete}'))
                    execute_sql_crud(connection, (f'DELETE FROM orders WHERE orders_id = {item_to_delete}'))
                connection.close()
                break
        except ValueError:
            print("There has been an error, please try again...")
            break


# Misc 

# Choose status of order from pre defined list

def choose_order_status():
    app_header("Choose Order Status")

    status_choice = input(
            ''' Please update the status of the order...

            1. Order Received
            2. Order Preparing
            3. Order Delivered
            4. Order Cancelled

        Please choose an option from 1 - 4.... 
        '''
        )

    if status_choice == "1": 
        return("Order Received")
    elif status_choice == "2": 
        return ("Order Preparing")
    elif status_choice == "3": 
        return ("Order Delivered")
    elif status_choice == "4": 
        return ("Order Cancelled")

# Assign a courier to an order - used in create and replace functions
def assign_courier_to_order(connection):
    existing_courier_ids = [courier_id[0] for courier_id in execute_sql_select(connection, ('SELECT couriers_id from couriers'))]
    chosen_courier_id = []
    app_header("Courier List")
    print_from_db_menu('couriers')
    while True: 
        assigned_courier = input("Please enter a courier you want to assign to the order...")
        if int(assigned_courier) not in existing_courier_ids:
            print("Invalid Courier ID, please try again...")
            continue
        elif assigned_courier in existing_courier_ids:
            break
        chosen_courier_id.append(assigned_courier)
        return chosen_courier_id

# Assign products to an order - used in create and replace functions
def assign_products_to_order(connection):
    existing_product_ids = [products_id[0] for products_id in execute_sql_select(connection, ('SELECT products_id from products'))]
    chosen_product_id = []
    app_header("Product List")
    print_from_db_menu('products')
    print()
    print("Press 0 when you have assigned all products to this order.")
    print()
    while True: 
        assigned_product = input("Please enter a product you want to assign to the order...")
        if int(assigned_product) == 0:
            break
        elif int(assigned_product) not in existing_product_ids:
            print("Invalid product ID, please try again...")
            continue
        chosen_product_id.append(assigned_product)
    return chosen_product_id