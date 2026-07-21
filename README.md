# InsightLake AI

An end-to-end modern data platform that ingests raw business data, transforms it with Apache Spark, stores curated datasets in a lakehouse, and exposes analytics and AI-assisted insights through an API.

## Architecture

```text
Raw CSV / API
      |
      v
AWS S3 (Bronze)
      |
      v
Apache Spark / Databricks
      |
      v
Delta Lake (Silver & Gold)
      |
      +--> dbt analytics models
      |
      +--> FastAPI service
      |
      +--> AI assistant for governed data questions
```

## Planned Technology Stack

- Python
- Apache Spark / PySpark
- Databricks
- Delta Lake
- AWS S3
- Apache Airflow
- dbt
- FastAPI
- Docker
- Terraform
- GitHub Actions

## Repository Structure

```text
InsightLake-AI/
├── .github/workflows/
├── airflow/dags/
├── api/
├── data/sample/
├── dbt/
├── docs/
├── notebooks/
├── src/
│   ├── ingestion/
│   ├── transformations/
│   └── quality/
├── terraform/
├── tests/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── Makefile
├── pyproject.toml
└── requirements.txt
```

## Current Status

This repository contains the initial production-style project structure. Implementation will be added incrementally through documented milestones.

## Roadmap

- [ ] Create sample retail dataset
- [ ] Build bronze ingestion pipeline
- [ ] Add silver transformations
- [ ] Create gold analytics tables
- [ ] Add data-quality checks
- [ ] Add Airflow orchestration
- [ ] Add FastAPI endpoints
- [ ] Add AI-assisted analytics
- [ ] Add Terraform infrastructure
- [ ] Add CI/CD workflow
- [ ] Add architecture diagram and screenshots

## Local Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

## Author

**Teja Vamshi**  
Data Engineer focused on modern cloud data platforms, lakehouse architecture, and AI-enabled analytics.
