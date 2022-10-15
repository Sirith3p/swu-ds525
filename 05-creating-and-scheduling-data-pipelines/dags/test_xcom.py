#import associated tool
from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator

def _push(**context):
    ti = context["ti"]
    ti.xcom_push(key="name", value="SG")

def _pull(**context):
    ti = context["ti"]
    name = ti.xcom_pull(task_ids="push", key="name")
    print(f"Hello!! {name}")

#context manager
with DAG(
    "test_xcom",
    start_date=timezone.datetime(2022, 10, 15),
    schedule = "*/30 * * * *", 
    tags=["workshop"],
    catchup=False,
) as dag:

    push = PythonOperator(
        task_id="push",
        python_callable=_push,
    )

    
    pull = PythonOperator(
        task_id="pull",
        python_callable=_pull,
    )

    push >> pull