#v.0.05
import sys
import util
import data_pers
import csv
import pandas

# Products list as variable from products txt file
products = data_pers.data_from_text_file('products.txt')

# Courier list as variable from products txt file
couriers = data_pers.data_from_text_file('couriers.txt')

# Orders list used in create/delete function - check and update
orders = []

def start_app():
    while True:
        util.app_header() 
        print()       
        contents_title = 'Main Screen'
        print('-'*len(contents_title))
        print(contents_title)
        print('-'*len(contents_title))
        print()
        contents = input('''
        A: Product Menu... 
        B: Courier Screen...
        C: Order Menu
        D: Exit App...

        Please enter your choice:
        ''') 
        if contents.upper() == 'A':
            util.clear_terminal()
            # Here we input out WHAT, LIST and FILE which will be used throughout app
            menu("Products",products,"products.txt")
        elif contents.upper() == 'B':
            util.clear_terminal()
            # Couriers input of WHAT, LIST and FILE - arguements that will be passed throughout app
            menu("Couriers",couriers,"couriers.txt")
        elif contents.upper() == 'C':
            util.clear_terminal()
            # Seperate Order menu - not using same arguements as products/couriers atm! 
            order_menu()        
        elif contents.upper() == 'D':
            print('You are now exiting Tominoes, have a nice day!')
            break
        else:
            util.clear_terminal()
            print('You must make a selection from A - D')
            print('Please try another selection')
            continue

def menu(what,list,filename):
        #Argument -> 
        # WHAT -> String for Courier or Products
        # LIST -> lists using txt to list function in data_pers module
        # Filename -> filepath for txt files
    # while True function - means menu will loop forever until another function has been called, or the 
    # while loop has been broken
    while True:   
        util.header(what)
        start_option = input(f'''Please select from the following options:

        0)   Return to Main Menu
        1)   Print Out {what} List
        2)   Create {what}
        3)   Update {what}
        4)   Delete {what}
        5)   Exit App
                ''')
        if start_option =='0':
            util.clear_terminal()
            start_app()
        elif start_option =='1':
            view_function(what,list,filename)
        elif start_option =='2':
            create(what,list,filename)
        elif start_option =='3':
            update(what,list,filename)
        elif start_option =='4':
            delete(what,list,filename) 
        elif start_option =='5':
            print('You are now exiting Tominoes, have a nice day!')
            break
        else:
            util.clear_terminal()
            print('You have not choosen the correctly. \nPlease try again.')
            continue
        
# This function could be moved in to the utilities module
def view_function(what,list,filename):
    util.clear_terminal()
    util.header(what)
    for item in list:
        print(item)
    return_option(what,list,filename)
    
# while loop used to return to previous menu or come out of app    
def return_option(what,list,filename):
    print()
    while True:
        rtn_input = input('Would you like to return to the ' + what + ' screen? Y/N')
        if rtn_input.upper() == 'Y' or rtn_input.upper() == 'YES':
            util.clear_terminal()
            menu(what,list,filename)
        elif rtn_input.upper() == 'N' or rtn_input.upper() == 'NO':
            print('You are now exiting Tominoes, have a nice day!')
            break               
        else:
            print('You have not choosen a suitable option, please try again...')
            continue

def create(what, list, filename):
    util.clear_terminal()
    util.app_header()
    added = input(f'Please enter the your {what}...').capitalize()
    # checks if inputted item is in the list
    if added in list:
        print(f'{added} is already in the system.')
        return_option(what,list,filename)
    else:
        # adds the item to the list using - note, this is added to the list but not saved
        list.append(added)
        print(f'You have added {added} to the {what} list.')
        # This function saves the list to the filename/filepath
        data_pers.data_to_a_text_file(list,filename)
        return_option(what,list,filename)

def delete(what,list,filename):
    deleted = input(f'Which {what} would you like to remove?').capitalize()
    if deleted not in list:
        print('You have entered an incorrect name\n Please try again...')
        delete(what,list,filename)
    elif deleted in list:
        list.remove(deleted)
        data_pers.data_to_a_text_file(list,filename)
        print(deleted, f'has been deleted from the {what} list.')
        view_function(what,list,filename)
        return_option(what,list,filename)
    else:
        print('You have not choosen correctly, please try again...')

def update(what,list,filename):
    update = input(f'Which {what} would you like to update?').capitalize()
    if update in list:
        updated = input(f'Which {what} would you like to replace {update}?').capitalize()
        # Removes old item from list
        list.remove(update)
        # Adds new item to the list
        list.append(updated)
        print(f'\nYou have replaced {update} with {updated}.')
        data_pers.data_to_a_text_file(list, filename)
        return_option(what,list,filename)
    else:
        print(f'You choose a {what} who is not currently in the system.\n Please try again...')
        return_option(what,list,filename)

def order_menu():
    while True:
        util.clear_terminal()
        util.header("Order Menu")
        order_option = input('''Please select from the following options:

    0)   Return to Main Menu
    1)   Print Out Order Screen
    2)   Create New Order
    3)   Update Order Status
    4)   Update Order - Stretch Goal
    5)   Delete Order
    6)   Exit App
            ''')

        if order_option =='0':
            util.clear_terminal()
        elif order_option =='1':
            util.clear_terminal()
            print_order("Order Menu")
        elif order_option =='2':
            util.clear_terminal()
            create_order()
        elif order_option =='3':
            util.clear_terminal()
            update_order_status()
        elif order_option =='4':
            util.clear_terminal()
            update_order()
        elif order_option =='5':
            util.clear_terminal()
            delete_order()
        elif order_option =='6':
            util.clear_terminal()
            print('You are now exiting Tominoes, have a nice day!')
            sys.exit()
        else:
            util.clear_terminal()
            print('You have not choosen the correctly. \nPlease try again.')
            continue 

