from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

df = spark.read.option("header", True).csv("/FileStore/employee.csv")

df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("employee_raw")

print("Employee Raw Table Loaded Successfully")