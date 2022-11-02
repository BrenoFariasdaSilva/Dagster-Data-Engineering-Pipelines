from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="hooli_data_eng",
        packages=find_packages(exclude=["hooli_data_eng_tests"]),
        package_data={"hooli_data_eng": ["dbt_project/*"]},
        install_requires=[
            "dagster",
            "dagster-dbt",
            "pandas",
            "numpy",
            "scipy",
            "dbt-core",
            "dbt-duckdb",
            "dbt-snowflake", 
            "dagster-duckdb",
            "dagster-aws",
            "dagster-duckdb-pandas",
            "dagster-snowflake",
            "dagster-snowflake-pandas",
            "dagster-cloud",
            "dagster-pyspark",
            "dagster-databricks"
        ],
        extras_require={"dev": ["dagit", "pytest"]},
    )
