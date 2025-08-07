class Atm:
    def __init__(self,name,number,balance=0):
        self.name = name
        self.number = number
        self.balance = balance
        
    def deposit(self):
        x = int(input("Enter the AMOUNT TO BE DEPOSITED: "))
        self.balance+=x
        
    def withraw(self):
        y = int(input("Enter the AMOUNT TO BE WITHRWAN: "))
        if y > self.balance:
            print("INSUFFUCIENT FUND")
        else:
            self.balance-=y    
            
    def display(self):
        print(f"Balance amount is {self.balance}")
        
name = input("Enter the ACCOUNT HOLDER NAME: ")
number = int(input("Enter the ACCOUNT NUMBER: "))
obj = Atm("name",number)
exit = 1
while(exit):
    print("1.DEPOSIT\n2.WITHRAW\n3.DISPLAY\n4.EXIT")
    c = int(input("ENTER THE CHOICE"))
    if c == 1:
         obj.deposit()
    elif c == 2:
        obj.withraw()
    elif c == 3:
        obj.display()   
    else:
        exit = 0      
         
   
    