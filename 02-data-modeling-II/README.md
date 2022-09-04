# Getting Started

```
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

# Running Cassandra
```
docker-compose up
```

# Running ETL Scripts
```
python etl.py
```

# Data Model
![alt text](https://github.com/Sirith3p/swu-ds525/blob/a5a783b799ea710a42c0867e95a4053e348c0d88/02-data-modeling-II/Project2_table.png)

# Examples of query from events table
```
query PushEvent
Row(actor_id='106313266', created_at=datetime.datetime(2022, 8, 17, 15, 55, 5), actor='kenobiwins', id='23488014712', public=True, type='PushEvent')
Row(actor_id='94136524', created_at=datetime.datetime(2022, 8, 17, 15, 52, 40), actor='Sidalvik', id='23487963448', public=True, type='PushEvent')
Row(actor_id='106591964', created_at=datetime.datetime(2022, 8, 17, 15, 54, 45), actor='kunedev', id='23488007824', public=True, type='PushEvent')
Row(actor_id='37953029', created_at=datetime.datetime(2022, 8, 17, 15, 52, 40), actor='BadProfessor', id='23487963492', public=True, type='PushEvent')
Row(actor_id='47776594', created_at=datetime.datetime(2022, 8, 17, 15, 55, 5), actor='baileys-li', id='23488014647', public=True, type='PushEvent')
Row(actor_id='46447321', created_at=datetime.datetime(2022, 8, 17, 15, 51, 5), actor='allcontributors[bot]', id='23487929588', public=True, type='PushEvent')
Row(actor_id='5146167', created_at=datetime.datetime(2022, 8, 17, 15, 51, 5), actor='markbush', id='23487929536', public=True, type='PushEvent')
Row(actor_id='101674460', created_at=datetime.datetime(2022, 8, 17, 15, 53, 42), actor='EliOceanak', id='23487985289', public=True, type='PushEvent')
```

# Examples of query from actors table
```
query number of events by each actor if number of event more than 1
Row(actor_id='77382887', actor='by-d-sign', number_events=2)
Row(actor_id='41898282', actor='github-actions[bot]', number_events=3)
Row(actor_id='55003092', actor='xsidc', number_events=2)
Row(actor_id='60316309', actor='Gabe616', number_events=2)
Row(actor_id='686971', actor='khurtwilliams', number_events=2)
Row(actor_id='53189160', actor='ausmoons', number_events=4)
Row(actor_id='111345762', actor='wwwuuid2com28', number_events=2)
Row(actor_id='8517910', actor='LombiqBot', number_events=2)
Row(actor_id='100631798', actor='simonkernel', number_events=2)
Row(actor_id='13384921', actor='ThatSpaceGuy', number_events=2)
```
