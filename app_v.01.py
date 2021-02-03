#v.0.16
# Imports function to exit app
import sys
import util
import csv
import pandas
import data_pers

####################################

# Fuction for inital contents screen
def start_app():
    util.app_header() 
    print()       
    contents_title = 'Main Screen'
    print('-'*len(contents_title))
    print(contents_title)
    print('-'*len(contents_title))
    print()
    # Menu that allows user to decide which layer to next move to
    contents = input('''
    A: Product Menu... 
    B: Courier Screen...
    C: Order Menu
    D: Exit App...
    
    Please enter your choice:
    ''') 
    
    if contents.upper() == 'A':
    #Each if/elif statement returns a def function to be used later in app
        util.clear_terminal()
        food_beverage()
    elif contents.upper() == 'B':
        util.clear_terminal()
        courier_start()
    elif contents.upper() == 'C':
        util.clear_terminal()
        order_menu()        
    elif contents.upper() == 'D':
        print('You are now exiting Tominoes, have a nice day!')
        # Exits program
        sys.exit()# producing inifite loop
    else:
        print('You must make a selection from A - D')
        print('Please try another selection')
        # Returns to original menu list
        # start_app()

####################################

# Initial Dictionaries of  dishes
starter_dict = {'Garlic Bread':2.99, 'Nachos':3.49, 'Wedges':2.49, 'Chicken Wings':3.99} 
main_dict = {'Pepperoni':2.99, 'Meat Feast':3.49}
dessert_dict = {'Icecream': 2.99, 'Sorbet':2.49}
drink_dict = {'Coke' : 0.99, 'Malbec' : 4.99}

###################################

# Function to print out price list including headers 
def print_list_main(app_sub_variable, dict):
    util.clear_terminal()
    util.app_header()
    title = app_sub_variable
    print()
    print('-'*len(title))
    print(title)    
    print('-'*len(title))
    print()
    # Prints list in veritcal order
    util.price_list(dict)
    print()
    # Returns to starter sub screen
    continue_or_quit(app_sub_variable, dict)        
    
###################################

# Asks a user if they want to return up a menu 

def continue_or_quit(app_sub_variable, dict): 
    while True:
        exit = input('Would you like to continue? (Y/N)')
        if exit.upper() == 'Y':
            util.clear_terminal()
            sub_screen(app_sub_variable, dict)

        elif exit.upper() == 'N':
            print('Have a nice day!')
            remove_item
            sys.exit()
        else: 
            print('You did not enter Y/N, please try again.')
            sub_screen(app_sub_variable, dict)

###################################

# Function Products Contents Screen   
def sub_screen(app_sub_variable, dict): 
    util.app_header()  
    title = f'{app_sub_variable} Menu'
    print()
    print('-'*len(title))
    print(title)    
    print('-'*len(title))
    print()

    sub_screen_input = input('''
        A: View Menu...
        B: Add item to Menu...
        C: Delete item in menu...
        D: Update item in menu...
        E: Update price of item in the menu...
        F: Return to Main Screen...
        ''')
    
    if sub_screen_input.upper() == 'A':
        view_menu(app_sub_variable, dict)
    elif sub_screen_input.upper() == 'B':
        add_item(app_sub_variable, dict)
    elif sub_screen_input.upper() == 'C':
        remove_item(app_sub_variable, dict)
    elif sub_screen_input.upper() == 'D':
        update_item(app_sub_variable, dict)
    elif sub_screen_input.upper() == 'E':
        update_price(app_sub_variable, dict)
    elif sub_screen_input.upper() == 'F':
        print('You are now returning to the main screen.')
        util.clear_terminal()
        food_beverage()   
    else:
        util.clear_terminal()
        print('You must make a selection from A - F')
        print('Please try another selection')
        print()
        sub_screen(app_sub_variable, dict)
        
###################################

# Food Beverage Contents Screen
def food_beverage():
    util.app_header()  
    title = 'Food and Beverage Menu'
    print()
    print('-'*len(title))
    print(title)    
    print('-'*len(title))
    print()

    food_beverage_input = input('''
        A: Starter...
        B: Mains...
        C: Desserts...
        D: Drinks...
        E: Return to Main Screen...
        ''')

    if food_beverage_input.upper() == 'A':
        util.clear_terminal()
        sub_screen('Starter', starter_dict)
    elif food_beverage_input.upper() == 'B':
        util.clear_terminal()
        sub_screen('Main', main_dict)
    elif food_beverage_input.upper() == 'C':
        sub_screen('Dessert', dessert_dict)
    elif food_beverage_input.upper() == 'D':
        sub_screen('Drinks', drink_dict)
    elif food_beverage_input.upper() == 'E':
        print('You are now returning to the main screen.')
        util.clear_terminal()
        start_app()   
    else:
        util.clear_terminal()
        print('You must make a selection from A - E')
        print('Please try another selection')
        print()
        food_beverage()
        
