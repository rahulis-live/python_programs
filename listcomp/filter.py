# filter word with length > 3 using list comprehension

a = ["hello","hii","bye","comeon"]
b = [i for i in a if len(i) > 3 ]
print(b)

# for i in a:
#     if len(i) > 3:
#         print(i)