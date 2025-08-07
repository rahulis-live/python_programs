d = {"Name": "Rahul" ,"Age" : 23, "place" : "Palakkad"}
print(d)
type(d)
print(d["Name"])
print(d.get('Age'))

a = dict(course = 'python', mentor = 'radhika',duration = 6)
print(a)

print(d.keys())
print(a.keys())

print(d.values())

d['sugam']= "adhe"
print(d)

d.update({"ajmal":"mananrkad", "nibraz":"malappuram"})
print(d)

d.pop('nibraz')
print(d)

d.popitem()
print(d)

# d.clear()
# del.d()