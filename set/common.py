# return a new set of identical items from two sets
s1={1,2,3}
s2={"rahul","is","happy",2}
s3=s1.intersection(s2)

if len(s3) == 0:
    print("empty set")
else:
    print(s3)