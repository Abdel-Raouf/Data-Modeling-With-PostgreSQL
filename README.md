# Target:
putting into practice the following concepts:
- Data modeling (Applying Conceptual Modeling, then Construct Fact and Dimension Tables)
- Database Schema (Apply a specific schema to Fact and Dimension Tables, which suits our Data-Size and Structure => Star-Schema)
- ETL Pipeline (Construct an ETL Pipeline to Transfer Data From Log Files To Database Tables)
# Project Description:
The objective of this project is to create SQL analytics database for a fictional music streaming service called Sparkify. Sparkify's analytics team seeks to understand what, when and how users are playing songs on the company's music app. The analysts need an easy way to query and analyze the data, which is currently locally stored in raw JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app on.

As the data engineer assigned to the project, my role is to create a Postgres database with tables designed to optimize queries on song play analysis. By construct a Database schema and an ETL Pipeline for this analysis.
# Data-Sample:
- **Song Datasets**: all json files are nested in subdirectories under /data/song_data. A sample of this files is:
```
{"num_songs": 1, "artist_id": "ARD7TVE1187B99BFB1", "artist_latitude": null, "artist_longitude": null, "artist_location": "California - LA", "artist_name": "Casual", "song_id": "SOMZWCG12A8C13C480", "title": "I Didn't Mean To", "duration": 218.93179, "year": 0}
```
- **Log Datasets**: all json files are nested in subdirectories under /data/log_data. A sample of a single row of each files is:
```
{"artist":null,"auth":"Logged In","firstName":"Kaylee","gender":"F","itemInSession":0,"lastName":"Summers","length":null,"level":"free","location":"Phoenix-Mesa-Scottsdale, AZ","method":"GET","page":"Home","registration":1540344794796.0,"sessionId":139,"song":null,"status":200,"ts":1541106106796,"userAgent":"\"Mozilla\/5.0 (Windows NT 6.1; WOW64) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/35.0.1916.153 Safari\/537.36\"","userId":"8"}
```
