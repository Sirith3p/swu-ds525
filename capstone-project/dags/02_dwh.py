import json
import glob
import os
import psycopg2
from typing import List

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.python import PythonOperator
#from airflow.providers.postgres.hooks.postgres import PostgresHook

host = "redshift-cluster-capstone.cfzeqwb4b9xc.us-east-1.redshift.amazonaws.com"
dbname = "dev"
user = "awsuser"
password = "Capstone525"
port = "5439"
conn_str = f"host={host} dbname={dbname} user={user} password={password} port={port}"
conn = psycopg2.connect(conn_str)
cur = conn.cursor()

def _create_tables():
    # Drop table if it exists
    drop_table_query = "DROP TABLE IF EXISTS retails, customers, food_products, pastry_sales, sales"
    cur.execute(drop_table_query)
    conn.commit()

    # Create table
    #create the retails table that consists of 8 columns and assign sales_outlet_id as the primary key
    table_create_retails = """
        CREATE TABLE IF NOT EXISTS retails(
            sales_outlet_id bigint NOT NULL,
            sales_outlet_type text,
            store_address text,
            store_city text,
            store_state text,
            store_postal_code text,
            store_longitude text,
            store_latitude text
        )
    """

    #create the food_products table that consists of 7 columns and assign product_id as the primary key
    table_create_food_products = """
        CREATE TABLE IF NOT EXISTS food_products(
            product_id bigint NOT NULL,
            product_group text,
            product_category text,
            product_type text,
            product text,
            wholesale_price float,
            retail_price float
        )
    """
    #create the customers table that consists of 5 columns and assign customer_id as the primary key
    table_create_customers = """
        CREATE TABLE IF NOT EXISTS customers(
            customer_id bigint NOT NULL,
            loyalty_card_number text,
            gender text,
            birth_year text,
            generation text
        )
    """

    #create the pastry_sales table that consists of 8 columns and assign id as the primary key
    table_create_pastry_sales = """
        CREATE TABLE IF NOT EXISTS pastry_sales(
            product_id bigint,
            sales_outlet_id bigint,
            transaction_date text,
            all_piece text,
            sold_piece text,
            waste text,
            waste_prop text
        )
    """

    #create the sales table that consists of 6 columns and assign sale_id as the primary key
    table_create_sales = """
        CREATE TABLE IF NOT EXISTS sales(
            sale_id bigint NOT NULL,
            product_id text,
            sales_outlet_id text,
            customer_id text,
            sale_date text,
            sale_time text
          )
    """

    create_table_queries = [
    table_create_retails,
    table_create_food_products,
    table_create_customers,
    table_create_pastry_sales,
    table_create_sales
    ]
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

