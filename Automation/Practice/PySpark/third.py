# Import all from `sql.types`
from pyspark.sql.types import *
from pyspark.ml.feature import StringIndexer

# Write a custom function to convert the data type of DataFrame columns
def convertColumn(df, names, newType):
    for name in names: 
        df = df.withColumn(name, df[name].cast(newType))
    return df 
# List of continuous features
CONTI_FEATURES  = ['age', 'fnlwgt','capital_gain', 'education_num', 'capital_loss', 'hours_week']
# Convert the type
df_string = convertColumn(df_string, CONTI_FEATURES, FloatType())
df.select('age','fnlwgt').show(5)
