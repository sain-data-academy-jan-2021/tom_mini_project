import unittest
from unittest.mock import patch, Mock
from crud import add_item_write_to_db
from database import execute_sql_crud, connect_to_db
from util import validate_number

# To run this unit test: python -m unittest test_app

class TestMenuFunctions(unittest.TestCase):
    
    @patch("database.connect_to_db")
    @patch("builtins.input")
    @patch("database.execute_sql_crud")
    def test_add_new_product_to_database(self, mock_execute_sql_crud, mock_input, mock_connect_to_db):
        
        #Assemble
        mock_connect_to_db.return_value = None
        mock_input.side_effect = ["1.50"]
        expected = 'INSERT INTO products (product_name, product_price) VALUES ("hat", 1.50)'
        
        #Act
        add_item_write_to_db("Product", "price", "products", "hat")
        
        #Assert
        print(mock_execute_sql_crud.call_count)
        mock_execute_sql_crud.assert_called_with(None, expected)
        
        
    @patch("database.connect_to_db")
    @patch("util.validate_number")
    @patch("database.execute_sql_crud")
    def test_add_new_courier_to_database(self, mock_execute_sql_crud, mock_validate_number, mock_connect_to_db):
        
        #Assemble
        mock_validate_number.return_value = "12345"
        mock_connect_to_db.return_value = None
        expected = 'INSERT INTO couriers (courier_name, courier_number) VALUES ("Bob", "12345")'
        
        #Act
        add_item_write_to_db("Courier", "number", "couriers", "Bob")
        
        #Assert
        mock_execute_sql_crud.assert_called_with(mock_connect_to_db, expected)

if __name__ == '__main__': 
    unittest.main()

