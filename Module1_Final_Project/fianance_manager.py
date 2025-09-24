# Class to generate category
class Category:
    def __init__(self, category):
        self.category = category
    
    def category_to_dictionary(self):
        return {
            'transaction category' : self.category 
                }
    
    def __str__(self):
        return self.category
    

# Class to generate Finance Manager
class MoneyTransaction:
    def __init__(self, transaction_type: str, transaction_title: str, transaction_amount: float):
        self.transaction_type = transaction_type
        self.transaction_title = transaction_title
        self.transaction_amount = transaction_amount

    def money_transaction_to_dictionary(self):
        return {
            'transaction category' : str(self.transaction_category),
            'transaction type' : self.transaction_type,
            'transaction title' : self.transaction_title,
            'transaction amount' : self.transaction_amount
                }
    
    def __str__(self, category):
        return (f'Category: {category} -Type: {self.transaction_type} - Title: {self.transaction_title} - Amount: {self.transaction_amount:.2f}')



