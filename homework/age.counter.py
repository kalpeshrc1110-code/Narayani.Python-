a = 2
while a > 1:
    try:
        n = int(input("Enter your age "))
    except:
        if ValueError:
            print ("WRONG VALUE ENTERED!!! PLEASE TRY AGAIN")
    finally:
        if n / 2 == 0:
            print ("your age is an even number")
        else:
            print ("your age is not an even number")
    a = a+1281