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