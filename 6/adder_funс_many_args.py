def adder(*a):
    p = a[0]
    for next in a[1:]:
       p = next + p
    print (p)

       
# adder ('str1','str2','str3')
adder ([1,2,3],[4,5,6])
adder (1,2,3,4,5,6,7,8,9,10,500,785)
# adder (2.0,5.4)
input("Press enter to exit ;)")
        
    
    
