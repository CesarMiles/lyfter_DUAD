# Class bank to be used to create customer's banking accounts
class BankAccounts():
    balance = 0

    # Function to deposit money to the balance
    def deposit_balance(self, amount):
        self.balance += amount
        return self.balance
        
    # Function to withdraw money from balance
    def withdraw_balance(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            print(f'Fondos insuficientes')
            return self.balance

# Instance to create saving accounts and inherit BankAccount class methods
class SavingAccount(BankAccounts):
    def __init__(self, balance, min_balance):
        self.min_balance = min_balance
        self.balance = balance
    
    # Function to calculate remaining balance 
    def saving_withdraw(self, amount):
        remaining_balance = self.balance - amount
        if remaining_balance < self.min_balance:
            print(f'Transaction cannot be completed. Remaining balance ({remaining_balance}) is below minimum balance {self.min_balance}')
        else:
            print(f'the amount {amount} has been succesfully deducted, your remaining balance is {remaining_balance}')
            return BankAccounts.withdraw_balance(self, amount)


# Testing zone
savingaccount = SavingAccount(500, 50)
savingaccount.saving_withdraw(451)
savingaccount.deposit_balance(300)
print(savingaccount.balance)