import pytest
from src.logic.finance import MoneyTransactions, Category, FinanceManager

# Unit Test for income transaction
def test_create_income_transaction():
    # Arrange and Act
    transaction = MoneyTransactions('Salary', 1000.0, 'Work', 'income')
    # Assert
    assert transaction.title == 'Salary'
    assert transaction.amount == 1000.0
    assert transaction.category == 'Work'
    assert transaction.type == 'income'

# Unit Test for expense transaction
def test_create_expense_transaction():
    # Arrange and Act
    transaction = MoneyTransactions('Groceries', 10.0, 'Food', 'expense')
    # Assert
    assert transaction.title == 'Groceries'
    assert transaction.amount == 10.0
    assert transaction.category == 'Food'
    assert transaction.type == 'expense'

# Unit Test for string representation of data 
def test_transaction_string_representation():
    # Arrange & Act
    transaction = MoneyTransactions('Coffee', 3.5, 'Food', 'expense')
    expected_str = 'Expense: Coffee - $3.5 (Food)'
    #Assert
    assert str(transaction) == expected_str

# Unit Test to confirm that data is not taking duplicate values on categories
def test_add_duplicate_category():
    # Arrange
    manager = FinanceManager()
    # Act
    manager.add_category(Category('Food'))
    manager.add_category(Category('Food'))
    manager.add_category(Category('Food'))
    categories = manager.obtain_categories()
    #Assert
    assert categories == ['Food']
    assert len(categories) == 1

# Unit Test to filter non-existent transaction
def test_filter_nonexistent_transaction_type():
    # Arrange
    manager = FinanceManager()
    manager.add_money_transaction(MoneyTransactions('Salary', 1000.0, 'Work', 'income'))
    # Act
    expense = manager.obtain_money_movements_per_type('expense')
    #Assert
    assert expense == []

# Unit test with negative amount (should be allowed)
def test_transaction_with_negative_amount():
    # Arrange & Act
    transaction = MoneyTransactions('Refund', -50.0, 'Shopping', 'income')
    # Assert
    assert transaction.amount == -50.0
    assert transaction.title == 'Refund'

# Unit Test for empty string category
def test_empty_string_category():
    # Arrange and Act
    category = Category('')
    # Assert
    assert category.name == ''
    assert str(category) == ''

# Unit test to review multiple transactions types
def test_manager_with_multiple_transactions():
    # Arrange
    manager = FinanceManager()
    # Act
    manager.add_money_transaction(MoneyTransactions('Salary', 1000.0, 'Work', 'income'))
    manager.add_money_transaction(MoneyTransactions('Rent', 500.0, 'Housing', 'expense'))
    manager.add_money_transaction(MoneyTransactions('Groceries', 75.0, 'Food', 'expense'))
    manager.add_money_transaction(MoneyTransactions('Bonus', 200.0, 'Work', 'income'))
    # Assert
    assert len(manager.money_transactions) == 4
    incomes = manager.obtain_money_movements_per_type('income')
    expenses = manager.obtain_money_movements_per_type('expense')
    assert len(incomes) == 2
    assert len(expenses) == 2

# Unit Test for transactions with special characters in the the title
def test_transaction_with_special_characters():
    # Arrange & Act
    transaction = MoneyTransactions('Café & Books', 25.50, 'Entertaiment', 'expense')
    # Assert
    assert transaction.title == 'Café & Books'
    assert transaction.amount == 25.50

# Unit Test for Category with spaces 
def test_category_with_spaces():
    # Arrange & Act
    category = Category('Home Utilities')
    #Assert
    assert category.name == 'Home Utilities'