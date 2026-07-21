# Architecture

## Data Layers

- **Bronze:** Raw data copied from source systems.
- **Silver:** Cleaned, typed, deduplicated, and validated datasets.
- **Gold:** Business-ready analytical models.

## Planned Components

1. Source ingestion from CSV and REST APIs
2. AWS S3 storage
3. Spark processing
4. Delta Lake tables
5. Airflow orchestration
6. dbt transformations
7. FastAPI serving layer
8. AI assistant with governed access to curated data
