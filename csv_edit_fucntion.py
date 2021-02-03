import csv

orders_list = []
edit_status_input = input("Please enter the order ID for the status change...").capitalize()
file = open("orders.copy.csv", "r")  # file is assigned variable
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
    orders_list.append(cell)
if found ==0:
    print("Order Not Found")
    file.closeT0
else:
    file = open("orders.copy.csv", "w",newline= "")
    csvr = csv.writer(file)
    csvr.writerows(orders_list)
    file.close()