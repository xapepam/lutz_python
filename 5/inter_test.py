args = ['S','P','A','M']
for x in args[0]:
    for other in args[1:]:
        if x not in other: print (x)
    else:
        print (x)
    
