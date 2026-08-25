# activity 1
list1 = (1, 3, 5)
list2 = (3, 5, 7)
results = map(lambda x, y: x + y, list1, list2)
print (list (results))

# activity 2
list3 = (10,20,30,40)
list4 = (100, 200, 300, 400)
for x,y in zip(list3, list4[::-1]):
    print (x,y)


stock = ['crayons', 'paper', 'pencil', 'markers', ]
price = [1.75, 2.99, 0.99, 5.75]

my_dict = {stock: price for stock,
           price in zip(stock, price)}
print (my_dict)

# activity 3
for i in range (10):
    if i == 5:
        exit()
    else:
        print (i)
        #we learned about zip, exit, map and lambda