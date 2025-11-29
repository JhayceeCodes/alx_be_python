class BankAccount:
    
    def __init__(self, account_balance = 0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    
    def withdraw(self, amount):
       
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        print(f"Current Balance: ${self.account_balance}")

mybank = BankAccount(100)
mybank.display_balance()
mybank.deposit(50)
mybank.display_balance()
mybank.withdraw(100)
print(mybank.withdraw(50))
mybank.display_balance()

