import os

os.environ["PYSPARK_PYTHON"] = r"C:\Program Files\Python312\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = r"C:\Program Files\Python312\python.exe"

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("WorkerTest") \
    .getOrCreate()

sc = spark.sparkContext

print(sc.parallelize([1, 2, 3]).collect())

spark.stop()