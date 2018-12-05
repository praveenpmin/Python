import pandas as pd

pd.set_option("display.max_rows", 5)
melbourne_file_path="C:\\Users\\ITPeople\\code\\Python\\ML\\melb_data.csv"
reviews = pd.read_csv("C:\\Users\\ITPeople\\code\\Python\\ML\\melb_data.csv")
melbourne_data=pd.read_csv(melbourne_file_path) 
# print(melbourne_data.columns)
# print(melbourne_data.head(2))
# print(melbourne_data)
print((reviews.Rooms == 3) & (reviews.Type == 'h'))
# print(reviews.Type == "h")
print(melbourne_data.describe())