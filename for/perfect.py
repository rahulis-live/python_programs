# perfect number

n = int(input("Enter the Number"))
l  = []
for i in range(1,n):
    if n % i == 0:
       l.append(i)
print(l)  
s = 0  
for i in l:
    s+=i
print(s)  
if s == n:
    print("perfect number")
else:
    print("not  a perfect number")    
    