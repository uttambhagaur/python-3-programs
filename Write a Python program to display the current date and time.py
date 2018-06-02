# Write a Python program to display the current date and time.
# date 02/06/2018
# Author  Uttam Singh Bhagaur

import time

print("Local Date and Time is : ")
x = time.localtime()
print("Date : %d/%d/%d Time : %d:%d:%d" %(x.tm_mday, x.tm_mon, x.tm_year, x.tm_hour, x.tm_min, x.tm_sec))
