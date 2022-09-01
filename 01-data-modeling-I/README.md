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
