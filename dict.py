import csv
import sys
from data_pers import open_a_csv_file, save_to_a_csv

courier_list = []
product_list = []

def create_function(what,filename,list,value):
    open_a_csv_file(filename,list)
    id = input(f"Please enter a new {what} ID.")
    new_key = input(f"Please enter a new {what} name.")
    new_value = input(f"Please enter a new {value} for {new_key}.")
    new_dict = dict(ID = id, Key = new_key, Value = new_value)
    list.append(new_dict)
    save_to_a_csv(filename,list)
    

def delete_function(what,filename,list):
    open_a_csv_file(filename,list)
    item_to_delete = input(f'Please enter the number for the {what} you wish to delete. ')
    for item in list:
        if item["ID"] == item_to_delete:
            list.remove(item)
    save_to_a_csv(filename,list)

def replace_function(what,filename,list,value):
    open_a_csv_file(filename,list)
    item_to_replace = input(f'Please enter the ID of the {what} you wish to replace...')
    for item in list:
        if item["ID"] == item_to_replace:
            list.remove(item)
            new_key = input(f"Please enter a new {what} name.")
            new_value = input(f"Please enter a new {value} for {new_key}.")
            new_dict = dict(ID = item_to_replace, Key = new_key, Value = new_value)
            list.append(new_dict)
            save_to_a_csv(filename,list) 
            break
        
def update_function(what,filename,list,value):
    open_a_csv_file(filename,list)
    item_to_replace = input(f'Please enter the ID of the {what} you wish to replace...')
    for item in list:
        if item["ID"] == item_to_replace:
            item["Key"] == item["Key"]
            item["Value"] = input("Enter updated status...")
            new_dict = dict(ID = item_to_replace, Key = item["Key"], Value = item["Value"])
            list.remove(item)
            list.append(new_dict)
            save_to_a_csv(filename,list) 
            break
            
def save_to_a_csv(filename,list):
    csv_columns = ["ID","Key","Value"]
    with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in list:
                writer.writerow(data)


#create_function("Courier", "couriers.copy.csv", courier_list, "Phone Number")
#create_function("Product", "products.copy.csv", product_list, "Price")

#delete_function("Courier", "couriers.copy.csv", courier_list) 
#delete_function("Product", "products.copy.csv", product_list) 

#replace_function("Courier", "couriers.copy.csv", courier_list, "Phone Number")
#replace_function("Product", "products.copy.csv", product_list, "Price")

#update_function("Courier", "couriers.copy.csv", courier_list, "Phone Number")
#update_function("Product", "products.copy.csv", product_list, "Price")


