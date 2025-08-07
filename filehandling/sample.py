# creates a new file - "x"
# f = open("sample1.txt","x")
# f.close()

# adds content to an empty file or to an already written file
# f = open("sample1.txt","a")
# f.write("helloo makkaleyy")
# f.close()

#creates  a new file and also if file exists overwrites
# f = open("sample.txt","w")
# f.write("Hello moneeeyyy")
# f.close()

f = open("sample.txt","r")
# s = f.read()
# s = f.readline()
# s = f.readlines()
# # for i in s:
# #  print(i.strip())
# print(s)    
for i in f:
 s = f.readline()
print(s)