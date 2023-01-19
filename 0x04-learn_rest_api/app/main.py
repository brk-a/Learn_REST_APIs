import psycopg2

conn = psycopg2.connect("dbname=my_api user=postgres")
cur = conn.cursor()