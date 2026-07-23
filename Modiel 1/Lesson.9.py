import time
A = int(input("Enter the value of the number you want to be summed"))

sum = 0
i = 1
while i <= A:
    sum = sum+i
    i = i+1
print(sum)
# activity 3
YtG = int(input("enter a number"))
sum = 0
temp = YtG
while temp > 0:
    digit = temp % 10
    sum +=digit ** 3
    temp //= 10
if YtG == sum:
    print ("This is an armstrong number")
else:
    print ("this is not an armstrong number")
# activity 2
 # abracabra make this code wait 10 seconds befored continuing
time.sleep(3.9)
B = 1
while B <= 1:
    print ("I LIKE BIRDS")
time.sleep(0.1)
