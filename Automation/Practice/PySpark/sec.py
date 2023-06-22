#import pyspark
#from pyspark.sql import SQLContext
#from pyspark.sql import Row
from pyspark.sql import SQLContext
from pyspark import SparkContext
sc =SparkContext()
url = "https://raw.githubusercontent.com/guru99-edu/R-Programming/master/adult_data.csv"
from pyspark import SparkFiles
#sc=SQLContext()
sqlContext = SQLContext(sc)
sc.addFile(url)

df = sqlContext.read.csv(SparkFiles.get("adult_data.csv"), header=True, inferSchema= True)
#df.printSchema()
df.show(5, truncate = False)
