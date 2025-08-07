#swapping two list without creating third list


def listswap(a,b):

    for i in range(len(a)) :
        for j in range(len(a)):
            if a[i] % 2 == 0 and b[i] % 2 != 0:
                a[i], b[i] = b[i], a[i]
  
    print(a,b)   
    
a = [1, 2, 3]
b = [4, 5, 6]
l = len(a)  
listswap(a,b)  
            
      
            
         