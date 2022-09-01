# Getting Started

```
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

# Prerequisite when install psycopg2 package
## For Debian/Ubuntu users:

```
sudo apt install -y libpq-dev
```

# Running Postgres
```
docker-compose up
```

# Running ETL Scripts
```
python create_tables.py
python etl.py
```

# E-R Diagram 
![alt text](https://github.com/Sirith3p/swu-ds525/blob/a5a783b799ea710a42c0867e95a4053e348c0d88/01-data-modeling-I/Project1_ER_diagram.jpg)
