def add(v,z):
    return (v+z)

def sub(v,z):
    return (v-z)

def div(v,z):
    return (v/z)

def mul(v,z):
    return (v*z)

v = int(input("enter a number"))
z = int(input("enter another number"))

print ("A = addition")

print ("B = subtract")

print ("C = division")

print ("D = Mulitplycation ")

Q = (input("what do you want to do with these numbers?? "))

if Q == "A":
    print(add (v,z))
elif Q=="B":
    print(sub (v,z))
elif Q == "C":
    print(div (v,z))
elif Q == "D":
    print (mul (v,z))
else:
    print ("this is an invalid statemnt, try removing any spaces before the letter and after the letter and enter one of the option, or making the letter uppercase")