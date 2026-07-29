# activity 1

print ("want to find out how many 'a's there are in your word")
n =  (input(" what is your word "))
o = 0
for index in n:
    if index == "a":
         o = o+1 
         print (o)
print ("there are", o,"'a's in your word")

# activity 2

print ("what to find the prime numbers in a certain range of numbers?")
print ("then put your range in and find out")
low = int(input("enter a lower number  ")) 
upp = int(input("enter a higher number  "))

print ("the lower number you chose is", low)
print ("the higher number you chose is", upp)

for num in range (low, upp + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print (num, "is a prime number ")

# activity 3
poi = int(input("enter a multi-digit number (perferably an odd number)  "))



