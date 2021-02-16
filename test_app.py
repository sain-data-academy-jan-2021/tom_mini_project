import unittest
from util import open_a_csv_file, save_to_a_csv, list_index

class TestApp(unittest.TestCase):

    def test_open_csv_returns_dict_in_file(self):
        
        # Assemble
        test_list = []
        expected = [{'ID': '1', 'Key': 'Water', 'Value': '0.99'},
                    {'ID': '2', 'Key': 'Pizza', 'Value': '1.75'},
                    {'ID': '3', 'Key': 'Apple Pie', 'Value': '3.25'}]
        
        # Act
        open_a_csv_file("sample_test_data.csv", test_list)
        actual = test_list

        # Assert
        assert expected == actual
        print("Test 1 Passed")
        print("test_open_csv_returns_dict_in_file") 



    def test_dict_to_csv(self):
        
        # Assemble
        test_list = [{'ID': '1', 'Key': 'Water', 'Value': '0.99'},
                    {'ID': '2', 'Key': 'Pizza', 'Value': '1.75'},
                    {'ID': '3', 'Key': 'Apple Pie', 'Value': '3.25'}]
        
        expected = [{'ID': '1', 'Key': 'Water', 'Value': '0.99'},
                    {'ID': '2', 'Key': 'Pizza', 'Value': '1.75'},
                    {'ID': '3', 'Key': 'Apple Pie', 'Value': '3.25'}]
        
        # Act
        test_list2 = []
        save_to_a_csv("sample_test_data2.csv", test_list)
        open_a_csv_file("sample_test_data2.csv", test_list2)
        actual = test_list2

        # Assert
        assert expected == actual
        print("Test 2 Passed")
        print("test_dict_to_csv") 



    def test_list_index(self):

        # Assemble
        test_list = [{'ID': '1', 'Key': 'Water', 'Value': '0.99'},
            {'ID': '2', 'Key': 'Pizza', 'Value': '1.75'},
            {'ID': '3', 'Key': 'Apple Pie', 'Value': '3.25'}]
        expected = ['1', '2', '3']

        # Act
        actual = list_index(test_list)

        # Assert
        assert expected == actual
        print("Test 3 Passed")
        print("test_list_index") 


if __name__ == '__main__':
    unittest.main()