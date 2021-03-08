import unittest
from unittest.mock import patch, Mock
from crud import add_item_write_to_db, choose_order_status
from database import *
from util import validate_number

# python3 -m unittest test_app

class TestMenuFunctions(unittest.TestCase):
    
    @patch("database.connect_to_db")
    @patch("builtins.input")
    @patch("database.execute_sql_crud")
    def test_add_new_product_to_database(self, mock_execute_sql_crud, mock_input, mock_connect_to_db):
        
        #Assemble
        mock_connect_to_db.return_value = None
        mock_input.side_effect = ["1.50"]
        expected = 'INSERT INTO products (product_name, product_price) VALUES ("hat", 1.5)'
        
        #Act
        add_item_write_to_db("Product", "price", "products", "hat")
        
        #Assert
        print(mock_execute_sql_crud.call_count)
        mock_execute_sql_crud.assert_called_with(None, expected)



    # ADDS THE MOCK COURIER BOB TO THE COURIER DATABASE
    
    
    # @patch("database.connect_to_db")
    # @patch("util.validate_number")
    # @patch("database.execute_sql_crud")
    # def test_add_new_courier_to_database(self, mock_execute_sql_crud, mock_validate_number, mock_connect_to_db):
        
    #     #Assemble
    #     mock_validate_number.return_value = "12312312312"
    #     mock_connect_to_db.return_value = None
    #     expected = 'INSERT INTO couriers (courier_name, courier_number) VALUES ("Bob", "12312312312")'
        
    #     #Act
    #     add_item_write_to_db("Courier", "number", "couriers", "Bob")
        
    #     #Assert
    #     mock_execute_sql_crud.assert_called_with(None, expected)


    # RUNS THE APP RATHER THAN COMPLETING THE TEST


    # @patch("builtins.input")
    # @patch("util.app_header")
    # @patch("app.menu")
    # def test_start_app_menu(self, mock_menu, mock_app_header, mock_input):

    #     # Assemble
    #     mock_input.return_value = "1"
    #     expected_header = "Product Main Menu" # using is called with rather than returning whole value 
    #     expected_menu = ["Product","price", "products"]

    #     # Act
    #     start_app()

    #     # Assert
    #     mock_app_header.assert_called_with(expected_header)
    #     mock_menu.assert_called_with(expected_menu)
    
    
    @patch("builtins.input")
    def test_choose_order_status_1(self, mock_input):

        # Assemble
        mock_input.side_effect = ["1"] # side effect used for multiple inputs one input -> mock_input.return_value = "1"
        expected = "Order Received"
        # Act
        actual = choose_order_status()
        # Assert
        assert expected == actual

    @patch("builtins.input")
    def test_choose_order_status_2(self, mock_input):
        mock_input.side_effect = ["2"] # side effect used for multiple inputs one input -> mock_input.return_value = "1"
        expected = "Order Preparing"
        actual = choose_order_status()
        assert expected == actual
        

    @patch("builtins.input")
    def test_choose_order_status_3(self, mock_input):
        mock_input.side_effect = ["3"] # side effect used for multiple inputs one input -> mock_input.return_value = "1"
        expected = "Order Delivered"
        actual = choose_order_status()
        assert expected == actual
        
    @patch("builtins.input")
    def test_choose_order_status_4(self, mock_input):
        mock_input.side_effect = ["4"] # side effect used for multiple inputs one input -> mock_input.return_value = "1"
        expected = "Order Cancelled"
        actual = choose_order_status()
        assert expected == actual

if __name__ == '__main__': 
    unittest.main()

