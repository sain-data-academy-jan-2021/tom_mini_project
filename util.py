import os 
import sys

# Generic Title Header function 

def app_header(sub_title):
    
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


# Clear Terminal Function

def clear_terminal():
    os.system('clear')
    
# Validates an inputted phone number

def validate_number(who):
    while True:
        added_number = input(f'Please enter the phone number of the {who}...')
        if len(added_number) == 11:
            return added_number
        else:
            print('You have not entered a recognised phone number, please try again...')
            


def exit_app():
    app_header("Cheerio!")
    print("You are now exiting Tominoes, have a nice day!")
    print()
    sys.exit()