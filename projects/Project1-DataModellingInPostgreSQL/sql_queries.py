"""
SQL Queries for working with our Sparkify data.

NOTE: TEXT field types are used because there is a performance penalty
for field types with limits, e.g. VARCHAR(255) in postgres.

EXCEPTION: we take the slight performance hit on gender CHAR(1) on the
users table because this allows us to truncate to the first letter, making 
the data more consistent, i.e. "Female" will still be stored as "F".
"""

# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
    songplay_id SERIAL PRIMARY KEY, 
    start_time TIMESTAMP NOT NULL, 
    user_id INT NOT NULL, 
    level TEXT NOT NULL, 
    song_id TEXT, 
    artist_id TEXT, 
    session_id INT NOT NULL, 
    location TEXT, 
    user_agent TEXT
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY, 
    first_name TEXT NOT NULL, 
    last_name TEXT NOT NULL, 
    gender CHAR(1) NOT NULL, 
    level TEXT NOT NULL
);
""")

# NOTE: songs table has one additional index, artist_id, to make
# our joins more efficient.

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id TEXT PRIMARY KEY, 
    title TEXT NOT NULL, 
    artist_id TEXT NOT NULL, 
    year INT NOT NULL, 
    duration NUMERIC NOT NULL
);
CREATE INDEX idx_songs_artist_id ON songs(artist_id);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id TEXT PRIMARY KEY, 
    name TEXT NOT NULL, 
    location TEXT, 
    latitude NUMERIC, 
    longitude NUMERIC
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time TIMESTAMP PRIMARY KEY, 
    hour INT NOT NULL, 
    day INT NOT NULL, 
    week INT NOT NULL, 
    month INT NOT NULL, 
    year INT NOT NULL, 
    weekday INT NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays (start_time, user_id, level, session_id, location, user_agent, song_id, artist_id) \
VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
""")

# NOTE: update user level to 'paid' on conflict to ensure data integrity.
# TODO: if inserted in time order, update level to 'free' if appropriate

user_table_insert = ("""
INSERT INTO users (user_id, first_name, last_name, gender, level) \
VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (user_id) \
DO UPDATE SET level = 'paid' WHERE users.level = 'paid' OR EXCLUDED.level = 'paid';
""")

song_table_insert = ("""
INSERT INTO songs (song_id, title, artist_id, year, duration) \
VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (song_id) \
DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artists (artist_id, name, location, latitude, longitude) \
VALUES (%s, %s, %s, %s, %s) \
ON CONFLICT (artist_id) \
DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time (start_time, hour, day, week, month, year, weekday) \
VALUES (%s, %s, %s, %s, %s, %s, %s) \
ON CONFLICT (start_time) \
DO NOTHING;
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, artists.artist_id FROM songs \
INNER JOIN artists \
ON songs.artist_id=artists.artist_id \
WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s;
""")

# QUERY LISTS
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
