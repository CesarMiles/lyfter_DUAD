# Class to generate category
class Category:
    def __init__(self, category):
        self.category = category
    
    def __str__(self):
        return self.category
    

# Class to generate Finance Manager
class MoneyTransaction:
    def __init__(self,transaction_category: str, transaction_type: str, transaction_title: str, transaction_amount: float):
        self.transaction_category = transaction_category
        self.transaction_type = transaction_type
        self.transaction_title = transaction_title
        self.transaction_amount = float(transaction_amount)

    def money_transaction_to_dictionary(self):
        return {
            'transaction category' : self.transaction_category,
            'transaction type' : self.transaction_type,
            'transaction title' : self.transaction_title,
            'transaction amount' : self.transaction_amount
                }
    
    def __str__(self):
        return f'{self.transaction_category} {self.transaction_type} {self.transaction_title} ${self.transaction_amount:.2f}'



