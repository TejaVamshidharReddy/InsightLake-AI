from pathlib import Path
from pyspark.sql import DataFrame, SparkSession

def load_csv(spark: SparkSession, path: str | Path) -> DataFrame:
    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(path))
    )
