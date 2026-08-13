#activty 1

import random 
import time

print ("try to guess the number between 0-10")
x = int(input("enter a number that u wish to guess "))

y = random.randint (0,10)
if y == x:
    time.sleep(0.3)
    print ("you guessed the number correct! bravo!")
else:
    time.sleep(0.5)
    print ("the number you guess is incorrect ")
print ("you guessed", x)
time.sleep(1)
print ("the number was", y)

# Activity 2

while True:
    n = (input("Enter an input ( Rock, Paper, Scissors) "))
    m = random.choice (["Rock", "Paper", "Scissors"])
    if n == m:
        print ("Its a tie!")
    elif m == 'Scissors' and n == 'Paper':
        print ("computer wins! you chose paper and computer chose sissors")
    elif m == 'Paper' and n == 'Scissors':
            print ("You wins! you chose Scissors and computer chose paper")
    elif m == 'Rock' and n == 'Paper':
            print ("You wins! you chose Paper and computer chose rock")
    elif m == 'Paper' and n == 'Rock':
            print ("computer wins! you chose rock and computer chose paper")
    elif m == 'Scissors' and n == 'Rock':
                print ("You wins! you chose roc and computer chose scissors")
    elif m == 'Rock' and n == 'Scissors':
            print ("computer wins! you chose scissors and computer chose rock")
    else:
          print ("ERROR!! WRONG INPUT!!")

