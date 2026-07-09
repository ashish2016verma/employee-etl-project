from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

raw_df = spark.table("ibm_watson1.raw.employee_raw")
stage_df = spark.table("ibm_watson1.stage.employee_stage")

print("="*50)
print("RAW LAYER VALIDATION")
print("="*50)

print(f"Raw Count        : {raw_df.count()}")
print(f"Stage Count      : {stage_df.count()}")

print(f"Raw Duplicate Count : {raw_df.count() - raw_df.dropDuplicates().count()}")

print(f"Stage Null Salary : {stage_df.filter(col('salary').isNull()).count()}")

print(f"Stage Null Email  : {stage_df.filter(col('email').isNull()).count()}")

print("="*50)