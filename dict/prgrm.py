#program to create a contact book.

d = {}
exit =1
while(exit):
    print("1.ADD CONTACT")
    print("2.EDIT CONTACT")
    print("3.DELETE CONTACT")
    print("4.DISPLAY CONTACT")
    print("5.EXIT")
    
    c = int(input("Emter your choice: "))
    
    if c==1:
        # adding contacts
        name = input("Enter the contact name: ")
        number = int(input("Enter the contact number: "))
        d[name] = number
        # print("Enter the contact Number: ")
        # d["number"] = input("Enter the contact number: ")
        
    elif c == 2:
        #edit contact
        edit = input("Enter the contact name for edit")
        if edit in d:
            x = input("Enter the new number")
            d[edit] = x
            
            print("fifjifj")
        else:
            print("Invalid user")    
        
        
    elif c ==3:
        #delete contact
        a = input("Enter the contact to delete")
        if a in d:
              d.pop(a)

    elif c ==4: 
        #displaying contacts
        for name in d.items():
            # print(name)
            print(f"name and number is :{name}")
        
    else: 
        exit = 0
