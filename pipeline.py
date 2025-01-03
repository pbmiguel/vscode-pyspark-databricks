from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, VectorAssembler

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("ProductInfoPipeline") \
    .getOrCreate()

# Create a mock DataFrame
data = [
    (1, "Laptop", 1200.0, "Electronics", 10),
    (2, "Phone", 800.0, "Electronics", 50),
    (3, "Table", 150.0, "Furniture", 20),
    (4, "Chair", 85.0, "Furniture", 30),
    (5, "Book", 20.0, "Stationery", 100)
]
columns = ["product_id", "product_name", "price", "category", "stock"]

mock_df = spark.createDataFrame(data, columns)

# Define StringIndexer for the 'category' column
category_indexer = StringIndexer(inputCol="category", outputCol="category_index")

# Define VectorAssembler to combine features into a single vector
vector_assembler = VectorAssembler(
    inputCols=["price", "stock", "category_index"], 
    outputCol="features"
)

# Create a pipeline
pipeline = Pipeline(stages=[category_indexer, vector_assembler])

# Fit the pipeline to the data
pipeline_model = pipeline.fit(mock_df)

# Transform the data using the pipeline
transformed_df = pipeline_model.transform(mock_df)

# Show the resulting DataFrame
transformed_df.select("product_id", "product_name", "features").show(truncate=False)

# Save Pipeline to disk
pipeline_model.write().overwrite().save("product_info_pipeline")

# Stop the SparkSession
spark.stop()
