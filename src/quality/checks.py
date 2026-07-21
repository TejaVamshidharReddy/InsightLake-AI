from pyspark.sql import DataFrame

def assert_not_empty(df: DataFrame) -> None:
    if df.limit(1).count() == 0:
        raise ValueError("Data quality check failed: dataset is empty")
