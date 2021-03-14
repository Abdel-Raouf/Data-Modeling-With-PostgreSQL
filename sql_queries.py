# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
# user is a reserved word in postgres, so we make it users to work properly
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS song"
artist_table_drop = "DROP TABLE IF EXISTS artist"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

# Fact table
songplay_table_create = (
    "CREATE TABLE IF NOT EXISTS songplays(songplay_id SERIAL PRIMARY KEY, start_time BIGINT, user_id INT, level VARCHAR, song_id VARCHAR, \
                                        artist_id VARCHAR, session_id INT, location VARCHAR, user_agent VARCHAR)")

# dimesnion table
user_table_create = ("CREATE TABLE IF NOT EXISTS users(user_id INT PRIMARY KEY, first_name VARCHAR NOT NULL, last_name VARCHAR NOT NULL, \
                    gender VARCHAR, level VARCHAR)")
# dimension table
song_table_create = ("CREATE TABLE IF NOT EXISTS songs(song_id VARCHAR PRIMARY KEY, title VARCHAR NOT NULL, artist_id VARCHAR NOT NULL, \
                    year INT, duration FLOAT NOT NULL)")
# dimension table
artist_table_create = ("CREATE TABLE IF NOT EXISTS artists(artist_id VARCHAR NOT NULL PRIMARY KEY, name VARCHAR NOT NULL, location VARCHAR, \
                        longitude FLOAT, latitude FLOAT)")
# dimension table
time_table_create = ("CREATE TABLE IF NOT EXISTS time(start_time TIMESTAMP PRIMARY KEY, hour INT, day INT, week_of_year INT, month INT, \
                    year INT, week_day INT)")

# INSERT RECORDS

songplay_table_insert = (
    "INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) \
        VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s) \
            ON CONFLICT (songplay_id) DO NOTHING")

user_table_insert = (
    "INSERT INTO users (user_id, first_name, last_name, gender, level) \
        VALUES (%s, %s, %s, %s, %s) \
        ON CONFLICT (user_id) DO NOTHING")

song_table_insert = (
    "INSERT INTO songs (song_id, title, artist_id, year, duration) \
        VALUES (%s, %s, %s, %s, %s) \
        ON CONFLICT (song_id) DO NOTHING")

artist_table_insert = (
    "INSERT INTO artists (artist_id, name, location, longitude, latitude) \
        VALUES (%s, %s, %s, %s, %s) \
        ON CONFLICT (artist_id) DO NOTHING")


time_table_insert = (
    "INSERT INTO time (start_time, hour, day, week_of_year, month, year, week_day) \
        VALUES(%s, %s, %s, %s, %s, %s, %s) \
        ON CONFLICT (start_time) DO NOTHING")

# FIND SONGS
song_select = ("SELECT songs.song_id, artists.artist_id FROM (songs JOIN artists ON songs.artist_id=artists.artist_id) \
                WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create,
                        song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop,
                      song_table_drop, artist_table_drop, time_table_drop]
