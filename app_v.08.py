# v.0.08
import sys
import util
import data_pers
import csv
import pandas

courier_list = []
product_list = []
orders = []


def start_app():
    while True:
        util.header("Main Screen")
        contents = input(
            """
        A: Product Menu... 
        B: Courier Screen...
        C: Order Menu
        D: Exit App...

        Please enter your choice:
        """
        )
        if contents.upper() == "A":
            menu("Products", product_list, "products.csv", "Price")
        elif contents.upper() == "B":
            menu("Couriers", courier_list, "couriers.csv", "Number")
        elif contents.upper() == "C":
            order_menu()
        elif contents.upper() == "D":
            print("You are now exiting Tominoes, have a nice day!")
            sys.exit()
        else:
            util.header("Main Screen")
            print("You must make a selection from A - D")
            print("Please try another selection")
            continue


def menu(what, list, filename, value):
    
    while True:
        util.header(what)
        start_option = input(
            f"""Please select from the following options:

        0)   Return to Main Menu
        1)   Print Out {what} List
        2)   Create {what}
        3)   Update {what}
        4)   Replace {what}
        5)   Delete {what}
        6)   Exit App
                """
        )

        if start_option == "0":
            start_app()
        elif start_option == "1":
            util.print_csv_function(what,filename)
        elif start_option == "2":
            util.create_function(what,filename,list,value)
        elif start_option == "3":
            util.update_function(what,filename,list,value)
        elif start_option == "4":
            util.replace_function(what,filename,list,value)
        elif start_option == "5":
            util.delete_function(what,filename,list)
        elif start_option == "6":
            util.header("Cheerio!")
            print("You are now exiting Tominoes, have a nice day!")
            sys.exit()
        else:
            util.clear_terminal()
            print("You have not choosen the correctly. \nPlease try again.")
            continue


# def print_csv_function(what,filename):
#     util.header(what)
#     with open(filename) as file:
#         reader = csv.reader(file)
#         for row in reader:
#             print(" ".join(row))
#     sys.exit()
            
# # while loop used to return to previous menu or come out of app
# def return_option(what, list, filename):
#     print()
#     while True:
#         rtn_input = input("Would you like to return to the " + what + " screen? Y/N")
#         if rtn_input.upper() == "Y" or rtn_input.upper() == "YES":
#             util.clear_terminal()
#             menu(what, list, filename, value)
#         elif rtn_input.upper() == "N" or rtn_input.upper() == "NO":
#             print("You are now exiting Tominoes, have a nice day!")
#             break
#         else:
#             print("You have not choosen a suitable option, please try again...")
#             continue


def order_menu():
    while True:
        util.clear_terminal()
        util.header("Order Menu")
        order_option = input(
            """Please select from the following options:

    0)   Return to Main Menu
    1)   Print Out Order Screen
    2)   Create New Order
    3)   Update Order Status
    4)   Update Order
    5)   Delete Order
    6)   Exit App
            """
        )

        if order_option == "0":
            start_app()
        elif order_option == "1":
            util.print_csv_function("Order Menu","orders.csv")
        elif order_option == "2":
            create_order()
        elif order_option == "3":
            update_order_status()
        elif order_option == "4":
            update_order()
        elif order_option == "5":
            delete_order()
        elif order_option == "6":
            util.header("Cheerio!")
            print("You are now exiting Tominoes, have a nice day!")
            sys.exit()
        else:
            util.header("Order Screen")
            print("You have not choosen the correctly. \nPlease try again.")
            continue


def create_order():
    util.header("Order Menu")
    order_id = input("Please enter the order ID...")
    cust_name = input("Please enter the customer's name...")
    cust_address = input("Please enter the customer's address...")
    cust_num = input("Please enter the customer's number...")
    util.header("Product Menu")
    # Prints out list of products to choose from
    util.print_csv_function("Products","products.csv")
    cust_order = input("What would the customer like to order?")
    # Status automatically defaults to preparing
    status = "Preparing"
    util.print_csv_function("Couriers","couriers.csv")
    courier = input("Please enter a courier you want to assign to the order...")
    # Function to add new order to orders csv file - using append to add to end of file
    # file -> variable that data is being parsed to
    # with open suffice opens, appends and closes file
    with open("orders.csv", mode="a") as file:
        # Defines column names
        content_header = [
            "Order_ID",
            "Name",
            "Customer_Address",
            "Customer_Number",
            "Courier",
            "Status",
            "Order",
        ]
        writer = csv.DictWriter(file, fieldnames=content_header)
        # Writes inputted info to sections
        writer.writerow(
            {
                "Order_ID": order_id,
                "Name": cust_name,
                "Customer_Address": cust_address,
                "Customer_Number": cust_num,
                "Courier": courier,
                "Status": status,
                "Order": cust_order,
            }
        )
    print()
    print(
        f"{cust_name}'s, order of {cust_order} is {status} and will be delivered by {courier} to {cust_address}.\nIn case of any difficulties, please phone the customer on {cust_num}. "
    )
    order_return_option(input)


# If you delete more than one order, it produces infinite writing loop in file!
# PLEASE FIX!!!!
def delete_order():
    util.header("Delete Order Menu")
    print_csv_function("Orders", "orders.csv")
    delete_order_number = input("Please enter the order number you wish to delete...").capitalize()
    with open("orders.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            orders.append(row)
            for line in row:
                if line == delete_order_number:
                    orders.remove(row)
                with open("orders.csv", "w") as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(orders)
    util.clear_terminal()
    util.header("Updated Order Menu")
    order_menu()


# Update order and Update status, if re entering function without leaving repeats the order menu
# It does not save and close the list, instead adds to it!
# This needs to be fixed!!!!
def update_order():
    util.header("Update Order Menu")
    edit_status_input = input(
        "Please enter the order ID for the status change..."
    ).capitalize()
    file = open("orders.csv", "r")  # file is assigned variable
    reader = csv.reader(file)  # csv reader allows us to go through one row at a time
    found = False
    for cell in reader:
        if cell[0] == edit_status_input:
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
            if update_number == "":
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
    if found == 0:
        print("Order Not Found")
        file.close
        order_return_option(input)
    else:
        file = open("orders.csv", "w", newline="")
        csvr = csv.writer(file)
        csvr.writerows(orders)
        file.close()
    util.clear_terminal()
    order_menu()


def update_order_status():
    util.header("Update Order Status")
    edit_status_input = input(
        "Please enter the order ID for the status change..."
    ).capitalize()
    file = open("orders.csv", "r")  # file is assigned variable
    reader = csv.reader(file)  # csv reader allows us to go through one row at a time
    found = False
    for cell in reader:
        if cell[0] == edit_status_input:
            cell[5] = input("Enter updated status...")
            found = True
        orders.append(cell)
    if found == 0:
        print("Order Not Found")
        file.close
        order_return_option(input)
    else:
        file = open("orders.csv", "w", newline="")
        csvr = csv.writer(file)
        csvr.writerows(orders)
        file.close()
    order_menu()


def order_return_option(input):
    print()
    while True:
        rtn_input = input("Would you like to return to the order menu screen? Y/N")
        if rtn_input.upper() == "Y" or rtn_input.upper() == "YES":
            util.clear_terminal()
            return order_menu()
        elif rtn_input.upper() == "N" or rtn_input.upper() == "NO":
            print("You are now exiting Tominoes, have a nice day!")
            sys.exit()
        else:
            print("You have not choosen a suitable option, please try again...")
            continue

#print_csv_function("Producrts", "products.csv")
start_app()
