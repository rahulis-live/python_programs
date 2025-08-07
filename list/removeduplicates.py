# remove dulplicates from a list
li = [1,2,2,3,4]
l = []

for i in li:
    if i not in l:
        l.append(i)
        
print(l)