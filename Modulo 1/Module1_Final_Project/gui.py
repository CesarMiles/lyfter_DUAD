import FreeSimpleGUI as sg
from fianance_manager import Category, MoneyTransaction, data_validation
from data_persistance import transaction_list_csv_file, csv_file_to_transaction_object, objects_to_table_data, update_category_list_based_on_previous_data

def main_window(table_data):
    sg.theme('Dark Purple 7')
    layout = [[sg.Text('                                                             Transaction Table', font=('bold'))],
              [sg.Table(table_data, justification='center', headings=['Category', 'Type', 'Title', 'Amount'], key='-TABLE-', auto_size_columns=False, expand_x=True, expand_y=True),],
              [sg.Button('Add transaction category'), sg.Button('Add expense'), sg.Button('Add income'), sg.Button('Quit')]]
    return sg.Window('Finance Manager', layout, resizable=True, finalize=True)


def add_category_transaction_window(main_win, transaction_category_list):
    layout = [[sg.Text('Please add the category to be included on the table')],
              [sg.Input(key='-CATEGORY-')],
              [sg.Button('Submit'), sg.Button('Cancel')]]
    # creating Window for Category Transaction
    add_category_win = sg.Window('Add Transaction Category', layout, finalize=True)
    
    # Category window event loop
    while True:
        event, values = add_category_win.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Submit':
            category_name = values['-CATEGORY-'].strip()
            if category_name:
                new_category = Category(category_name)
                if str(new_category) not in transaction_category_list:
                    transaction_category_list.append(str(new_category))
                    break
                else:
                    sg.popup('The category is already on the list')
                    break

    add_category_win.close()

def add_expense_window(main_win, transaction_category_list, full_transaction_list):
    layout = [[sg.Text('Please add expense to be included on the table. Please note that the type for this entry will be expense.')],
              [sg.Text('Category'), sg.Combo(transaction_category_list, default_value=transaction_category_list[0], readonly=True, key='-CATEGORY-', enable_events=True), sg.Text('Title'), sg.Input(key='-TITLE-', enable_events=True), sg.Text('Amount'), sg.Input(key='-AMOUNT-', enable_events=True)],
              [sg.Button('Submit'), sg.Button('Cancel')]]
    # creating window for expense transaction entry
    add_expense_win = sg.Window('Add Expense', layout, finalize=True)

    # Expense window event loop
    while True:
        event, values = add_expense_win.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Submit':
            try:
                transaction_category = values['-CATEGORY-'].strip()
                transaction_type = 'expense'
                transaction_title = values['-TITLE-'].strip()
                transaction_amount = values['-AMOUNT-']
                validated_data = data_validation(transaction_title, transaction_amount, sg)
                if validated_data is not None:
                    full_transaction_list.append(MoneyTransaction(transaction_category, transaction_type, transaction_title, transaction_amount))
                    new_transactions_for_table = objects_to_table_data(full_transaction_list)
                    main_win['-TABLE-'].update(new_transactions_for_table)
                    sg.popup(f'Transaction succesfully added to the table!')
                    break
            except ValueError as error:
                sg.popup_error(f'Amount must be a number: {error}')
    add_expense_win.close()

def add_income_window(main_win, transaction_category_list, full_transaction_list):
    layout = [[sg.Text('Please add income to be included on the table. Please note that the type for this entry will be income.')],
              [sg.Text('Category'), sg.Combo(transaction_category_list, default_value=transaction_category_list[0], readonly=True, key='-CATEGORY-', enable_events=True), sg.Text('Title'), sg.Input(key='-TITLE-', enable_events=True), sg.Text('Amount'), sg.Input(key='-AMOUNT-', enable_events=True)],
              [sg.Button('Submit'), sg.Button('Cancel')]]
    # creating window for income transaction entry
    add_income_win = sg.Window('Add Income', layout, finalize=True)

    # Income window event loop
    while True:
        event, values = add_income_win.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Submit':
            try:
                transaction_category = values['-CATEGORY-'].strip()
                transaction_type = 'income'
                transaction_title = values['-TITLE-'].strip()
                transaction_amount = values['-AMOUNT-']
                validated_data = data_validation(transaction_title, transaction_amount, sg)
                if validated_data is not None:
                    full_transaction_list.append(MoneyTransaction(transaction_category, transaction_type, transaction_title, transaction_amount))
                    new_transactions_for_table = objects_to_table_data(full_transaction_list)
                    main_win['-TABLE-'].update(new_transactions_for_table)
                    sg.popup(f'Transaction succesfully added to the table!')
                    break
            except ValueError as error:
                sg.popup_error(f'Amount must be a number: {error}')
    add_income_win.close()


def main():
    full_transaction_list = []
    csv_file_to_transaction_object(full_transaction_list)
    table_data = objects_to_table_data(full_transaction_list)
    transaction_category_list = []
    if full_transaction_list:
        update_category_list_based_on_previous_data(table_data, transaction_category_list)


    main_win = main_window(table_data) 

    while True:             # Event Loop
        event, values = main_win.read()
        # Closing conditions
        if event == sg.WIN_CLOSED or event == 'Quit':  
                break
        
        # Windows loop
        elif event == 'Add transaction category':
            add_category_transaction_window(main_win, transaction_category_list)
        elif event == 'Add expense':
            if not transaction_category_list: 
                sg.popup('Please enter a category before adding expense')
            else:
                add_expense_window(main_win, transaction_category_list, full_transaction_list)
                transaction_list_csv_file(full_transaction_list)
        elif event == 'Add income':
            if not transaction_category_list:
                sg.popup('Please enter a category before adding income')
            else:
                add_income_window(main_win, transaction_category_list, full_transaction_list)
                transaction_list_csv_file(full_transaction_list)

    main_win.close()

