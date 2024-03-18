import os
from datetime import datetime
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import PostgresUserPasswordProfileMapping

profile_config = ProfileConfig(
    profile_name="jaffle_shop",
    target_name="dev",
    profile_mapping=PostgresUserPasswordProfileMapping(
        conn_id="postgres",
        profile_args={"schema": "public"},
    ),
)

dag_dbt_jaffle_shop = DbtDag(
    project_config=ProjectConfig(
        "/usr/local/airflow/dags/dbt/jaffle_shop/",
    ),
    profile_config=profile_config,
    execution_config=ExecutionConfig(
        dbt_executable_path=f"{os.environ['AIRFLOW_HOME']}/dbt_venv/bin/dbt",
    ),
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dag_id="DBT-Jaffle-Shop",
    default_args={"retries": 2},
)
