s = input("Введите любые символы:")
print ("Преобразование символов в код ASCII и группировка их в список.")
l = []
for x in s:
        l.append(int(ord(x)))
print (l)
print ("Сложение всех значений списка между собой.")
f = sum(l)
print (f)

