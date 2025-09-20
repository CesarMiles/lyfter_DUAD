import json
import os
from src.logic.finance import Category, MoneyTransactions
from pathlib import Path

class FileManager:
    def __init__(self, data_folder = 'data'):
        self.data_folder = Path(data_folder)
        self.data_folder.mkdir(exist_ok = True)

        self.categories_file = self.data_folder / 'categories.json'
        self.transaction_file = self.data_folder / 'transactions.json'
    
    def save_categories(self, categories):
        data = [{'name': cat.name} for cat in categories]
        with open(self.categories_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)
    
    def load_categories(self):
        if not self.categories_file.exists():
            return []
        
        with open(self.categories_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return [Category(item['name']) for item in data]
    
    def save_transactions(self, transactions):
        data = []
        for trans in transactions:
            transaction_data = {
                'title': trans.title,
                'amount': trans.amount,
                'category': trans.category,
                'type': trans.type
            }
            data.append(transaction_data)
        
        with open(self.transaction_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ident=2)
    
    def load_transactions(self):
        if not self.transactions_file.exists():
            return []
        
        with open(self.transaction_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        return [MoneyTransactions(item['title'], item['amount'], item['category'], item['type']) for item in data]