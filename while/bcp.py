#program to know about break, continue and pass



#break
i =1
while i <= 5:
    print(i)
    if i == 3:
        break
    
#continue
while i <= 5:
    i+=1
    if i == 3:
        continue
    print(i)
        
#pass
while i <= 5:
    pass    

#else can be used in "while" and "for loop" also
i =1
while i <= 5:
    print(i)
    i+=1
else:
    print("hii")
    #this else will not work if we add any break statemnts in the while portion
    
