import FreeSimpleGUI as sg
from fianance_manager import Category

def main_window(transaction_category_list):
    sg.theme('Dark Purple 7')
    layout = [[sg.Text('           '), sg.Text('Transaction Table', font=('bold'))],
              [sg.Text('           '), sg.Table([[transaction_category_list]], headings=['Category', 'Type', 'Title', 'Amount'], key='-TABLE-')],
              [sg.Button('Add transaction category'), sg.Button('Add expense'), sg.Button('Add income')]]
    return sg.Window('Finance Manager', layout, location=(800,600), finalize=True)


def add_category_transaction_window(main_win, transaction_category_list):
    layout = [[sg.Text('Please add the category to be included on the table')],
              [sg.Input(key='-CATEGORY-', enable_events=True)],
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
                transaction_category_list.append(str(new_category))
                main_win['-TABLE-'].update(transaction_category_list)
    add_category_win.close()

def add_expense_window():
    layout = [[sg.Text('Please add expense to be included on the table')],
              [sg.Text('Category'), sg.Input(key='-CATEGORY-', enable_events=True), sg.Text('Type: '), sg.Text('expense', background_color='RoyalBlue4', key='-TYPE-'), sg.Text('Title'), sg.Input(key='-TITLE-', enable_events=True), sg.Text('Amount'), sg.Input(key='-AMOUNT-', enable_events=True)],
              [sg.Button('Submit'), sg.Button('Cancel')]]
    return sg.Window('Add Expense', layout, finalize=True)

def add_income_window():
    layout = [[sg.Text('Please add income to be included on the table')],
              [sg.Text('Category'), sg.Input(key='-CATEGORY-', enable_events=True), sg.Text('Type: '), sg.Text('Expense', background_color='RoyalBlue4', key='-TYPE-'), sg.Text('Title'), sg.Input(key='-TITLE-', enable_events=True), sg.Text('Amount'), sg.Input(key='-AMOUNT-', enable_events=True)],
              [sg.Button('Submit'), sg.Button('Cancel')]]
    return sg.Window('Add Income', layout, finalize=True)



def main():
    transaction_category_list = [] 
    main_win = main_window(transaction_category_list) 
    add_expense, add_income = None, None

    while True:             # Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            window.close()
            if window == add_category:      
                add_category = None
            elif window == add_expense:
                add_expense = None
            elif window == add_income:
                add_income = None
            elif window == main:    
                break

        elif event == 'Add transaction category':
            add_category = add_category_transaction_window(main_win, transaction_category_list)
        elif event == 'Add expense' and not add_category and not add_expense and not add_income:
            add_expense = add_expense_window()
        elif event == 'Add income' and not add_category and not add_expense and not add_income:
            add_income = add_income_window()
        # elif event == 'Submit':
        #     if window == add_category:
        #         category_name = values['-CATEGORY-'].strip()
        #         if category_name:
        #             new_category = Category(category_name)
        #             transaction_category_list.append(str(new_category))
        #             main_win['-TABLE-'].update(transaction_category_list)
    #     elif event == 'Erase': #Pending to add Submit FUnction
    #         window['-OUTPUT-'].update('')
    #         window['-IN-'].update('')
    window.close()

if __name__ == '__main__':
    main()