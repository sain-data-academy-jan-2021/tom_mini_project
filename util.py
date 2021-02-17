import os 
import sys
import csv
import pandas

courier_list = []
product_list = []



def clear_terminal():
    os.system('clear')

def header(sub_title):
    
    clear_terminal()
    # Variable to import for main menu graphical setup
    title = '+ Welcome to Tominoes Pizza Cafe +'
    # Prints a - character the length of the title
    print('|',('-'*len(title)),'|')
    print('|',(title),'|')
    print('|',('-'*len(title)),'|')    
    print()
    print('-'*len(sub_title))
    print(sub_title)    
    print('-'*len(sub_title))
    print()

def open_a_csv_file(filename,list):
    
    with open(filename) as file:
        csv_file = csv.DictReader(file) 
        for row in csv_file:
            list.append(row)

def save_to_a_csv(filename,list):
    
    csv_columns = list[0].keys()
    
    with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in list:
                writer.writerow(data)

def save_product_to_a_csv(filename,list):
    
    csv_columns = list[0].keys()
    
    with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in list:
                writer.writerow(data)

def order_to_a_csv(filename,list):
    
    csv_columns = ["ID","Name","Customer_Address","Customer_Number","Courier","Status","Order"]
    
    with open(filename, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
            writer.writeheader()
            for data in list:
                writer.writerow(data)                

def list_index(list):
    
    index_list = []
    for item in list:
        index_list.append(item['ID'])
        
    return index_list

def last_id(table):
    first_key = list(table[0].keys())[0]
    last_id = int((table[-1][first_key]))
    last_id += 1
    return str(last_id)