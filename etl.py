import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *
import numpy
from psycopg2.extensions import register_adapter, AsIs


# converting from numpy.Int64 to regular integer, to be able to insert into postgres table
def addapt_numpy_int64(numpy_int64):
    return AsIs(numpy_int64)


def process_song_file(cur, filepath):
    # open song file
    # important to put 'lines=True' as the second argument, to tell pandas to read the json file as a line separated json.
    df = pd.read_json(filepath, lines=True)

    # insert song records
    songs_df = df[['song_id', 'title', 'artist_id',
                   'year', 'duration']]
    song_data = songs_df.values[0].tolist()

    cur.execute(song_table_insert, song_data)

    # insert artist record
    artists_df = df[['artist_id', 'artist_name',
                     'artist_location', 'artist_longitude', 'artist_latitude']]
    artist_data = artists_df.values[0].tolist()
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[(df.page == 'NextSong')]

    # convert timestamp column to datetime
    ts_to_dt = pd.to_datetime(df['ts'])

    # insert time data records
    time_data = [ts_to_dt, ts_to_dt.dt.hour, ts_to_dt.dt.day, ts_to_dt.dt.isocalendar().week,
                 ts_to_dt.dt.month, ts_to_dt.dt.year, ts_to_dt.dt.weekday]
    column_labels = ('start_time', 'hour', 'day',
                     'week_of_year', 'month', 'year', 'week_day')
    time_labels_dict = dict(zip(column_labels, time_data))
    time_df = pd.DataFrame.from_dict(time_labels_dict)

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = df[['userId', 'firstName', 'lastName', 'gender', 'level']]

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():

        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()

        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record (getting data from dimensions into fact table)
        songplay_data = [time_df['start_time'][index], user_df['userId'][index], user_df['level'][index],
                         songid, artistid, row.sessionId, row.location, row.userAgent]
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root, '*.json'))
        for f in files:
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    # change user and password credientials to your own. mine are user:postgres password:1234
    conn = psycopg2.connect(
        "host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    # adapter to convert from numpy.Int64 to integer in python
    register_adapter(numpy.int64, addapt_numpy_int64)

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
