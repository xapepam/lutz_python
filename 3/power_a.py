L = [1, 2, 4, 8, 16, 9, 39, 64]
X = 5
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i = i+1   
else:
    print('not found')
    
    
