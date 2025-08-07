#Check if String Starts and Ends with the Same Character
str = input("Enter the string: ")
rev =""

for i in str:
    rev=""
    rev = i + rev 
#print(rev)
if str[0] == rev:
    print("String Starts and Ends with the Same Character")
else:
    print("NOOOOOO...........")