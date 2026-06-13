from pyspark.sql import SparkSession

# Create Spark Session
spark = SparkSession.builder \
    .appName("RDD_Test") \
    .master("local[*]") \
    .getOrCreate()

# Get Spark Context
sc = spark.sparkContext

# Create RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# Action
print("RDD Elements:", rdd.collect())

spark.stop()