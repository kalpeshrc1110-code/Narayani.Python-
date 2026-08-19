#activity 1

a1 = ('n', 'b', 'i', (9,6,2), 'n', 'd',)
print (a1)
a2 = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
print (a2)
a3 = (a1 + a2)
print (a3)
a4 = (1,5,2,8,)
print (len(a4))
a5 = (1,4,6,2)
slice = a5 [1:3]
print (slice)

#activity 2

def tide(r):
    e = (len(r))
    s = 0
    while s<e:
        if r[s] != r[e]:
            return False 
        else:
            e-=1
            s+=1
    return True
    


r = (1,2,3,4,4,3,2,1)
if (tide(r)):
    print ("this is a flip-flop number")
else:
    print ("this is a not flip-flop number")



