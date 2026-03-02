#hiii
from pyspark.sql import SparkSession, functions as F
spark = SparkSession.builder.getOrCreate()
spark.read.csv("data.csv", header=True, inferSchema=True).withColumn("total", F.col("a")+F.col("b")).filter(F.col("total")>0).write.csv("out.csv", header=True, mode="overwrite")
