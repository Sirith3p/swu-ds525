# Creating and Scheduling Data Pipelines

# Getting Started

```
$ cd 05-creating-and-scheduling-data-pipelines 
$ docker-compose up
```

# Access airflow
After installed dockker-compose file, Airflow UI can be accessed via port `8080`

## Create the data pipelines
Please see the process in this python source file: [etl](https://github.com/Sirith3p/swu-ds525/blob/0f8072eeb356467a29acdc03b56ecb8e55b342af/05-creating-and-scheduling-data-pipelines/dags/etl.py)

### The pipeline structure
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/image/proj5-2.jpg)

### Data model
![alt text](https://github.com/Sirith3p/swu-ds525/blob/0f8072eeb356467a29acdc03b56ecb8e55b342af/01-data-modeling-I/Project1_ER_diagram.jpg)

### Airflow Grid 
In this project, we assign that the process updates daily.
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/image/proj5-1.jpg)

## Results from the data pipeline
We can find the 4 tables which were created in Postgres.
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/image/proj5-3.jpg)

Each table was inserted the data as described data model and showed the examples as belows:

### Event table
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/image/proj5-4.jpg) 

### Actor table
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/image/proj5-5.jpg) 

### Repo table
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/image/proj5-7.jpg) 

### Org table
![alt text](https://github.com/Sirith3p/swu-ds525/blob/main/05-creating-and-scheduling-data-pipelines/image/proj5-6.jpg) 