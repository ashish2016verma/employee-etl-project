from pyspark.sql import SparkSession
from pyspark.sql.functions import col,when
spark = SparkSession.builder.getOrCreate()
df = spark.table("ibm_watson1.stage.employee_stage")

df = df.withColumn(
    "annual_salary",
    col("salary") * 12
)
df = df.withColumn(
    "bonus",
    when(col("department") == "Sales", col("annual_salary") * 0.1).otherwise(col("annual_salary") * 0.05)
)
df = df.withColumn(
    "grade"
    ,when(col("bonus") >= 100000, "A")
    .when(col("bonus") >= 50000, "B")
    .when(col("bonus") >= 25000, "C")
    .otherwise("D")
)

df.write\
    .format("delta")\
    .option("overwriteSchema", "true")\
    .mode("overwrite")\
    .saveAsTable("ibm_watson1.main.employee_main")
print("Succesfully created main table")



