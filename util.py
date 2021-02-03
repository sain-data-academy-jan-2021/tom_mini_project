import os 
import csv
import pandas
import sys

courier_list = []
product_list = []


    
def price_list(dict):
    for x, y in dict.items():
        print(x,' £',y)
        
def clear_terminal():
    os.system('clear')

def header(title):
    clear_terminal()
    # Variable to import for main menu graphical setup
    title = '+ Welcome to Tominoes Pizza Cafe +'
    # Prints a - character the length of the title
    print('|',('-'*len(title)),'|')
    print('|',(title),'|')
    print('|',('-'*len(title)),'|')    
    print()
    print('-'*len(title))
    print(title)    
    print('-'*len(title))
    print()


        


def open_a_csv_file(filename,list):
    with open(filename) as file:
        csv_file = csv.DictReader(file) 
        for row in csv_file:
            list.append(row)
            
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
