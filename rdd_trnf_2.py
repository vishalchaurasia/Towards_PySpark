import os

os.environ["PYSPARK_PYTHON"] = r"C:\Program Files\Python312\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Program Files\Python312\python.exe"

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("WorkerTest") \
    .getOrCreate()

sc = spark.sparkContext

rdd1 = sc.parallelize([1, 2, 3, 4, 5])
rdd2 = sc.parallelize([4,5,6,7])
result = rdd1.intersection(rdd2).collect()
print(result)