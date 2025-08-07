str = input("Enter the string: ")
rev =""

for i in str:
    rev = i + rev 
if rev == str:
    print("Palindrome")
else:
    print("not palindrome")    

     