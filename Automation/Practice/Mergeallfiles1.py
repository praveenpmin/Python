# importing the required modules
import glob
import pandas as pd
import datetime
import os
from datetime import datetime

today = datetime.now()
datetime_object = datetime.strptime(str(today.month), "%m")
month_name = datetime_object.strftime("%b")
 
# specifying the path to csv files
#path = '/Users/praveenbabu/Documents/python/Python/Automation/Practice/'+month_name
#path = '/Users/praveenbabu/Documents/python/Python/Automation/Practice/Apr'
path = '/Users/praveenbabu/Documents/python/Python/Automation/Practice/AllStocks/Mon'
#print(path)
 
# csv files in the path
file_list = glob.glob(path + "/*.xlsx")
 
# list of excel files we want to merge.
# pd.read_excel(file_path) reads the 
# excel data into pandas dataframe.
excl_list = []
 
for file in file_list:
    excl_list.append(pd.read_excel(file))
 
# concatenate all DataFrames in the list
# into a single DataFrame, returns new
# DataFrame.
excl_merged = pd.concat(excl_list, ignore_index=True)
 
# exports the dataframe into excel file
# with specified name.
#excl_merged.to_excel(path+'/All_' + month_name +'_Stocks.xlsx', index=False)
excl_merged.to_excel(path+'/All_Stocks.xlsx', index=False)