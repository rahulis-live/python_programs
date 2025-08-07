from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def process_payment(self,amt):
        pass
    def transaction_summary(self,name,amt,method):
        print(f"TRANSACTION SUMMARY")
        print(f"name : {name}")
        print(f"amt : {amt}")
        print(f"method : {method}")
        
class CreditCardPayment(Payment):
    def __init__(self,name,accno):
        self.name = name
        self.accno = accno
        
    def process_payment(self,amt):
        print(f"\n{self.name} paid {amt} using Credit Card ending with {self.accno[10:]}")
        
        print("Transaction succesfull\n")
        
        self.transaction_summary(self.name,amt,"CREDIT CARD")
class UPIPayment(Payment):
    def __init__(self,name,upiid):
        self.name = name
        self.upiid = upiid
    
    def process_payment(self,amt):
        
        if amt > 5000:
            print(f"{self.name} attempted to pay {amt} via UPI ({self.upiid})")
            print("Transcation Failed: Limit Exceeded")
        else:    
            print(f"{self.name} paid {amt} via UPI ({self.upiid})")
            print("Transaction succesfull")           
            self.transaction_summary(self.name,amt,"UPI")

exit =1
while(exit):

    print("\n1.CREDIT CARD\n2.PRCOESS CREDIT CARD\n3.UPI ID\n4.PROCESS UPI ID")
    choice=int(input("Enter the choice"))
    if choice ==1:
        
        p1 = CreditCardPayment("Rahul","1234-xxxx-5678")       
    elif choice ==2:
         p1.process_payment(3500) 
    elif choice ==3:
        x = int(input("Enter the amount to be paid be paid via UPI: "))
        p2 = UPIPayment("Chikku","chikku@upi")
    elif choice == 4:
         p2.process_payment(x)  
    else:
        exit=0
        