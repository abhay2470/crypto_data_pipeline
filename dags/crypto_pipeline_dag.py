from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    dag_id="crypto_data_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule ="@hourly",
    catchup=False
) as dag:

    fetch_crypto_task = BashOperator(
        task_id="fetch_crypto_data",
        bash_command="python /usr/local/airflow/dags/fetch_crypto_data.py"
    )

    fetch_crypto_task