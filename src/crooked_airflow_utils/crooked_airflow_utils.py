import sys
from airflow.operators.bash import BashOperator

def hello():
    print("hello")

def pong():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(f"{'p' * n}ing")
    else:
        print('ping')

def ping():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(f"{'p' * n}ong")
    else:
        print('pong')

def gen_bash_task(name: str, cmd: str, dag, trigger="all_success"):
    """airflow bash task 생성
        - trigger-rules : https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/dags.html#trigger-rules
    """
    bash_task = BashOperator(
        task_id=name,
        bash_command=cmd,
        trigger_rule=trigger,
        dag=dag
    )
    return bash_task

if __name__ == "__main__":
    ping()
    pong()