def _copy_tables():
    ##############################
    # Copy data from S3 to the table we created above
    table_query_retails = """
    COPY retails FROM 's3://ds525-capstoneproject/cleaned/retail'
    ACCESS_KEY_ID 'ASIAQZBGVQQX232IGJ23'
    SECRET_ACCESS_KEY 'K4nGJkAgr4K3Ls9O9szJPaqDPwQSGF19ygy8J2tL'
    SESSION_TOKEN 'FwoGZXIvYXdzEAcaDKh+dEOsN1i/W3Z93yLJATM6I2zrPOJPvo53ykhZENen2007gKEbhk1/FCgEIBFZQLlLkX51agl82OsA/SxIDs1vlJi9MsNaAQ0tHCm8rMM3K/nI9lqX3R71yegYX1SNdb9AJeMcvlgyCrJFmzm7JhjxkzXPzGPa1cYjnb/I1wjDCgJSJW2paBJSBONTuPN2HcwynVkhKf0hVBksblf4XH+Kg8wadhJ5BIQhzubSxBpF9fgVQXNt3MsSSRZydjP794niinFr/ymwyrexzmartoQ4lIezXE5djSiYhfecBjItaTJyYDm5zDQXAG/pIbV+X6+0r4P4sqBWpy2x2XByGVFEJWRgLdU7KcJZwwgf'
    CSV
    IGNOREHEADER 1
    REGION 'us-east-1'
    """
    table_query_food_products="""
    COPY food_products FROM 's3://ds525-capstoneproject/cleaned/food'
    ACCESS_KEY_ID 'ASIAQZBGVQQX232IGJ23'
    SECRET_ACCESS_KEY 'K4nGJkAgr4K3Ls9O9szJPaqDPwQSGF19ygy8J2tL'
    SESSION_TOKEN 'FwoGZXIvYXdzEAcaDKh+dEOsN1i/W3Z93yLJATM6I2zrPOJPvo53ykhZENen2007gKEbhk1/FCgEIBFZQLlLkX51agl82OsA/SxIDs1vlJi9MsNaAQ0tHCm8rMM3K/nI9lqX3R71yegYX1SNdb9AJeMcvlgyCrJFmzm7JhjxkzXPzGPa1cYjnb/I1wjDCgJSJW2paBJSBONTuPN2HcwynVkhKf0hVBksblf4XH+Kg8wadhJ5BIQhzubSxBpF9fgVQXNt3MsSSRZydjP794niinFr/ymwyrexzmartoQ4lIezXE5djSiYhfecBjItaTJyYDm5zDQXAG/pIbV+X6+0r4P4sqBWpy2x2XByGVFEJWRgLdU7KcJZwwgf'
    CSV
    IGNOREHEADER 1
    REGION 'us-east-1'
    """
    table_query_customers="""
    COPY customers FROM 's3://ds525-capstoneproject/cleaned/customers'
    ACCESS_KEY_ID 'ASIAQZBGVQQX232IGJ23'
    SECRET_ACCESS_KEY 'K4nGJkAgr4K3Ls9O9szJPaqDPwQSGF19ygy8J2tL'
    SESSION_TOKEN 'FwoGZXIvYXdzEAcaDKh+dEOsN1i/W3Z93yLJATM6I2zrPOJPvo53ykhZENen2007gKEbhk1/FCgEIBFZQLlLkX51agl82OsA/SxIDs1vlJi9MsNaAQ0tHCm8rMM3K/nI9lqX3R71yegYX1SNdb9AJeMcvlgyCrJFmzm7JhjxkzXPzGPa1cYjnb/I1wjDCgJSJW2paBJSBONTuPN2HcwynVkhKf0hVBksblf4XH+Kg8wadhJ5BIQhzubSxBpF9fgVQXNt3MsSSRZydjP794niinFr/ymwyrexzmartoQ4lIezXE5djSiYhfecBjItaTJyYDm5zDQXAG/pIbV+X6+0r4P4sqBWpy2x2XByGVFEJWRgLdU7KcJZwwgf'
    CSV
    IGNOREHEADER 1
    REGION 'us-east-1'
    """
    table_query_pastry_sales="""
    COPY pastry_sales FROM 's3://ds525-capstoneproject/cleaned/pastry_sales'
    ACCESS_KEY_ID 'ASIAQZBGVQQX232IGJ23'
    SECRET_ACCESS_KEY 'K4nGJkAgr4K3Ls9O9szJPaqDPwQSGF19ygy8J2tL'
    SESSION_TOKEN 'FwoGZXIvYXdzEAcaDKh+dEOsN1i/W3Z93yLJATM6I2zrPOJPvo53ykhZENen2007gKEbhk1/FCgEIBFZQLlLkX51agl82OsA/SxIDs1vlJi9MsNaAQ0tHCm8rMM3K/nI9lqX3R71yegYX1SNdb9AJeMcvlgyCrJFmzm7JhjxkzXPzGPa1cYjnb/I1wjDCgJSJW2paBJSBONTuPN2HcwynVkhKf0hVBksblf4XH+Kg8wadhJ5BIQhzubSxBpF9fgVQXNt3MsSSRZydjP794niinFr/ymwyrexzmartoQ4lIezXE5djSiYhfecBjItaTJyYDm5zDQXAG/pIbV+X6+0r4P4sqBWpy2x2XByGVFEJWRgLdU7KcJZwwgf'
    CSV
    IGNOREHEADER 1
    REGION 'us-east-1'
    """
    table_query_sales="""
    COPY sales FROM 's3://ds525-capstoneproject/cleaned/sales'
    ACCESS_KEY_ID 'ASIAQZBGVQQX232IGJ23'
    SECRET_ACCESS_KEY 'K4nGJkAgr4K3Ls9O9szJPaqDPwQSGF19ygy8J2tL'
    SESSION_TOKEN 'FwoGZXIvYXdzEAcaDKh+dEOsN1i/W3Z93yLJATM6I2zrPOJPvo53ykhZENen2007gKEbhk1/FCgEIBFZQLlLkX51agl82OsA/SxIDs1vlJi9MsNaAQ0tHCm8rMM3K/nI9lqX3R71yegYX1SNdb9AJeMcvlgyCrJFmzm7JhjxkzXPzGPa1cYjnb/I1wjDCgJSJW2paBJSBONTuPN2HcwynVkhKf0hVBksblf4XH+Kg8wadhJ5BIQhzubSxBpF9fgVQXNt3MsSSRZydjP794niinFr/ymwyrexzmartoQ4lIezXE5djSiYhfecBjItaTJyYDm5zDQXAG/pIbV+X6+0r4P4sqBWpy2x2XByGVFEJWRgLdU7KcJZwwgf'
    CSV
    IGNOREHEADER 1
    REGION 'us-east-1'
    """

    copy_table_query = [table_query_retails,
    table_query_food_products,
    table_query_customers,
    table_query_pastry_sales,
    table_query_sales]
    for query2 in copy_table_query:
        cur.execute(query2)
        conn.commit()


#create DAG in airflow 
with DAG(
    #name of DAG
    "capstone_project",
    #assign the start date, scheduling and tags
    start_date=timezone.datetime(2022, 12, 17),
    schedule="@daily",
    tags=["capstone","DS525"],
    catchup=False,
) as dag:

    #create task to get file from folder 'data' 
    copy_tables = PythonOperator(
        task_id="copy_tables",
        python_callable=_copy_tables,
        #op_kwargs={
           # "filepath": "/opt/airflow/dags/data",
        #}
    )

    #create task to create table from function '_create_tables'
    create_tables = PythonOperator(
        task_id="create_tables",
        python_callable=_create_tables,
    )

    #create task to insert data into table from function '_process'
    #process = PythonOperator(
    #    task_id="process",
    #    python_callable=_process,
    #)
    
    #create process flow
    create_tables >> copy_tables

    #end