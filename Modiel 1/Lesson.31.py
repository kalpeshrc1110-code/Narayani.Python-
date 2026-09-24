class a:
    def __init__ (self, a):
        self.a = a

    def __it__ (self, other):
        self.other = other
        if (self.a>other.a):
            return "this is less"
        else:
            return "this is greater"

    def __eq__ (self, other):
        if (self.a == other.a):
            return "equal"
        else:
            return "this is not equal"

ob1 = a(2)
ob2 = a(3)

print ("passed down ", ob1.a, ob2.a)
print (ob2.a == ob1.a)
    
