# Purpose:
putting into practice the following concepts:
- Data modeling (Applying Conceptual Modeling, then Construct Fact and Dimension Tables).
- Database Schema (Apply a specific schema to Fact and Dimension Tables, which suits our Data-Size and Structure => Star-Schema).
- ETL Pipeline (Construct an ETL Pipeline to Transfer Data From Log Files To Database Tables).
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
# Database Schema:
The schema used for this project is the *Star Schema*: There is one main fact table containing all the measures associated with each event songplays, and 4-dimensional tables songs, artists, users and time, each with a primary key that is being referenced from the fact table.
![App_Look](https://github.com/Abdel-Raouf/Data-Modeling-With-PostgreSQL/blob/main/images/Star-Schema.png)

# Data Model Selection:
We used a Database based on the Relational Data-Model (PostgreSQL), Due to:
- The data types are structured (we know before-hand the structure of the jsons we need to analyze, and where and how to extract and transform each field).
- The amount of data we need to analyze is not Very big.
- This structure will enable the analysts to aggregate the data efficiently.
- Using Joins will give the flexibility to analysts, while querying the Data. 

# Project Structure:
1. **data folder**, where all needed jsons reside.
2. **sql_queries.py** contains all your SQL queries, and is imported into the files bellow.
3. **create_tables.py** drops and creates tables. You run this file to reset your tables before each time you run your ETL scripts.
4. **etl.py** reads and processes files from song_data and log_data and loads them into your tables.
5. **etl.ipynb** reads and processes a single file from song_data and log_data and loads the data into your tables.
6. **etl.py** reads and processes files from song_data and log_data and loads them into your tables.

# Data Processing And Quality Checks
Data is extracted from two types of JSON source files: 
- **songs** data is a subset from the [Million Song Dataset](http://millionsongdataset.com/).
- **users** data generated using [event simulator](https://github.com/Interana/eventsim) Based on the songs dataset. 

The JSON files are read into pandas dataframes, processed and uploaded into the database using psycopg2.

A number of steps clean the data and reduce the size of the database by removing data not needed for the analysis:

  - *Songplays* are identified by filtering for actions initiated from the 'NextSong' page.
  - *Timestamps* are converted from UNIX time to TimeStamp format.

# How to Run:
1. Run **create_tables.py** from terminal to set up the database and tables.
2. Run **etl.py** from terminal to process and load data into the database.
3. Launch **test.ipynb** to run validation and example queries.
