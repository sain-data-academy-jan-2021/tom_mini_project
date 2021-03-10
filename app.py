
# v.1. ß3
from util import * 
from database import * 
from printing import * 
from reporting import *
from crud import * 

from database import connect_to_db
from printing import print_from_db_menu
from reporting import report_1, report_2, report_3, report_4, report_5, report_6
from crud import delete_row, add_order, add_item_write_to_db, replace_item_write_to_db, replace_order_options_in_db, update_item_write_to_db
from util import app_header, exit_app


# Main contents menu - initialised from starting app
def start_app():
    while True:
        
        
        contents = input(
            """
        1: Product Menu... 
        2: Courier Screen...
        3: Order Menu....
        4: Reporting Screen...
        0: Exit App...

        Please enter your choice:
        """
        )
        if contents == "1":
            app_header("Product Main Menu")
            menu("Product","price", "products")

        elif contents == "2":
            app_header("Courier Main Menu")
            menu("Courier", "number", "couriers")

        elif contents == "3":
            app_header("Order Main Menu")
            menu("Order", "Status", "orders")

        elif contents == "4":
            reporting_menu()

        elif contents == "0":
            exit_app()

        else:
            app_header("Main Screen")
            print("You made an incorrect selection, please try again... \n")

# Generic sub menu for products, couriers and orders 
def menu(what, val, table):
    while True: 
        connection = connect_to_db()
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
            app_header("Main Screen")
            start_app()

        elif start_option == "1":
            print_from_db_menu(table)
            return_option(connection, what, val, table)

        elif start_option == "2":
            add_item_to_db(connection, what, val, table)
            return_option(connection, what, val, table)

        elif start_option == "3":
            update_item_sub_menu(what, val, table)

        elif start_option == "4":
            replace_item_in_db(connection, what, val, table)
            app_header(what)
            menu(what, val, table)

        elif start_option == "5":
            delete_row(connection, what, val, table)
            return_option(connection, what, val, table)

        elif start_option == "6":
            exit_app()

        else:
            app_header(f"{what} Screen")
            print("You made an incorrect selection, please try again... \n")

        connection.close


# Menu screen for reporting section 
def reporting_menu():
    while True: 
        app_header("Reports Screen")
        reporting_option = input(
            """ Please select a report: 
            
        0)   Return to the main menu...
        1)   Details for a specific order...
        2)   Orders not yet delivered...
        3)   Delivered orders...
        4)   Cancelled orders...
        5)   Graphical representation of Order Status... 
        6)   Deliveries per courier...
        """
        )
        if reporting_option == "0":
            app_header("Main Screen")
            start_app()
        elif reporting_option == "1":
            report_1('orders')
            reports_return_option()
        elif reporting_option == "2":
            report_2()
            reports_return_option()
        elif reporting_option == "3":
            report_3()
            reports_return_option()
        elif reporting_option == "4":
            report_4()
            reports_return_option()
        elif reporting_option == "5":
            report_5()
            reports_return_option()
        elif reporting_option == "6":
            report_6()
            reports_return_option()
        else:
            app_header("Reports Screen")
            print("You made an incorrect selection, please try again... \n \n Please press 0 to return to the main menu...\n")

# CRUD MENUS

# CREATE

# Create generic item to database initial menu
def add_item_to_db(connection, what, val, table):
    if table == 'products' or table == 'couriers':
        add_item_sub_menu(what, val, table)
    elif table == 'orders':
        add_order(connection, what, val, table)
        app_header(f"{what} Screen")
        menu(what, val, table)

# Create sub menu for products or couriers
def add_item_sub_menu(what, val, table):
    added_item = input(f'Please enter the name of the {what} you wish to add...\n \nPlease press 0 if you wish to return to the previous menu...')
    if added_item == "0":
        app_header(f"{what} Screen")
        menu(what, val, table)
    else:
        add_item_write_to_db(what, val, table, added_item)
        app_header(f"{what} Screen")
        menu(what, val, table)


# REPLACE

# Replace item generic initial menu 
def replace_item_in_db(connection, what, val, table):
    if table == 'products' or table == 'couriers':
        replace_item_menu(connection, what, val, table)
    elif table == 'orders':
        replace_order_options_in_db(connection, what, val, table)


# Replace item sub menu
def replace_item_menu(connection, what, val, table):
    print_from_db_menu(table)
    item_to_replace = input(f'Please enter the ID for the {what} you want to replace...\n \nPlease press 0 if you wish to return to the previous menu...')
    if item_to_replace == "0":
        app_header(f"{what} Screen")
        menu(what, val, table)
    else:
        replace_item_write_to_db(connection, what, val, table, item_to_replace)
        app_header(f"{what} Screen")
        menu(what, val, table)


# UPDATE

# Updating an item generic sub menu
def update_item_sub_menu(what, val, table):
    app_header(f'Update {what} {val}')
    print_from_db_menu(table)
    update_item = input(f'Please enter the ID for the {what} you want to update the {val} for...\n \nPlease press 0 if you wish to return to the previous menu...')
    if update_item == "0":
        app_header(f"{what} Screen")
        menu(what, val, table)
    else:
        update_item_write_to_db( what, val, table, update_item)
        app_header(f"{what} Screen")
        menu(what, val, table)


# GENERIC RETURN OPTION FUNCTIONS 

# Generic Return Option 

def return_option(connection, what, val, table):
    print()
    while True:
        rtn_input = input("Would you like to return to the " + what + " screen? Y/N")
        
        if rtn_input.upper() == "Y" or rtn_input.upper() == "YES":
            app_header(what+" Screen")
            menu(what, val, table)
            
        elif rtn_input.upper() == "N" or rtn_input.upper() == "NO":
            exit_app()
            
        else:
            print("You have not choosen a suitable option, please try again...")
            continue

# Reports Return Option

def reports_return_option():
    print()
    while True:
        rtn_input = input("Would you like to return to the reports screen? Y/N")
        
        if rtn_input.upper() == "Y" or rtn_input.upper() == "YES":
            app_header("Reporting Screen")
            reporting_menu()
            
        elif rtn_input.upper() == "N" or rtn_input.upper() == "NO":
            exit_app()
            
        else:
            print("You have not choosen a suitable option, please try again...")
            continue


app_header("Main Screen")
start_app()