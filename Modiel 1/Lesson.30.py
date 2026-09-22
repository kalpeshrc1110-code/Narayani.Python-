from abc import ABC, abstractmethod 
class absclass(ABC):
    def print (self, x):
        self.x = x
        print ("passed value", x)

    @abstractmethod
    def task(self):
        print ("we are in ")

class task2(absclass):
    def task (self):
        print ("ah yes, we are in gng")

test_orb = task2()
test_orb.task()
test_orb.print (100)

#activty 3

class cockatiel():
    def size(self):
      
        print ("cockatiels are medium sized birds")

    def uf(self):
        print ("cockatiel have a crest that looks similar to a crown, not many birds have this")

    def colour(self):
        print ("""cockateils come in vast varitiys of browns and greys and whites and yellow and reds,
          with their heads being yellow with red cheeks and their body being all the oabove""")


class conure():
    def size(self):
        print ("conures are medium sized birds")
    
    def uf(self):
        print ("conures are conures")
    
    def colour(self):
        print ("R A I N B O W")

obj_cockatiel = cockatiel()
obj_conure = conure()

for bird in (obj_conure,obj_cockatiel):
    bird.size()
    bird.uf()
    bird.colour()
