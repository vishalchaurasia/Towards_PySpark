# #map(func) — 1-to-1 transformation
# #Applies a function to every element in the RDD. Each input element produces exactly one output element. Great for transforming values.

# from pyspark.sql import SparkSession
# # sc = SparkSession.builder
# # .master("local[*]") \
# # .appName("RDD Practice") \
# # getOrCreate().sparkContext
# spark = SparkSession.builder \
#     .appName("RDD_Test") \
#     .master("local[*]") \
#     .getOrCreate()
# sc = spark.sparkContext
# rdd = sc.parallelize([11,22,33,44,55])
# result = rdd.map(lambda x: x / 0.5).collect()
# print(result)


  #######################CHATGPT###########################
# import os
# HARSHADAAAAAAAAAAAAAAAAAAAAAAAA
# # os.environ["PYSPARK_PYTHON"] = r"C:\Users\Harshada\venv\Scripts\python.exe"
# # os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Users\Harshada\venv\Scripts\python.exe"

# import sys
# print("Python executable:", sys.executable)

# from pyspark.sql import SparkSession

# spark = SparkSession.builder \
#     .appName("RDD_Test") \
#     .master("local[*]") \
#     .getOrCreate()

# sc = spark.sparkContext

#VISHALLLLLLLLLLLLLLLLLLLLLLLLLLLL
import os

os.environ["PYSPARK_PYTHON"] = r"C:\Program Files\Python312\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Program Files\Python312\python.exe"

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("WorkerTest") \
    .getOrCreate()

sc = spark.sparkContext

# rdd = sc.parallelize([11,22,33,44,55])

# result = rdd.map(lambda x: x / 0.5).collect()

# print(result)



############################flat map()###########################
#flatMap(func) — 1-to-many transformation
#Key difference from map(): map() would give [['hello','world'], ['pyspark','is','fun']] — a list of lists. flatMap() flattens it into one list.

# rdd = sc.parallelize(["barf giri ho vadiiii mein", "unn mein lipti simti hui", "aur hassi teri gunje", "hehehehe"])
# ganna = rdd.flatMap(lambda x: x.split(" ")).collect()
# print(ganna)

############################filter(func) — keep matching elements###########################
#Keeps only the elements for which the function returns True. Think of it like a WHERE clause in SQL.


#########################union(other) — combine two RDDs########################
#Returns a new RDD that contains all elements from both RDDs. Duplicates are allowed — this is a bag union, not a set union.

# rdd1 = sc.parallelize([1, 2, 3, 4, 5])
# rdd2 = sc.parallelize([4,5,6,7])
# result = rdd1.union(rdd2).collect()
# print(result)


############################intersection(other) — common elements only###########################
#Returns a new RDD containing only the elements found in both RDDs. Like SQL INTERSECT. Automatically removes duplicates.

rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize([4,5,6,7])
result = rdd1.intersection(rdd2).collect()
print(result)