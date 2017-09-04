L = [1, 2, 4, 8, 16, 10,  39, 64]
for X in L:
    if 2 ** 5 == X:
        print('Found at index #', L.index(X))
        break
    else:
        print('At index #', L.index(X), 'not found')

    
    
    
