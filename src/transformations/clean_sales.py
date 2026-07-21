from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def clean_sales(df: DataFrame) -> DataFrame:
    return (
        df.dropDuplicates()
        .withColumn("quantity", F.col("quantity").cast("integer"))
        .withColumn("unit_price", F.col("unit_price").cast("double"))
        .withColumn("sales_amount", F.col("quantity") * F.col("unit_price"))
    )
