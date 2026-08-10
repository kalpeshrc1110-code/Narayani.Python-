# activity 1
def tax (n):
    return n * 0.13

def tip (n):
    return n * 0.15
    
 

n = int(input("enter the amount you spend at the restraunt (tax not included) $"))

print ("the tax will be $", tax(n) )
print ("the tip will be $", tip(n) )

# activity 2
def cube (num):
    return num*num*num

def by_three (num):
    if num% 3 == 0:
        return cube (num)
    else:
        return False



num = int(input("enter a number to find the cube of it"))
print ("the cube of ", num, "is", by_three (num))
 # acticity 3

def factorial (x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial (x-1)

x = int(input("enter a number to find the factotial of the number "))

print (factorial(x), "is the factorial of the number")






    