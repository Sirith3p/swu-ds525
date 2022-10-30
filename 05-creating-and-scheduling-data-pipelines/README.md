# Creating and Scheduling Data Pipelines

# Getting Started

```
$ cd 05-creating-and-scheduling-data-pipelines 
$ docker-compose up
```

# Access airflow
After installed dockker-compose file, Airflow UI can be accessed via port `8080`

## Create the data pipelines
Please see the process in this python source file: [Source code etl_proj5.py](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/dags/etl_proj5.py)

### The pipeline structure
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/images/proj5-2.png)

### Data model
![alt text](https://github.com/Sirith3p/swu-ds525/blob/0f8072eeb356467a29acdc03b56ecb8e55b342af/01-data-modeling-I/Project1_ER_diagram.jpg)

### Airflow Grid 
In this project, we assign that the process updates daily.
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/images/proj5-1.png)

## Results from the data pipeline
We can find the 4 tables which were created in Postgres.
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/images/proj5-3.png)

Each table was inserted the data as described data model and showed the examples as belows:

### Event table
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/images/proj5-4.png) 

### Actor table
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/images/proj5-5.png) 

### Repo table
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/images/proj5-7.png) 

### Org table
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/images/proj5-6.png) 