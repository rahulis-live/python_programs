# sort a tuple
s =(5,3,6,4)
li = list(s)
n = len(li)

for i in range(n):
    for j in range(0, n - i - 1):
        if li[j] > li[j +1]:
            li[j], li[j+1] = li[j+1], li[j]
s = tuple(li)

print(s)            
            
            
        
 