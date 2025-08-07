import matplotlib.pyplot as plt

# x=["amjad", 'jaba', 'prrr', 'foisndfo']
# y=[21,14,57,65]
# plt.plot(x,y,c='blue')
# plt.title('age & name')
# plt.xlabel=('name')
# plt.ylabel=('age')
# plt.show()


split=[50,30,20]
label=[split[0],'corona','dungee']
colors=['red','blue','green']
plt.pie(split,labels=label,colors=colors)
plt.title('sugamano')
plt.show()