# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (
    songplay_id serial PRIMARY KEY, 
    start_time TIME NOT NULL, 
    user_id integer NOT NULL, 
    level VARCHAR(255) NOT NULL, 
    song_id VARCHAR(255) NOT NULL, 
    artist_id VARCHAR(255) NOT NULL, 
    session_id integer NOT NULL, 
    location VARCHAR(255), 
    user_agent VARCHAR(255),
    CONSTRAINT songplays_user_id_fkey FOREIGN KEY (user_id)
        REFERENCES users (user_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT songplays_song_id_fkey FOREIGN KEY (song_id)
        REFERENCES songs (song_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION,
    CONSTRAINT songplays_artist_id_fkey FOREIGN KEY (artist_id)
        REFERENCES artists (artist_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
)
""")

user_table_create = ("""
CREATE TABLE users (
    user_id integer PRIMARY KEY, 
    first_name VARCHAR(50) NOT NULL, 
    last_name VARCHAR(50) NOT NULL, 
    gender CHAR(1) NOT NULL, 
    level VARCHAR(255) NOT NULL
)
""")

song_table_create = ("""
CREATE TABLE songs (
    song_id VARCHAR(255) PRIMARY KEY, 
    title VARCHAR(255) NOT NULL, 
    artist_id VARCHAR(255) NOT NULL, 
    year integer NOT NULL, 
    duration float(5) NOT NULL,
    CONSTRAINT songs_artist_id_fkey FOREIGN KEY (artist_id)
        REFERENCES artists (artist_id) MATCH SIMPLE
        ON UPDATE NO ACTION ON DELETE NO ACTION
)
""")

artist_table_create = ("""
CREATE TABLE artists (
    artist_id VARCHAR(255) PRIMARY KEY, 
    name varchar(255) NOT NULL, 
    location VARCHAR(255), 
    lattitude VARCHAR(255), 
    longitude VARCHAR(255)
)
""")

time_table_create = ("""
CREATE TABLE time (
    start_time TIME, 
    hour integer NOT NULL, 
    day integer NOT NULL, 
    week integer NOT NULL, 
    month integer NOT NULL, 
    year integer NOT NULL, 
    weekday integer NOT NULL
)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
SELECT * FROM songs WHERE title = "%s"
""")

# QUERY LISTS
# order is important here, make sure tables are created before tables with foreign keys 
create_table_queries = [time_table_create, artist_table_create, song_table_create, user_table_create, songplay_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]

# original order in template
#create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
#drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
