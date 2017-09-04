D = {'name': 'mel', 'age': 45, 'name1': 'mike', 'age':15, '100': 'yes', 'enable': 'no', 'status':'common'}
k = list(D.keys())
k.sort()
print (k)
for i in k:
    print (D[i])
