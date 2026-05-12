# Real-Time Crypto Data Pipeline

## Project Overview
Built a real-time cryptocurrency data pipeline using Python, AWS S3, Apache Airflow, and Streamlit.

## Tech Stack
- Python
- REST API
- Pandas
- AWS S3
- Apache Airflow
- Docker
- Streamlit

## Features
- Real-time crypto API ingestion
- Automated workflow orchestration using Airflow DAGs
- Cloud storage with AWS S3
- Interactive Streamlit dashboard
- Automated CSV generation

## Project Architecture

API → Python → CSV → Airflow → AWS S3 → Streamlit Dashboard

## Run Project

```bash
astro dev start
streamlit run streamlit_app.py

---

# Step 3 — Initialize Git

Open terminal in project root:

```powershell id="0x7k5n"
git init