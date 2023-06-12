import sys
import crooked_airflow_utils

def test_ping():
    sys.argv = ['foo', '10']
    crooked_airflow_utils.ping()

