import unittest
import app

class TestApp(unittest.TestCase):
    # def test_create_item_in_list(self):
        
    #     # Assemble
    #     new_item = "Pepsi"
    #     filepath = "products.txt"
    #     products = ["Orange","Kiwi","Apple","Melon"]
    #     expected = ["Orange","Kiwi","Apple","Melon","Pepsi"]

    #     # Act
    #     actual = create("Products",products,filepath,new_item)
    #     print(actual)
        
    #     # Assert
    #     assert expected == actual
    #     print("Test 1 (Create) Passed")

    def test_view_a_list(self):
        # Assemble
        products = ["Orange","Kiwi","Apple","Melon"]

        # Act
        actual = app.view_function("Products", products, "products.txt")
        print(actual)
        expected = ["Orange","Kiwi","Apple","Melon"]
        
        # Assert
        assert expected == actual



    # def view_function(what, list, filename):
    #     util.clear_terminal()
    #     util.header(what)
    #     for item in list:
    #         print(item)
    #     return_option(what, list, filename)

# def order_return_option():
#     print()
#     while True:
#         rtn_input = input('Would you like to return to the order menu screen? Y/N')
#         if rtn_input.upper() == 'Y' or rtn_input.upper() == 'YES':
#             util.clear_terminal()
#             order_menu()
#         elif rtn_input.upper() == 'N' or rtn_input.upper() == 'NO':
#             print('You are now exiting Tominoes, have a nice day!')
#             sys.exit()               
#         else:
#             print('You have not choosen a suitable option, please try again...')
#             continue

    # def test_order_return_option(self):
    # # Assemble
    #     user_input = "Y"
    #     expected = app.order_menu()
    
    # # Act
    #     actual = app.order_return_option(user_input)
    #     print(actual)
    
    # # Assert
    #     assert expected == actual
    #     print("Test 2 (Order Return Option) Passed")
    
        
if __name__ == '__main__':
    unittest.main()