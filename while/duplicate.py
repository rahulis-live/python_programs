#  Remove duplicate characters from a string.

n = input("Enter the String: ")
l= len(n)
count = 1
li = " "
for i in range(l):
    if n[i] not in li:
        count = 1
        for j in range(i+1,l):
            if n[j] == n[i]:
             count+=1
             li+=n[i]
        print(n[i],end="")
          
          
        
