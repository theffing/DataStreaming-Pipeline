from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

# https://youtu.be/GqAcTrqKcrY?si=7Y5gIB91J3XlSXyG

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2025, 11, 14, 3, 00)
}

def get_data():
    import json
    import requests
    
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]

    return res

def stream_data():
    import json

def format_data(res):
    data = {}


with DAG('user_automation', 
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )
