a=[154444444444444444,45450,9,5654654,3,654546548,4654654,6,2645654]

print (a)
n=len(a)
m=n-1
while m>0:
 for i in range(m):
  if (a[i]>a[i+1]):
   x=a[i]
   a[i]=a[i+1]
   a[i+1]=x
 m=m-1
print(a)
