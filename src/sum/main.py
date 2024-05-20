from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Sum of Series") \
    .getOrCreate()

rdd = spark.sparkContext.parallelize(range(1, 100))

print("Series sum =", rdd.sum())
spark.stop()
