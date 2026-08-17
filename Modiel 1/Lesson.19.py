#activity 1
from datetime import datetime , timedelta
import calendar
import random
import datetime


print (datetime.datetime.now())

print (calendar.month(2026,8))

#activity 2

start = datetime.datetime(2000,1,4,5,6,0,0)

end = datetime.datetime(2999,1,4,5,6,0,0)

time = end - start

randoms = random.randint(0,int(time.total_seconds()))

random_date = start + timedelta(seconds = randoms)

print("the random date cohsen is", random_date)

#activity 3




