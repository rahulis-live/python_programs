#second largest number in a list

l = [23,45,321,212]
larg = second = 0
for i in l:
    if i > larg:
        second = larg
        larg = i
    elif i < larg and i > second:
        second = i    
print(second)        
print(larg)        