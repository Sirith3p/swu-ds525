# Import library ที่เกี่ยวข้อง
import json
import glob
import os
import psycopg2
from typing import List

from airflow import DAG
from airflow.utils import timezone
from airflow.operators.python import PythonOperator
#from airflow.providers.postgres.hooks.postgres import PostgresHook

# กำหนด settings ในการเชื่อมต่อกับ Amazon Redshift
host = "redshift-cluster-capstone.cfzeqwb4b9xc.us-east-1.redshift.amazonaws.com"
dbname = "dev"
user = "awsuser"
password = "Capstone525"
port = "5439"
conn_str = f"host={host} dbname={dbname} user={user} password={password} port={port}"
conn = psycopg2.connect(conn_str)
cur = conn.cursor()

# Create create table function
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
            sales_outlet_type VARCHAR,
            store_address VARCHAR,
            store_city VARCHAR,
            store_state VARCHAR,
            store_postal_code VARCHAR,
            store_longitude VARCHAR,
            store_latitude VARCHAR
        )
    """

    #create the food_products table that consists of 7 columns and assign product_id as the primary key
    table_create_food_products = """
        CREATE TABLE IF NOT EXISTS food_products(
            product_id bigint NOT NULL,
            product_group VARCHAR,
            product_category VARCHAR,
            product_type VARCHAR,
            product VARCHAR,
            wholesale_price float,
            retail_price float
        )
    """
    #create the customers table that consists of 5 columns and assign customer_id as the primary key
    table_create_customers = """
        CREATE TABLE IF NOT EXISTS customers(
            customer_id bigint NOT NULL,
            loyalty_card_number VARCHAR,
            gender VARCHAR,
            birth_year VARCHAR,
            generation VARCHAR
        )
    """

    #create the pastry_sales table that consists of 8 columns and assign id as the primary key
    table_create_pastry_sales = """
        CREATE TABLE IF NOT EXISTS pastry_sales(
            product_id bigint,
            sales_outlet_id bigint,
            transaction_date VARCHAR,
            all_piece VARCHAR,
            sold_piece VARCHAR,
            waste VARCHAR,
            waste_prop VARCHAR
        )
    """

    #create the sales table that consists of 6 columns and assign sale_id as the primary key
    table_create_sales = """
        CREATE TABLE IF NOT EXISTS sales(
            sale_id bigint NOT NULL,
            sale_date VARCHAR,
            sale_time VARCHAR,
            sales_outlet_id bigint,
            customer_id bigint,
            product_id bigint
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

# Create copy table function เพื่อนำข้อมูลจาก cleaned zone เข้าสู่ datawarehouse
def _copy_tables():
    ##############################
    # Copy data from S3 to the table we created above
    # Copy data to retail table
    table_query_retails = """
    COPY retails FROM 's3://ds525-capstoneproject/cleaned/retail'
    ACCESS_KEY_ID 'ASIAQZBGVQQXWYMLYT3V'
    SECRET_ACCESS_KEY 'VtUUbnmkMXXXR0rTicV6CT996oIjWp48hDx84/uh'
    SESSION_TOKEN 'FwoGZXIvYXdzEDUaDKd1tbkV491m0Jf43SLJAT+xAGb9cre1/a0Y2Elev8mrMvJ3tzSZNYZm9NrLKZuZcfAK38IjMf2Q4tmhhbOGIwvNfB0cdR1spRWk5o7pfN/uwP0GwE/0/I9xzq4BE28a8l93eb/gBPxR2EzNFxXzL37LQ7Q6mEjcFfUhsBBPA8VFIatrI1R97sAanfzNS+8Pi0zCaMs7rtm4fj5YNe88fnhbARxTZ32IH096800Tp1KtqCMvzuzjJt9iHP6wqMOmlbixrX+/M/7tUE5htCyAbPH56wQw/yXZLCibn4GdBjItzGWGbpWE+Fa8RcAfSPsBGoZytLo+Xw/4/TZk9P8r+tenu/mQJMSiuTCy08Hw'
    CSV
    IGNOREHEADER 1
    REGION 'us-east-1'
    """

    # Copy data to food products table
    table_query_food_products="""
    COPY food_products FROM 's3://ds525-capstoneproject/cleaned/food'
    ACCESS_KEY_ID 'ASIAQZBGVQQXWYMLYT3V'
    SECRET_ACCESS_KEY 'VtUUbnmkMXXXR0rTicV6CT996oIjWp48hDx84/uh'
    SESSION_TOKEN 'FwoGZXIvYXdzEDUaDKd1tbkV491m0Jf43SLJAT+xAGb9cre1/a0Y2Elev8mrMvJ3tzSZNYZm9NrLKZuZcfAK38IjMf2Q4tmhhbOGIwvNfB0cdR1spRWk5o7pfN/uwP0GwE/0/I9xzq4BE28a8l93eb/gBPxR2EzNFxXzL37LQ7Q6mEjcFfUhsBBPA8VFIatrI1R97sAanfzNS+8Pi0zCaMs7rtm4fj5YNe88fnhbARxTZ32IH096800Tp1KtqCMvzuzjJt9iHP6wqMOmlbixrX+/M/7tUE5htCyAbPH56wQw/yXZLCibn4GdBjItzGWGbpWE+Fa8RcAfSPsBGoZytLo+Xw/4/TZk9P8r+tenu/mQJMSiuTCy08Hw'
    CSV
    IGNOREHEADER 1
    REGION 'us-east-1'
    """

    # Copy data to customers table
    table_query_customers="""
    COPY customers FROM 's3://ds525-capstoneproject/cleaned/customers'
    ACCESS_KEY_ID 'ASIAQZBGVQQXWYMLYT3V'
    SECRET_ACCESS_KEY 'VtUUbnmkMXXXR0rTicV6CT996oIjWp48hDx84/uh'
    SESSION_TOKEN 'FwoGZXIvYXdzEDUaDKd1tbkV491m0Jf43SLJAT+xAGb9cre1/a0Y2Elev8mrMvJ3tzSZNYZm9NrLKZuZcfAK38IjMf2Q4tmhhbOGIwvNfB0cdR1spRWk5o7pfN/uwP0GwE/0/I9xzq4BE28a8l93eb/gBPxR2EzNFxXzL37LQ7Q6mEjcFfUhsBBPA8VFIatrI1R97sAanfzNS+8Pi0zCaMs7rtm4fj5YNe88fnhbARxTZ32IH096800Tp1KtqCMvzuzjJt9iHP6wqMOmlbixrX+/M/7tUE5htCyAbPH56wQw/yXZLCibn4GdBjItzGWGbpWE+Fa8RcAfSPsBGoZytLo+Xw/4/TZk9P8r+tenu/mQJMSiuTCy08Hw'
    CSV
    IGNOREHEADER 1
    REGION 'us-east-1'
    """

    # Copy data to pastry sales table
    table_query_pastry_sales="""
    COPY pastry_sales FROM 's3://ds525-capstoneproject/cleaned/pastry_sales'
    ACCESS_KEY_ID 'ASIAQZBGVQQXWYMLYT3V'
    SECRET_ACCESS_KEY 'VtUUbnmkMXXXR0rTicV6CT996oIjWp48hDx84/uh'
    SESSION_TOKEN 'FwoGZXIvYXdzEDUaDKd1tbkV491m0Jf43SLJAT+xAGb9cre1/a0Y2Elev8mrMvJ3tzSZNYZm9NrLKZuZcfAK38IjMf2Q4tmhhbOGIwvNfB0cdR1spRWk5o7pfN/uwP0GwE/0/I9xzq4BE28a8l93eb/gBPxR2EzNFxXzL37LQ7Q6mEjcFfUhsBBPA8VFIatrI1R97sAanfzNS+8Pi0zCaMs7rtm4fj5YNe88fnhbARxTZ32IH096800Tp1KtqCMvzuzjJt9iHP6wqMOmlbixrX+/M/7tUE5htCyAbPH56wQw/yXZLCibn4GdBjItzGWGbpWE+Fa8RcAfSPsBGoZytLo+Xw/4/TZk9P8r+tenu/mQJMSiuTCy08Hw'
    CSV
    IGNOREHEADER 1
    REGION 'us-east-1'
    """

    # Copy data to sales table
    table_query_sales="""
    COPY sales FROM 's3://ds525-capstoneproject/cleaned/sales'
    ACCESS_KEY_ID 'ASIAQZBGVQQXWYMLYT3V'
    SECRET_ACCESS_KEY 'VtUUbnmkMXXXR0rTicV6CT996oIjWp48hDx84/uh'
    SESSION_TOKEN 'FwoGZXIvYXdzEDUaDKd1tbkV491m0Jf43SLJAT+xAGb9cre1/a0Y2Elev8mrMvJ3tzSZNYZm9NrLKZuZcfAK38IjMf2Q4tmhhbOGIwvNfB0cdR1spRWk5o7pfN/uwP0GwE/0/I9xzq4BE28a8l93eb/gBPxR2EzNFxXzL37LQ7Q6mEjcFfUhsBBPA8VFIatrI1R97sAanfzNS+8Pi0zCaMs7rtm4fj5YNe88fnhbARxTZ32IH096800Tp1KtqCMvzuzjJt9iHP6wqMOmlbixrX+/M/7tUE5htCyAbPH56wQw/yXZLCibn4GdBjItzGWGbpWE+Fa8RcAfSPsBGoZytLo+Xw/4/TZk9P8r+tenu/mQJMSiuTCy08Hw'
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

    #create task to get file from folder 'cleaned' in S3 
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

    #create process flow
    create_tables >> copy_tables

    #end