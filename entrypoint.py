# Import PySpark SQL functions and types
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Initialize a SparkSession
spark = SparkSession.builder \
    .appName("Mock PySpark DataFrame") \
    .getOrCreate()

# Define a schema for the DataFrame
schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True),
    StructField("city", StringType(), True)
])

# List of sample data matching the schema
data = [
    (1, "Alice", 30, "New York"),
    (2, "Bob", 25, "San Francisco"),
    (3, "Charlie", 35, "Los Angeles"),
    (4, "David", 29, "Chicago"),
(5, "Eve", 22, "Houston")
]

# Create a DataFrame using the schema and sample data
df = spark.createDataFrame(data, schema)

# Show the DataFrame
df.show()