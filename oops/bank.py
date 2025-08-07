## Modelling a bank account

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} is deposited./nNew balance is {self.balance}")
    
    def withraw(self,amount):
        if amount > self.balance:
             print("Insufficient Funds")
        else:
            self.balance-= amount
            print(f"{amount} is withdrawn. /nNew balance is {self.balance}")
    def get_balance(self):
        print(f"Balance in the account is {self.balance}")        
            
account = BankAccount("Krish",3000)
print(account.balance)                    

# Call Instance Methods 
account.deposit(2000)  
account.get_balance()
account.withraw(1000)
