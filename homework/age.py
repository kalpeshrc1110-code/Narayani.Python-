U = int(input("What is your age?"))
if (U<=-1):
    ("ERROR IN SYSTEM!! THIS AGE IS NOT YET BORN")
elif (U>=10 and U<21):
    print (" your age is between 10-20")
elif (U>=21 and U<65):
    print ("you are an adult")
elif (U>65 and U<100):
    print ("you are very old")
elif (U>100 and U<116):
    print ("you more then a centry old")
elif (U>116 and U<150):
    print ("you are the oldest person alive")
elif (U>=150):
    print ("This system does not believe you are this old!")
else:
    print ("you are younger then 10")