###################################

# View menu option for products 
def view_menu(app_sub_variable, dict):
        util.clear_terminal()
        util.app_header()
        title = (f'{app_sub_variable} Menu')
        print()
        print('-'*len(title))
        print(title)    
        print('-'*len(title))
        print()
        # Prints list in veritcal order
        util.price_list(dict)
        print()
        # Returns to product sub screen
        continue_or_quit('Product', dict)
        
###################################

# User Input Error
def invalid_input(function_menu):
    util.clear_terminal()
    util.app_header()
    print('You made an incorrect input')
    print('Please try another selection')
    function_menu()
    
###################################

# Function to add dish for products 
def add_item(app_sub_variable, dict):
    util.clear_terminal()
    # Requests input to add to product menu list
    util.app_header()
    print()
    add_item = input(f'Please add a {app_sub_variable} to the menu...').capitalize()
    add_item_price = input('Please enter a price...')
    # Adds inputted product to product menu
    if not add_item in dict:
        dict[add_item]=add_item_price
        print(f'You have inserted {add_item},to the {app_sub_variable} menu.')
        print()
        print(f'Updated {app_sub_variable} menu:')
        print('-'*len('Updated {app_sub_variable} menu:'))
        util.price_list(dict)
        continue_or_quit(app_sub_variable, dict)
        
    else: 
        print(add_item,'is already on the menu.')
        add_item_again = input('Would you like to try again? Y/N')
        if add_item_again.upper() == 'Y':
            print('Please try again...')
            sub_screen(app_sub_variable, dict)
        else:
            util.clear_terminal()    
            sub_screen(app_sub_variable, dict) 
    sub_screen(app_sub_variable, dict)

###################################

# Function to remove dish in dictionary
def remove_item(app_sub_variable, dict):
    util.clear_terminal()
    util.app_header()
    print()
    print('Below is the current list of dishes\nYou will need to choose which item you want to delete from the menu:')
    print('-'*len('You will need to choose which item you want to delete from the menu:'))
    util.price_list(dict)
    print()
    product_delete_menu = input('''
        A: Delete item in menu...
        B: Exit a return to previous menu...
        ''')
    if product_delete_menu.upper() == 'A':
        remove_product = input('Which item would you like to remove?').capitalize()            
        try:
            dict.pop(remove_product)
            print_list_main(app_sub_variable, dict)
            sub_screen(app_sub_variable, dict)
            
        except:
            util.clear_terminal()
            print('We have not found an item to delete.')
            sub_screen(app_sub_variable, dict)
            
    elif product_delete_menu.upper() == 'B':
        util.clear_terminal()
        print('You have decided to return to the previous screen.')
        print()
        sub_screen(app_sub_variable, dict) 
    else:
        util.clear_terminal()
        print('You did not make a selection from the list. ')
        sub_screen(app_sub_variable, dict) 

###################################

# Function to update an item in the product dictionary 
def update_item(app_sub_variable, dict):    
    util.clear_terminal()
    util.app_header()
    print()
    print(f'Below is the current list of {app_sub_variable} dishes\nYou will need to choose which item you want to replace from the menu:')
    print('-'*len('You will need to choose which item you want to replace from the menu:'))
    util.price_list(dict)
    print()
    product_replace_menu = input('''
        A: Replace item in menu...
        B: Exit a return to previous menu...
        ''')
    if product_replace_menu.upper() == 'A':
        replace_product = (input('Which item would you like to update?')).capitalize()
        if replace_product in dict:
            replaced_product = (input('What would you like to replace it with?')).capitalize()
            replaced_product_price = input('How much is the new dish?')
            del dict[replace_product]
            dict[replaced_product]=replaced_product_price
            util.clear_terminal()
            util.app_header()
            print()
            print('You have decided to remove', replace_product, 'from the menu and replace it with',replaced_product,'.')
            print()
            print(f'Updated {app_sub_variable} menu:')
            print('-'*len('Updated Product menu:'))
            util.price_list(dict)
            print()
            continue_or_quit(app_sub_variable, dict)
        else:
            util.clear_terminal()
            print(replace_product, 'Item not found')
            sub_screen(app_sub_variable, dict) 
    elif product_replace_menu.upper() == 'B':
        print('You have decided to return to the product screen.')
        print()
        sub_screen(app_sub_variable, dict) 
    else:
        print('You did not make a selection from the list. ')
        sub_screen(app_sub_variable, dict) 

