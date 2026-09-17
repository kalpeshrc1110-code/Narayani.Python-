#activity 2

class computer():

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print ("sell price is :" .format(self.__maxprice))

    def setmaxprice(self, price):
        self.__maxprice = price

c = computer()
c.sell()

c.setmaxprice(1000) 
c.sell()

c.sell()
c.__maxprice = 1000
c.sell()

# activity 3
class point():
    def __init__ (x=0, y=0,):
        self.x = x
        self.y = y
        


# activity 1
class bird():
    __penguin = 97
  

    def __hawk(self):
        print ("this is very private info but hawks are predetory borbsssss")

    def peacock(self):
        print ("helooo did you know that", bird.__hawk)

macaw = bird()
macaw.peacock()
macaw.__hawk()


