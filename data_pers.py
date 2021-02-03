import util
import sys
import csv


def data_from_text_file(filename):
    try:
        with open(filename, "r") as fileholder:
            txt = fileholder.read().splitlines()
            return(txt)

    except FileNotFoundError:
        util.clear_terminal()
        util.header("Error")
        print(f'We are sorry however the {filename} file has not been found.')
        sys.exit()
        
    except Exception as e:
        util.clear_terminal()
        util.header("Error")
        print(f'We are sorry however there has been an error, please refer to the following error message: \n {e}.')
        sys.exit()
        
        
def data_to_a_text_file(mylist, file):
    try:
        with open (file, "w") as fileholder:
            for i in mylist:
                fileholder.write(i + "\n")
    except Exception as e:
        util.clear_terminal()
        util.header("Error")
        print(f'We are sorry however there has been an error, please refer to the following error message: \n {e}.')
        sys.exit()
        

courier_list = []
product_list = []

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