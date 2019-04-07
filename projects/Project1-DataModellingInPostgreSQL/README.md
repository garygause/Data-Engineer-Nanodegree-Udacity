
Initial setup:
- install postgresql
  - on mac, brew install postgresql
- create studentdb
  - createdb 'studentdb'
- setup user/roles
  - psql postgres
  - \du  #to see roles
  - CREATE USER student with superuser createdb
  - \password student
- test login
  - psql -U student -d studentdb -W

