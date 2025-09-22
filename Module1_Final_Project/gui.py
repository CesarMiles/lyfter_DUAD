import FreeSimpleGUI as sg

def main_window():
    sg.theme('Dark Purple 7')
    layout = [[sg.Table([[]], headings=['Expense', 'Income'])],
              [sg.Button('Add a category for a transaction'), sg.Button('Add a expense'), sg.Button('Add income')]]
    return sg.Window('Finance Manager', layout, location=(800,600), finalize=True)


def add_category_transaction_window():
    layout = [[sg.Text('Please add the category to be included on the table')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), k='-OUTPUT-')],
              [sg.Button('Erase'), sg.Button('Exit')]]
    return sg.Window('Add Transaction Category', layout, finalize=True)

def add_expense_window():
    layout = [[sg.Text('Please add expense to be included on the table')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), k='-OUTPUT-')],
              [sg.Button('Erase'), sg.Button('Exit')]]
    return sg.Window('Add Transaction Category', layout, finalize=True)

def add_income_window():
    layout = [[sg.Text('Please add income to be included on the table')],
              [sg.Input(key='-IN-', enable_events=True)],
              [sg.Text(size=(25,1), k='-OUTPUT-')],
              [sg.Button('Erase'), sg.Button('Exit')]]
    return sg.Window('Add Transaction Category', layout, finalize=True)



def main():
    main, add_category, add_expense, add_income = main_window(), None, None, None    

    while True:             # Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == add_category:       # if closing win 2, mark as closed
                add_category = None
            elif window == add_expense:
                add_expense = None
            elif window == add_income:
                add_income = None
            elif window == main:     # if closing win 1, exit program
                break
        elif event == 'Add a category for a transaction' and not add_category or add_expense or add_income:
            add_category = add_category_transaction_window()
        elif event == 'Add a expense' and not add_category or add_expense or add_income:
            add_category = add_expense_window()
        elif event == 'Add income' and not add_category or add_expense or add_income:
            add_category = add_income_window()
        elif event == '-IN-':
            window['-OUTPUT-'].update(f'You enetered {values["-IN-"]}')
        elif event == 'Erase':
            window['-OUTPUT-'].update('')
            window['-IN-'].update('')
    window.close()

if __name__ == '__main__':
    main()