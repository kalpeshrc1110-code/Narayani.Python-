clr1 = {'green', 'blue',}
clr2 = ('blue', )
if clr1 != clr2:
    print (clr1.difference(clr2, ))

num1 = {1,2,3,4,5}
num2 = {1,3,5,}
if num1 != num2:
    print (num1.difference(num2))