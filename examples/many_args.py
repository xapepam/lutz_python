def function(*args):
    sum = 0
    for i in args:
        sum+=i
    return sum
 
print function(1,2,3,-1,5)