###################################

# Function to update a price in the product dictionary
def update_price(app_sub_variable, dict):
    util.clear_terminal()
    util.app_header()
    print()
    print(f'Below is the current list of {app_sub_variable} dishes\nYou will need to choose which item you want to update the price for:')
    print('-'*len('Below is the current list of product dishes\nYou will need to choose which item you want t   update the price for:'))
    util.price_list(dict)
    print()
    product_price_update = input('''
        A: Update price in menu...
        B: Exit a return to previous menu...
        ''')
    if product_price_update.upper() == 'A':
        update_price = (input('Which menu item would you like to update the price for?')).capitalize()
        if update_price in dict:
            updated_price = (input('Please enter the new price...'))
            dict[update_price] = updated_price
            util.clear_terminal()
            util.app_header()
            print(f'You have updated the price of {update_price}to £ {updated_price}.')
            print()
            print(f'Updated {app_sub_variable} menu:')
            print('-'*len(f'Updated {app_sub_variable} menu:'))
            util.price_list(dict)
            continue_or_quit(app_sub_variable, dict)

        else:
            util.clear_terminal()
            print('Product not found')
            sub_screen(app_sub_variable, dict)

    elif product_price_update.upper() == 'B':
        print(f'You have decided to return to the {app_sub_variable} screen.')
        print()
        sub_screen(app_sub_variable, dict) 
    else:
        util.clear_terminal()
        print('You did not make a selection from the list. ')
        sub_screen(app_sub_variable, dict)         
        
####################################
####################################
####################################

# Couriers Section of the App 

####################################

couriers = data_pers.data_from_text_file('couriers.txt')
util.clear_terminal()
#products = data_pers.data_from_text_file('products.txt')

####################################

# Initial Courier section of app
def courier_start():
    header('Courier')
    start_option = input('''Please select from the following options:

0)   Return to Main Menu
1)   Print Out Courier List
2)   Create New Courier
3)   Update Courier
4)   Delete Courier
5)   Exit App
        ''')

    if start_option =='0':
        util.clear_terminal()
        start_app()
    elif start_option =='1':
        listing_function()
    elif start_option =='2':
        create('Courier', 'couriers.txt')
    elif start_option =='3':
        update_courier()
    elif start_option =='4':
        delete_courier()
    elif start_option =='5':
        sys.exit()
    else:
        util.clear_terminal()
        print('You have not choosen the correctly. \nPlease try again.')
        courier_start()    

####################################
# Courier header
def header(title):
    util.app_header()  
    print()
    print('-'*len(title))
    print(title)    
    print('-'*len(title))
    print()
    
####################################

# Listing function in courier section 
def listing_function():
    util.clear_terminal()
    header('Courier List')
    for people in couriers:
        print(people)
    previous_courier_option()

####################################

# Add courier section 

def create(section, filepath):
    util.clear_terminal()
    added = input(f'Please enter the your {section}...').capitalize()
    if added not in couriers:
        couriers.append(added)
        print(f'You have added {added} to the {section} list.')
        data_pers.data_to_a_text_file(couriers, 'couriers.txt')
        previous_courier_option()
    else:
        print(f'{added} is already in the system.')
        previous_courier_option()
        
####################################

# Delete courier section
def delete_courier():
    deletecourier = input('Which courier would you like to remove?').capitalize()
    if deletecourier not in couriers:
        print('You have entered an incorect name\n Please try again...')
        delete_courier()
    elif deletecourier in couriers:
        couriers.remove(deletecourier)
        data_pers.data_to_a_text_file(couriers, 'couriers.txt')
        print(deletecourier, 'has been deleted from the courier list.')
        listing_function()
        previous_courier_option()
    else:
        print('You have not choosen correctly, please try again...')
        
        
####################################

# Function to return to courier menu
def previous_courier_option():
    pco = input('\nDo you wish to return to the previous menu?').lower()
    if pco == 'y' or pco == 'yes':
        util.clear_terminal()
        courier_start()
    elif pco == 'n' or pco =='no':
        print('Have a nice day!')
        sys.exit()
    else:
        util.clear_terminal()
        util.app_header()
        print()
        print('You have not choosen a valid input, please try again...')

        
