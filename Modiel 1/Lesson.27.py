# Activity 1
class IOString:

    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = (input("Enter string :  "))

    def print_str1(self):
        print("results in: ", self.str1.upper())


str1 = IOString()

str1.get_string()

str1.print_str1()

#activity 2

class employee:

    def __init__(self):
        print ("constructer is called")

    def __del__(self):
        print ("destructer is created")

def birb():
    print ('making birb please wait')
    birb = employee()
    print ('function end')
    return birb

print ('calling birb function')
birb2 = birb()
print ('progrem ende')

# Activity 3

class pair_element:
    def twosum(self, nums, target ):
        lookup = {}
        for i,num in enumerate(nums):
            if target - num in lookup:
                return (lookup[target - num], i)
            lookup[num] = i

value = int(input("enter a number divisible by ten, and under 130 thank you.  " ))
print("index1=%d, index2=%d" % 
      pair_element().twosum((10,20,30,40,50,60,70),value))




