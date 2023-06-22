import datetime
from datetime import datetime
import os.path
#import time
#import openpyxl

def folder_Exist():
    today = datetime.now()
    datetime_object = datetime.strptime(str(today.month), "%m")
    month_name = datetime_object.strftime("%b")
    file_Path='/Users/praveenbabu/Documents/python/Python/Automation/Practice/classeg/'+month_name
    isdir = os.path.isdir(file_Path)
    #print(isdir)  

    try:
        os.makedirs(f'/Users/praveenbabu/Documents/python/Python/Automation/Practice/classeg'+month_name)
    except FileExistsError:
        # directory already exists
        pass
folder_Exist()