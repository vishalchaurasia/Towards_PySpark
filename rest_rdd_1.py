from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RDD Practice") \
    .master("local[*]") \
    .getOrCreate()

sc = spark.sparkContext

rdd = sc.parallelize([1, 2, 3, 4, 5])

result = rdd.map(lambda x: x * 2).collect()

print(result)

spark.stop()