####################################

# Update courier function - not currently working
def update_courier():
    update_courier = input('Which courier would you like to update?').capitalize()
    if update_courier in couriers:
        updated_courier = input(f'Which courier would you like to replace {update_courier}?').capitalize()
        couriers.remove(update_courier)
        couriers.append(updated_courier)
        print(f'\nYou have replaced {update_courier} with {updated_courier}.')
        data_pers.data_to_a_text_file(couriers, 'couriers.txt')
        previous_courier_option()
    else:
        print('You choose a courier who is not currently in the system.\n Please try again...')
        previous_courier_option()
####################################

# ORDER SECTION

def order_menu():
    header("Order Menu")
    order_option = input('''Please select from the following options:

0)   Return to Main Menu
1)   Print Out Order Screen
2)   Create New Order
3)   Update Order Status
4)   Update Order - Stretch Goal
5)   Delete Order - Stretch Goal
6)   Exit App
        ''')

    if order_option =='0':
        util.clear_terminal()
    elif order_option =='1':
        util.clear_terminal()
        print_order()
    elif order_option =='2':
        util.clear_terminal()
        create_order()
    elif order_option =='3':
        util.clear_terminal()
        update_order()
    elif order_option =='4':
        util.clear_terminal()
        print('Stretch Goal')
    elif order_option =='5':
        util.clear_terminal()
        delete_order()
    elif order_option =='6':
        util.clear_terminal()
        sys.exit()
    else:
        util.clear_terminal()
        print('You have not choosen the correctly. \nPlease try again.')
        order_menu()  

####################################

def print_order():
    header("Order Menu")
    df = pandas.read_csv('orders.csv')
    print(df)    
    return_option('Order Menu')
    #csv_to_dic("orders.csv")
    

def return_option(rtn_opt):
    print()
    while True:
        rtn_input = input('Would you like to return to the ' + rtn_opt + ' screen? Y/N')
        if rtn_input.upper() == 'Y' or rtn_input.upper() == 'YES':
            util.clear_terminal()
            order_menu()
        elif rtn_input.upper() == 'N' or rtn_input.upper() == 'NO':
            print('You are now exiting Tominoes, have a nice day!')
            break               
        else:
            print('You have not choosen a suitable option, please try again...')
            continue
            

####################################

def create_order():
    header("Order Menu")
    cust_name = input("Please enter the customer's name...")
    cust_address = input("Please enter the customer's address...")
    cust_num = input("Please enter the customer's number...")
    util.clear_terminal()
    header("Product Menu")
    util.price_list(starter_dict)
    util.price_list(main_dict)
    util.price_list(dessert_dict)
    util.price_list(drink_dict)


    cust_order = input("What would the customer like to order?")
    status = "Preparing"
    courier = "T.B.C."
    
    with open('orders.csv', mode='a') as file:
        content_header = ['Name', 'Customer_Address', 'Customer_Number', 'Courier', 'Status', 'Order'] 
        writer = csv.DictWriter(file, fieldnames=content_header)

        writer.writerow({
            "Name": cust_name,
            "Customer_Address": cust_address,
            "Customer_Number": cust_num,
            "Courier": courier,
            "Status": status,
            "Order": cust_order 

        })
        
    print(f"{cust_name}'s, order of {cust_order} is {status} and will be delivered by {courier} to {cust_address}.\nIn case of any difficulties, please phone the customer on {cust_num}. ")
    return_option('Order Menu')

####################################

def update_order():
    header("Update Order Menu")
    df = pandas.read_csv('orders.csv')
    print(df) 

####################################

def delete_order():
    header("Delete Order Menu")
    df = pandas.read_csv('orders.csv')
    print(df) 
    
####################################


# def csv_to_dic(filename): 
#     with open(filename, 'r') as file:
#         csv_file = csv.DictReader(file) 
#         for row in csv_file:
#             print(row)
    
####################################


# Name,Customer_Address,Customer_Number,Courier,Status,Order
# "Peter Rabbit","12 The Burrow",0123456,"xxx", "yyy","zzz"
# "George Foreman","18 The Grill",345678,"xxx", "yyy","zzz"
# "Harry Potter","4 Privet Drive",123845,"xxx", "yyy","zzz"


    


# Command to run app

start_app()
