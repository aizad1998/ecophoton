import psycopg2
from datetime import datetime
import time

print("Hello world")
val = 0

db = psycopg2.connect(
  host="127.0.0.1",
  user="postgres",
  password="root",
  database="raspitest"
)

currtime = datetime.now()

dbcursor = db.cursor()
dbcursor.execute("DROP TABLE IF EXISTS cardata;")
dbcursor.execute("CREATE TABLE IF NOT EXISTS cardata (id serial PRIMARY KEY, data INT NOT NULL, created_on TIMESTAMP DEFAULT NOW());")


while 1:
  datacommand = "INSERT INTO cardata (data) VALUES ("+ str(val) +");"
  dbcursor.execute(datacommand)
  db.commit()
  val += 10
  time.sleep(1)

  #  + str(val) + 

  