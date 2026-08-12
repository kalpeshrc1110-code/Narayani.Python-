def shut ():
    print ("shutting down system")

def hut ():
    print ("the system will not shut down")

n = (input("""would you like to shut down system? 
Y/N """))

if n == 'Y':
    shut ()
    
elif n == 'N':
    hut ()
else:
    print ("sorry this is an invalid response")
    
