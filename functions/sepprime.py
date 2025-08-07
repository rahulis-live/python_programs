# Create an integer list and separate the prime and non-prime numbers into two different lists.
def sepprime(n):
    a =[]
    p = []
    np = []
    count = 0  
    for i in range(n):
        a.append(int(input( )))
    # print(a)    
    for j in a:
        count = 0
        for k in range(1,j+1):
            if j % k == 0:
                count+= 1
        if count == 2:
            p.append(j)
        else:
            np.append(j)             
        
        
    print(f"prime numbers are: {p} \n non-prime numbers are : {np}")    

n = int(input("Enter the total numbers required in the integer list: "))
print("Enter the numbers :")
  
sepprime(n)