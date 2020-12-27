import psycopg2
conn = psycopg2.connect(database="postgis_30_sample", user="postgres", password="admin123")
print("Opened database successfully")