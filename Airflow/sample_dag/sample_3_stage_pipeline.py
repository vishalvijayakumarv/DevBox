from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Define functions for each stage
def download(**kwargs):
    print("Stage 1: Downloading the file...")

def extract(**kwargs):
    print("Stage 2: Extracting the contents...")

def upload(**kwargs):
    print("Stage 3: Uploading the file...")

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
}

# Create the DAG
with DAG(
    dag_id='sample_3_stage_pipeline',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
    description='A 3-stage DAG: download, extract, upload',
) as dag:

    # Define tasks
    download_task = PythonOperator(
        task_id='download',
        python_callable=download,
    )

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract,
    )

    upload_task = PythonOperator(
        task_id='upload',
        python_callable=upload,
    )

    # Set task dependencies
    download_task >> extract_task >> upload_task
