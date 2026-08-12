#Activty 1
try:
    n = int(input("enter a number"))
    print ("you have entered", n)
except ValueError as ex:
    print ("you have not entered a number! please try again later...", ex)
# but using except you skip the syntaxerror


#activity 3

valid = False
while not valid:
    try:
        n,m=int(input("enter 2 numbers"))
        while n%m != 0:
            print ("bye")
        
            print ("BYE")
    except ValueError:
        print ("invalid response")


#activty 2

try:
    num1, num2 = int(input(" Enter 2 numbers seperate the numbers using comma  "))
    n = num1 / num2 
    print (n)
except ZeroDivisionError as ex:
    print ("the numbers cannot be 0")
except SyntaxError as ex:
    print ("""you forgot the comma put a comma in like this
    1,2 """)
#except ValueError as ex:
    #print ("dont add a space between the numbers")
finally:
    print ("this will run no matter what")

          