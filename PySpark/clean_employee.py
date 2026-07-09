from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, when

spark = SparkSession.builder.getOrCreate()

# Read data from Raw layer
df = spark.table("ibm_watson1.raw.employee_raw")

# Remove duplicate records
df = df.dropDuplicates()

# Trim string columns
df = df.withColumn("name", trim(col("name"))) \
       .withColumn("department", trim(col("department"))) \
       .withColumn("city", trim(col("city"))) \
       .withColumn("email", trim(col("email")))

# Replace NULL salary with 0
df = df.withColumn(
    "salary",
    when(col("salary").isNull(), 0).otherwise(col("salary"))
)

# Replace NULL email
df = df.withColumn(
    "email",
    when(col("email").isNull(), "Not Available").otherwise(col("email"))
)

# Write to Stage
df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("ibm_watson1.stage.employee_stage")

print("Stage table loaded successfully")