import random 
import time

print ("""The computer is choosing a number between 1-10!
Guess the correct number the computer has chosen!!""")
n = int(input("Enter a number that you wish to guess "))

m = random.randint (0,10)
if m == n:
    time.sleep(0.3)
    print ("you guessed the number correct! bravo!")
else:
    time.sleep(0.7)
    print ("the number you guess is incorrect ")
print ("you guessed", n)
time.sleep(1)
print ("the number was", m)
