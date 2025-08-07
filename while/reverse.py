#program to find a reverse and palindrome
n = int(input("Enter a number: "))
b = n
r = 0
while n > 0:
    a = n % 10
    r =(r  * 10) + a
    n = n // 10
    
print("reverse of a number is : ", r)    
    
if r == b:
    print("palindrome")
else:
    print("not palindrome")        
    
