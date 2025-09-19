
# Class to define the money transactions
class MoneyTransactions:
    def __init__(self, title: str, amount: float, category: str, type: str):
        self.title = title
        self.amount = amount
        self.category = category
        self.type = type
        self.date = None

    def __str__(self):
        return f'{self.type.capitalize()}: {self.title} - ${self.amount} ({self.category})'

# Class for money movement organization
class Category:
    def __init__(self, name: str):
        self.name = name
    
    def __str__(self):
        return self.name

class FinanceManager:
    def __init__(self):
        self.money_transactions = []
        self.categories = []
    
    def add_money_transaction(self, money_transaction: MoneyTransactions):
        self.money_transactions.append(money_transaction)
    
    # Function to add categories and avoid them if is already on the list
    def add_category(self, category: Category):
        if not any(cat.name == category.name for cat in self.categories):
            self.categories.append(category)
    
    # Function to retrieve caterogies from the list
    def obtain_categories(self):
        return [cat.name for cat in self.categories]
    
    def obtain_money_movements_per_type(self, type: str):
        return [mov for mov in self.money_transactions if mov.type == type]

