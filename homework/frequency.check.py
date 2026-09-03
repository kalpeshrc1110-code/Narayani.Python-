code = {"codingal" : 1, "is" : 2, "best" : 2, "for" :2, "learning": 2, "code" : 3}

n = (input("would u like to check the frequency of the code? Y/N: "))
if n == 'Y':
    m = int(input("enter the number you would like to check! 1/2/3: "))
    if m == 1:
        print ("the occorance of '1' in 'code' happens once")
    elif m == 2:
        print ("the occorance of '2' in 'code' is three times")
    elif m == 3:
        print ("the occorance of '3' in 'code' is once")
    else:
        print ("invalid awnser")
else:
    print ("you will not be checking frequency of code")

