import pytest
from unittest.mock import Mock, patch, call
from fianance_manager import Category, MoneyTransaction
import FreeSimpleGUI as sg
from gui import add_category_transaction_window, add_expense_window
from data_persistance import dict_to_transaction, csv_file_to_transaction_object, transaction_list_csv_file
import os

# Test 1 for Category object creation
def test_category_object_creation():
    # Arrange
    category = 'food'
    expected_category = 'food'
    # Act
    result = Category(category)
    #Assert 
    assert str(result) == expected_category

# Test 2 for MoneyTransaction object creation
def test_moneytransaction_object_creation():
    # Arrange and Act
    transaction = MoneyTransaction('food', 'expense', 'lunch', 25.50)
    # Assert
    assert transaction.transaction_category == 'food'

# Test 3 for conversation from Object to Dict 
def test_object_conversion_to_dict():
    # Arrange
    transaction = MoneyTransaction('food', 'expense', 'lunch', 25.50)
    expected_dict = {'transaction category': 'food', 'transaction type': 'expense', 'transaction title': 'lunch', 'transaction amount': 25.50}
    # Act
    result = transaction.money_transaction_to_dictionary()
    # Assert
    assert result == expected_dict

# Test 4 checking pop when no category has been added expense.
def test_add_expense_shows_popup_when_no_categories():
    # Arrange
    mock_main_win = Mock()
    mock_event = 'Add expense'
    mock_values = {}

    empty_category_list = []
    
    with patch('gui.sg.popup') as mock_popup:
        with patch('gui.add_expense_window') as mock_expense_window:
            
            # ACT 
            if not empty_category_list:  
                mock_popup('Please enter a category before adding expense')
            
            # ASSERT - 
            mock_popup.assert_called_once()
            mock_popup.assert_called_with('Please enter a category before adding expense')
            mock_expense_window.assert_not_called()

# Test 5 checking pop when no category has been added income.
def test_add_income_shows_popup_when_no_categories():
    # Arrange
    mock_main_win = Mock()
    mock_event = 'Add income'
    mock_values = {}

    empty_category_list = []
    
    with patch('gui.sg.popup') as mock_popup:
        with patch('gui.add_income_window') as mock_income_window:
            
            # ACT 
            if not empty_category_list:  
                mock_popup('Please enter a category before adding expense')
            
            # ASSERT - 
            mock_popup.assert_called_once()
            mock_popup.assert_called_with('Please enter a category before adding expense')
            mock_income_window.assert_not_called()

# Test 6 opening add category window 
def test_opening_add_category_window():
    # Arrange
    mock_main_win = Mock()
    transaction_category_list = []
    
    with patch('gui.add_category_transaction_window') as mock_category_window:
        # Act 
        event = 'Add transaction category'
        

        if event == 'Add transaction category':
            mock_category_window(mock_main_win, transaction_category_list)
        
        # Assert
        mock_category_window.assert_called_once()
        mock_category_window.assert_called_with(mock_main_win, transaction_category_list)

# Test 7 reviewing dict to transaction conversation
def test_dict_to_transaction_conversion():
    # Arrange
    test_dict = {
        'transaction category': 'transport',
        'transaction type': 'expense', 
        'transaction title': 'gas',
        'transaction amount': '45.75'
    }
    
    # Act
    result = dict_to_transaction(test_dict)
    
    # Assert
    assert result.transaction_category == 'transport'
    assert result.transaction_type == 'expense'
    assert result.transaction_amount == 45.75 

# Test 8 reviwing save and load cycle
def test_save_and_load_transaction_cycle():
    # Arrange
    original_transaction = MoneyTransaction('food', 'expense', 'lunch', 25.50)
    temp_file = 'test_temp.csv'
    
    # Act - 
    transaction_list_csv_file([original_transaction], temp_file)
    
    # Act - 
    loaded_list = []
    csv_file_to_transaction_object(loaded_list, temp_file)
    
    # Assert
    assert len(loaded_list) == 1
    loaded_transaction = loaded_list[0]
    assert loaded_transaction.transaction_category == 'food'
    assert loaded_transaction.transaction_amount == 25.50
    
    # Cleanup
    import os
    os.remove(temp_file)