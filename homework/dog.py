class dog:
    def __init__(self, breed, name, age,):
        self.breed = breed
        self.name = name
        self.age = age

beagle = dog('beagle', 'Tracker', 5)
poodle = dog('Poodle', 'lovely', 7)

print (beagle.breed, beagle.name, beagle.age)
print (poodle.breed, poodle.name, poodle.age)