# update th first set with items that dont exis in the second set.
s1={1,2,3,"rahul",4}
s2={2,3,4}

s3 = s1.intersection(s2)
# print(s3)
s3=s3.symmetric_difference(s1)
print(s3)
