class Appliance:
    def __init__(self,brand,power_rating,status):
        self.brand = brand
        self.power_rating = power_rating
        self.status = status
        
    def turn_on(self):
        self.status = "ON"
        print(f"{self.brand} is now {self.status}")
    def turn_off(self):
        self.status = "OFF"
        print(f"{self.brand} is now {self.status}")
    def show_info(self):
        print(f"Brand name is {self.brand}\nPower rating is {self.power_rating}\nStatus is {self.status}")
    
    
    
class WashingMachine(Appliance):
    def __init__(self,brand,power_rating,status,mode):
        super().__init__(brand,power_rating,status)
        self.mode = mode

    
    def set_mode(self):
        x = input("Enter Wash Mode: ")
        self.mode = x       
        print(f"Wash Mode set to {x}")
    def start_wash(self):
        print(f"Washing {capacity} load using {self.mode} mode...")
    
print("\nSMART WASHING MACHINE SETUP\n")

brand = input("Enter Applicance brand: ")
power = int(input("Enter Power rating (W): "))
capacity = int(input("Enter Capacity (in Kg): ")) 
status ="OFF"
mode=""
obj = WashingMachine(brand,power,status,mode)

exit = 1
while(exit):
    print("1.Turn ON\n2.Turn OFF\n3.Set Wash Mode\n4.Start Washing\n5.Show Appliance Info\n6.EXIT")
    
    choice = int(input("Enter the choice: "))   
    if choice == 1:
        obj.turn_on()
    elif choice == 2:
        obj.turn_off()
    elif choice == 3:
        obj.set_mode()  
    elif choice == 4:
        obj.start_wash()
    elif choice == 5:
        obj.show_info()      
    else:
        exit = 0          