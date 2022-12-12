#use time module and use conditional statement
#exercise- good morning sir

import time


a = int(time.strftime('%H'))
if a<12:
    print("Good Morning Sir.")
elif a>12 and a<16:
    print("Good Afternoon Sir.")
else:
    print("Good evening sir.")