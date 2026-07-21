from datetime import datetime
from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="insightlake_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["insightlake", "data-engineering"],
) as dag:
    start = EmptyOperator(task_id="start")
    ingest = EmptyOperator(task_id="ingest_bronze")
    transform = EmptyOperator(task_id="transform_silver")
    publish = EmptyOperator(task_id="publish_gold")
    finish = EmptyOperator(task_id="finish")

    start >> ingest >> transform >> publish >> finish
