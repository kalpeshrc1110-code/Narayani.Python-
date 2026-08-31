# activity 1

class student:
    grade = 10
    print ("hi im a student of grade", grade)

ob = student()

#activity 2

class car:

    def __init__(self, maxspeed, mileage):

        self.maxspeed = maxspeed
        self.mileage = mileage


honda = car ('250', '18' )

print ("tha max speed of honda is", honda.maxspeed, "and for every liter of petrol this car can go", honda.mileage, "miles")

# activity 3

class parrot:
    species = 'lovebird'

    def __init__(self, age, name, type):
        self.age = age
        self.name = name
        self.type = type

bird = parrot('4', 'Neal', 'African blue lovebird')
love = parrot('7', 'Cutey','lovebird..?')

print (bird.age, bird.name, bird.type)
print (love.age, love.name, love.type)