# This can be moved to the util module
def print_order(what):
    util.header(what)
    # Using pandas module to prettify the order csv fiel
    df = pandas.read_csv('orders.csv', index_col=0)
    print(df)    
    order_return_option()
    
def create_order():
    util.header("Order Menu")
    order_id = input("Please enter the order ID...")
    cust_name = input("Please enter the customer's name...")
    cust_address = input("Please enter the customer's address...")
    cust_num = input("Please enter the customer's number...")
    util.clear_terminal()
    util.header("Product Menu")
    # Prints out list of producst to choose from
    for x in products:
        print(x)
    cust_order = input("What would the customer like to order?")
    # Status automatically defaults to preparing
    status = "Preparing"
    util.clear_terminal()
    util.header("Courier Menu")
    for x in couriers:
        print(x)
    courier = input("Please enter a courier you want to assign to the order...")
    # Function to add new order to orders csv file - using append to add to end of file
    # file -> variable that data is being parsed to
    # with open suffice opens, appends and closes file
    with open('orders.csv', mode='a') as file:
        # Defines column names
        content_header = ['Order_ID', 'Name', 'Customer_Address', 'Customer_Number', 'Courier', 'Status', 'Order'] 
        writer = csv.DictWriter(file, fieldnames=content_header)
        # Writes inputted info to sections
        writer.writerow({
            "Order_ID": order_id,
            "Name": cust_name,
            "Customer_Address": cust_address,
            "Customer_Number": cust_num,
            "Courier": courier,
            "Status": status,
            "Order": cust_order 
        })
    print()
    print(f"{cust_name}'s, order of {cust_order} is {status} and will be delivered by {courier} to {cust_address}.\nIn case of any difficulties, please phone the customer on {cust_num}. ")
    order_return_option()

def delete_order():
    util.clear_terminal()
    util.header("Delete Order Menu")
    df = pandas.read_csv('orders.csv', index_col=0)
    print(df) 
    delete_order_number = input('Please enter the order number you wish to delete...')
    with open('orders.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            orders.append(row)
            for line in row:
                if line == delete_order_number:
                    orders.remove(row)
                with open('orders.csv', 'w') as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(orders)
    util.clear_terminal()
    util.header("Updated Order Menu")
    df = pandas.read_csv('orders.csv', index_col=0)
    print(df)
    order_return_option()
    
    
# Update order and Update status, if re entering function without leaving repeats the order menu
# This needs to be fixed!!!! 
def update_order():
    util.clear_terminal()
    util.header("Delete Order Menu")
    df = pandas.read_csv('orders.csv', index_col=0)
    print(df) 
    edit_status_input = input("Please enter the order ID for the status change...").capitalize()
    file = open("orders.csv", "r")  # file is assigned variable
    reader = csv.reader(file) # csv reader allows us to go through one row at a time
    found = False
    for cell in reader:
        if(cell[0]==edit_status_input):
            update_name = input("Enter updated name...").title()
            if update_name == "":
                pass
            else:
                cell[1] = update_name
            update_address = input("Enter updated address...").title()
            if update_address == "":
                pass
            else:
                cell[2] = update_address
            update_number = input("Enter updated number...").title()
            if update_number== "":
                pass
            else:
                cell[3] = update_number
            update_courier = input("Enter updated courier...").title()
            if update_courier == "":
                pass
            else:
                cell[4] = update_courier
            update_status = input("Enter updated status...").title()
            if update_status == "":
                pass
            else:
                cell[5] = update_status
            update_order = input("Enter updated order...").title()
            if update_order == "":
                pass
            else:
                cell[6] = update_order
            found = True
        orders.append(cell)
    if found ==0:
        print("Order Not Found")
        file.close
        order_return_option()
    else:
        file = open("orders.csv", "w",newline= "")
        csvr = csv.writer(file)
        csvr.writerows(orders)
        file.close()
    util.clear_terminal()
    order_return_option()

def update_order_status():
    util.clear_terminal()
    util.header("Update Order Menu")
    df = pandas.read_csv('orders.csv', index_col=0)
    print(df)
    edit_status_input = input("Please enter the order ID for the status change...").capitalize()
    file = open("orders.csv", "r")  # file is assigned variable
    reader = csv.reader(file) # csv reader allows us to go through one row at a time
    found = False
    for cell in reader:
        if(cell[0]==edit_status_input):
            cell[5] = input("Enter updated status...")
            found = True
        orders.append(cell)
    if found ==0:
        print("Order Not Found")
        file.close
        order_return_option()
    else:
        file = open("orders.csv", "w",newline= "")
        csvr = csv.writer(file)
        csvr.writerows(orders)
        file.close()
    util.clear_terminal()
    order_return_option()

def order_return_option():
    print()
    while True:
        rtn_input = input('Would you like to return to the order menu screen? Y/N')
        if rtn_input.upper() == 'Y' or rtn_input.upper() == 'YES':
            util.clear_terminal()
            order_menu()
        elif rtn_input.upper() == 'N' or rtn_input.upper() == 'NO':
            print('You are now exiting Tominoes, have a nice day!')
            sys.exit()               
        else:
            print('You have not choosen a suitable option, please try again...')
            continue

start_app()
