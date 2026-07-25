wea = int(input("the tempature outside is________ degrees"))
if (wea>=-6 and wea<14):
    print ("Rohan can wear a jacket and pullovers, because it is cold today")
elif ( wea>=14 and wea<21 ):
    print ("Rohan has to wear a jacket OR pullovers, because it is chilly today")
elif (wea<=-7):
    print ("Rohan has to wear winter cloths, because it is freezing today")
else: 
    print (" Rohan can wear something light and soft")
