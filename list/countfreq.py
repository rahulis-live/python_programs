# Count the frequency of each element in a list without using any built-in functions like count() or collections.Counter.

l = int(input("Enter the total number of elements in the list: "))
print("Enter the Element: ")
n= []
count = 1
li = []
for j in range(l):
    n.append(int(input()))

for i in range(l):
    if n[i] not in li:
        count = 1
        for j in range(i+1,l):
            if n[j] == n[i]:
             count+=1
             li.append(n[i])
        print(n[i],count)
    
        