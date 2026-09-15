# Activity 1

class car:
    def __init__(self, speed, gas):
        self.speed = speed
        self.gas = gas

class car_pet(car):
    pass

pet_car = car_pet (272, 70)
print("the speed the car is able to is: ", pet_car.speed, "the amount of gas this car can hold is", pet_car.gas )

# Activity 2

class Parent():
    def __init__(self, lastname, eyes):
        self.lastname = lastname
        self.eyes = eyes
    def display(self):
        print (self.lastname)
        print (self.eyes)

class Child(Parent):
    def __init__(self,lastname, eyes, name,age):
        self.name = name
        self.age = age

        Parent.__init__(self,lastname,eyes)

a = Child('Chaudhari', 'brown', 'Narayani', 12)
a.display()

# Activity 3

class borbs():
    def __init__(self):
        print ("im borb and borb is me")

    def fly(self):
        print ("most borb can fly")

    def beak(self):
        print ("all borb have beaks ")

class hummingborb(borbs):
    def __init__(self):
        print ("i am humming borb and humming brob is me")
        super().__init__()
    def fly(self):
        print ("i flap me wings almost 100 times in a second")
        
    def beak(self):
        print ("my beak is very thin ")

a = hummingborb()
a.fly()
a.beak()





