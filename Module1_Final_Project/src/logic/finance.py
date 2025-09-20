
# Class to define the money transactions
class MoneyTransactions:
    def __init__(self, title: str, amount: float, category: str, type: str):
        self.title = title
        self.amount = amount
        self.category = category
        self.type = type
        self.date = None

    # Function to write on string format the information from transactions
    def __str__(self):
        return f'{self.type.capitalize()}: {self.title} - ${self.amount} ({self.category})'

# Class for money movement organization
class Category:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name

# Class to create the finance manager
class FinanceManager:
    def __init__(self, file_manager = None):
        self.money_transactions = []
        self.categories = []
        self.file_manager = file_manager

        if self.file_manager:
            self.load_data()
    
    # Function to load data from files
    def load_data(self):
        self.categories = self.file_manager.load_categories()
        self.money_transactions = self.file_manager.load_transactions()
    
    # Function to save data on files
    def save_data(self):
        if self.file_manager:
            self.file_manager.save_categories(self.categories)
            self.file_manager.save_transactions(self.money_transactions)
    
    # Function to process money transactions
    def add_money_transaction(self, money_transaction: MoneyTransactions):
        self.money_transactions.append(money_transaction)
        self.save_data()
    
    # Function to add categories and avoid them if is already on the list
    def add_category(self, category: Category):
        if not any(cat.name == category.name for cat in self.categories):
            self.categories.append(category)
            self.save_data()
    
    # Function to retrieve caterogies from the list
    def obtain_categories(self):
        return [cat.name for cat in self.categories]
    
    def obtain_money_movements_per_type(self, type: str):
        return [mov for mov in self.money_transactions if mov.type == type]

