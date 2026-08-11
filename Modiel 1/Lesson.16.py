# activity 1
word = (input("Enter a word"))

for i in word:
    if (i== 'a'):
        print ("'a' has been detected in this word")
        break
else:
     print ("there is no 'a' in this word")

# activity 2
b = int(input("enter a number"))

if b % 20 == 0:
        print ("twist")
if b % 15 == 0:
        pass
if b % 5 == 0:
        print ("fizz")
if b % 3 == 0:
        print ("buzz")
else:
        print ("this number is not divisable by 20, 15, 5 or 3... better luck next time")

# activty 3

e = 11
for i in range (1, 11):
       e = e-1
       if e == 5:
              continue
       else:
             print (e)

       
    


