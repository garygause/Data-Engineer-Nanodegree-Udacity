Data Engineer Project 1 - Sparkify Music Database in PostgreSQL
==========================================

1. Overview
2. Initial Setup
3. Project Files
4. Schema
5. See Also

## Overview

This project is the first project in the Udacity Data Engineer Nanodegree program.  The goal of the project is to create a database for the fictional Sparkify Music Streaming Service.

We are provided with some code templates (see original_files), as well as user activity logs (song plays) and song data from the Million Song Dataset.

Our goal is to design a database in postgres and perform ETL actions on the data to allow us to answer the following types of questions:

- What is the most popular song played?
- What artist has the most songs played?
- What is the favorite artist for a particular user?  Favorite song?
- What is the average amount of time spent by users?
- What is the most active user on the service?

## Initial Setup

If you wish to run this code locally, I recommend either installing postgres locally or using one of the popular Docker images (Docker not covered in this README).  For local install, perform the following steps before running the code:

- Install PostgreSQL (on Mac, brew install postgresql is convenient).
- Create "studentdb" (createdb 'studentdb').
- Add "student" user with password "student" and grant createdb role.
- Test login (psql -U student -d studentdb -W)

In addition, you will want to install jupyter to run the notebooks, install a virtualenv (python3 -m venv env), and install the modules in requirements.txt (pip install -r requirements.txt).


## Project Files

The following files can be found in this project.

- create_tables.py: a helper script for dropping and creating tables based on the sql in sql_queries.py.

- sql_queries.py: contains all the sql used in the project, drop/create tables, insert/query tables.

- etl.ipynb: jupyter notebook for building the initial ETL code.

- etl.py: actual ETL code for working with the data.

- test.ipynb: notebook for running test queries against the loaded database.

- data: song and log data to be processed

- original_files: directory of the original, unedited files in the project
   
## Schema

The following schema was implemented to support the business (project) needs.  

TEXT fields are used over fixed length VARCHAR(n) type fields to avoid the performance hit of length comparison.  

TIMESTAMP fields are used for data manipulatio.  

### songplays

Fact table with records in log data associated with song plays i.e. records with page NextSong

NOTE: we do not always have artist or song info in the log files.

| COLUMN  	| TYPE  	| NULL     | KEY   	 |
|---	        |---	        |---       |---          |
|   songplay_id	| SERIAL        | NOT NULL | PRIMARY KEY | 
|   start_time	|   TIMESTAMP	| NOT NULL |             | 
|   user_id	|   INT	        | NOT NULL | 	| 
|   level	|   TEXT        | NOT NULL |  	| 
|   song_id	|   TEXT	|          |    | 
|   artist_id	|   TEXT	|          |   	| 
|   session_id	|   INT	   	| NOT NULL |    |
|   location	|   TEXT	|          |  	| 
|   user_agent	|   TEXT	|          |  	| 


### users

Dimension table with users in the app.

NOTE: CHAR(1) is used for gender field to ensure consistent format, "M|F", allowing the field to be truncated automatically if something like "Female" is entered.

| COLUMN  	| TYPE  	| NULL      | KEY   	|
|---	        |---	        |---	    |---        |	
|   user_id	| INT  	        | NOT NULL  |   PRIMARY KEY	| 
|   first_name	| TEXT     	| NOT NULL  |	| 
|   last_name	| TEXT  	| NOT NULL  |	| 
|   gender	| CHAR(1)       | NOT NULL  |  	| 
|   level	| TEXT   	| NOT NULL  | 	| 


### songs

Dimension table with songs in the music database.

NOTE: INDEX added to artist_id for more efficient JOINS.

 | COLUMN  	| TYPE  	| NULL      | KEY   	|
|---	        |---	        |---	    |---        |	
|   song_id	| TEXT  	| NOT NULL  |   PRIMARY KEY	| 
|   title	| TEXT   	| NOT NULL  |	| 
|   artist_id	| TEXT   	| NOT NULL  |  INDEX	| 
|   year	| INT           | NOT NULL  |	| 
|   duration	| NUMERIC 	| NOT NULL  |  	| 


### artists

Dimension table with artists in the music database.

| COLUMN  	| TYPE  	| NULL      | KEY   	|
|---	        |---	        |---	    |---        |	
|   artist_id	| TEXT  	| NOT NULL  |   PRIMARY KEY	| 
|   name	| TEXT   	| NOT NULL  |  	| 
|   location	| TEXT    	|           |	| 
|   latitude	| NUMERIC 	|           |	| 
|   longitude	| NUMERIC       |           |   | 


### time

Dimension table with timestamps of records in songplays broken down into specific units.

NOTE: All fields are NOT NULL because we calculate all values off start_time prior to insert.

 | COLUMN  	| TYPE  	| NULL      | KEY   	|
|---	        |---	        |---	    |---        |	
|   start_time	| TIMESTAMP  	| NOT NULL  |   PRIMARY KEY	| 
|   hour	| INT    	| NOT NULL  |  	| 
|   day	        |  INT    	| NOT NULL  |  	| 
|   week	|  INT   	| NOT NULL  |  	| 
|   month	|  INT   	| NOT NULL  |  	| 
|   year	|  INT   	| NOT NULL  |  	| 
|   weekday	|  INT   	| NOT NULL  |  	| 


## See Also

- [Million Song Dataset](https://labrosa.ee.columbia.edu/millionsong/)
- [Data Engineer - Udacity](https://www.udacity.com/course/data-engineer-nanodegree--nd027)


