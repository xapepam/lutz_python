def min1(*args):
        res = args[0]
        for arg in args[1:]:
                if arg < res:
                        res = arg
                        return res
while True:
        l = []
        l.clear()
        s = input("Любые числа, не более числа 10 без пробелов:")  
        for x in s:
         try:
          l.append(int(x))
         except ValueError:
          print('Это не число. Выходим.')
          raise SystemExit`````
        print (l)
        print(min1(*l))
        


