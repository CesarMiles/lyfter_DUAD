import csv
from fianance_manager import MoneyTransaction

# Function to create CSV File once data is entered
def transaction_list_csv_file(full_transaction_list, file_name='Transaction_data.csv'):
    if not full_transaction_list:
        return
    
    transaction_dict_list = []
    for transaction in full_transaction_list:
        transaction_dict = transaction.money_transaction_to_dictionary()
        transaction_dict_list.append(transaction_dict)

    headers = transaction_dict_list[0].keys()

    with open(file_name, 'w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, headers)
        writer.writeheader()
        writer.writerows(transaction_dict_list)
    
# Function to conver csv rows to objects
def dict_to_transaction(transaction_dict):
    return MoneyTransaction(
        transaction_category = transaction_dict['transaction category'],
        transaction_type = transaction_dict['transaction type'],
        transaction_title = transaction_dict['transaction title'],
        transaction_amount = float(transaction_dict['transaction amount'])
    )

# Function to open CSV file and pull data if previously created and create list of objects
def csv_file_to_transaction_object(full_transaction_list, file_name='Transaction_data.csv'):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            loaded_data = list(reader)

            if not loaded_data:
                return None
            
            for transaction_dict in loaded_data:
                transaction = dict_to_transaction(transaction_dict)
                full_transaction_list.append(transaction)
            return full_transaction_list
        
    except FileNotFoundError as error:
        return None

# Function to convert list of objects to pysimple gui table format
def objects_to_table_data(full_transaction_list):
    return [
        [t.transaction_category,
         t.transaction_type,
         t.transaction_title,
         f'${t.transaction_amount:.2f}']
         for t in full_transaction_list
    ]

# Function to update the category list based on load data 
def update_category_list_based_on_previous_data(table_data, transaction_category_list):
    for transaction in table_data:
        if str(transaction[0]) not in transaction_category_list:
            transaction_category_list.append(transaction[0])
            
    return transaction_category_list