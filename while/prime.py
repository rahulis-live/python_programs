#write a program to find the prime of a number

n =int(input("Enter the number"))

for i in range(2,n):
    if n % i == 0:
        isTrue = False
        break
    else:
        isTrue = True
if isTrue == False:
    print("not a prime number")
else:
    print("Prime number")    
        
            
        
    
    
   
      