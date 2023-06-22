import calendar
import datetime
from datetime import datetime
import os.path

today = datetime.now()
  
#print("Current Date and Time :", today)
print("Current Month :", today.month)
datetime_object = datetime.strptime(str(today.month), "%m")
month_name = datetime_object.strftime("%b")
print("Short name: ",month_name)
#for x in range(1,13):
    #datetime_object = datetime.datetime.strptime(x, "%m")
    #month_name = datetime_object.strftime("%b")
    #print("Short name: ",month_name)
#    print(x, ":", calendar.month_abbr[x], "-", calendar.month_name[x])
file_Path='/Users/praveenbabu/Documents/python/Python/Automation/Practice/'+month_name
isdir = os.path.isdir(file_Path)
print(isdir)  

try:
    os.makedirs(f'/Users/praveenbabu/Documents/python/Python/Automation/Practice/'+month_name)
except FileExistsError:
    # directory already exists
    pass