# count the number of times each element occurs in the list

n = [1,2,2,3,1,3,4,1,1]
li = [] 
for ch in n:
    if ch not in li:
        count = 0
        for x in n:
            if x == ch:
                count += 1
        print(ch, count)
        li.append(ch) 

        
        