n = int(input("Enter a number you want to know the sum of"))
sum = 0
for i in range (1, n+1):
    sum = sum+i
print("Sum =", sum)

# activty 2
p = (input("enter a random word you want to be backwards")) 
p2 = ('')
for i in p:
    p2 = i + p2
print ("for the orignal word", p)
print ("for the reversed word", p2)
#activity 3
b = int(input("Enter a number you want to countdown from"))
for i in range (b,0,-1):
    print (i)