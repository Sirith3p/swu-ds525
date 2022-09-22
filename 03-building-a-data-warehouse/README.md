# Project 3: Building a Data Warehouse

# Getting Started

```
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

# Create Amazon Redshift Cluster 
## Configuration
```
Cluster configuration
- Cluster Name: 'redshift-cluster-1'
- Node type: 'ra3.xlplus'
- Number of nodes: 1

Database configuration
- Admin user name: 'awsuser'
- Admin user password: 'Ds525lab'

Associated IAM role: 'LabRole'

Additional configurations: As Default settings
```
![alt text](https://github.com/Sirith3p/swu-ds525/blob/41a77cd6f6cc060c045cb7f4fa94704c376d70c4/03-building-a-data-warehouse/image/Proj3_Redshift.jpg)

# Create Amazon S3 to store file
![alt text](https://github.com/Sirith3p/swu-ds525/blob/db36770d01218a637c92a5bbb9f3080be0e99077/03-building-a-data-warehouse/image/Proj3_S3.jpg)
In this bucket, two files were stored.
1. events_json_path.json
2. github_events_01.json

# Create etl.py to access Amazon Redshift for creating tables and loading data from S3 to Redshift
## Running ETL Scripts
```
python etl.py
```

## Data model
![alt text](https://github.com/Sirith3p/swu-ds525/blob/eae3cb34c811072c387ecb5561f4e75510f27d65/03-building-a-data-warehouse/image/Proj3_table.jpg)

## Tables after running etl script
Loading file from S3 to Redshift: [staging events table](https://github.com/Sirith3p/swu-ds525/blob/3037a4da201242f28410bc4be38f036ec8a142ee/03-building-a-data-warehouse/table/staging_events.csv)

Other tables which were inserted data from staging events table
- [Events](https://github.com/Sirith3p/swu-ds525/blob/d213b2e51d59f89321559dad21d087dd489c769c/03-building-a-data-warehouse/table/events.csv)
- [Actors](https://github.com/Sirith3p/swu-ds525/blob/d213b2e51d59f89321559dad21d087dd489c769c/03-building-a-data-warehouse/table/actors.csv)
- [Repo](https://github.com/Sirith3p/swu-ds525/blob/d213b2e51d59f89321559dad21d087dd489c769c/03-building-a-data-warehouse/table/repo.csv)
