#import associated tool
from airflow import DAG
from airflow.utils import timezone
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

#context manager
with DAG(
    "my_dag",
    start_date=timezone.datetime(2022, 10, 8),
    schedule = None, #"* * * * *", 
    tags=["workshop"],
):
    t1 = EmptyOperator(task_id="t1")

    echo_hello = BashOperator(
        task_id = "echo_hello",
        bash_command = "echo 'hello'",
    )

    def _print_hey():
        print("Hey!")

    print_hey = PythonOperator(
        task_id = "print_hey",
        python_callable = _print_hey,
    )

    t2 = EmptyOperator(task_id="t2")

#create dependecies
    #t1 >> echo_hello >> print_hey >> t2

    #t1 >> echo_hello
    #t1 >> print_hey
    #echo_hello >> t2
    #print_hey >> t2

    t1 >> [echo_hello, print_hey] >> t2