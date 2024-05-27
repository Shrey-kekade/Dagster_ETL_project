from NCHS_operations import *
from dagster import job

# Creating the dagster job which will execute the operations written in NCHS_operations.py. 
# Hierarchical operations written below ensure the sequential execution of the pipeline.

@job
def etl():
    visualize(
        fetch_data_from_postgresql(
            load_data_into_postgresql(
                transform_data(
                    extract_data_from_mongodb(
                        load_data_to_mongodb()
                    ) 
                )
            )
        )
    )    