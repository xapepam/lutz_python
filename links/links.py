import webbrowser
while True:
    print ('Hello this is sorage and link-selecter \n')
    print ('\n')
    print ('Choose number to open link: \n 1. Bublesort \n 2. Selectsort\n 3. epmty \n 4. empty \n \n 0. Exit \n')
    x = int(input('Enter a number: '))
    if x == 1:
      webbrowser.open('http://py-algorithm.blogspot.ru/2011/10/blog-post.html')
    if x == 2:
      webbrowser.open('http://ya.ru')

