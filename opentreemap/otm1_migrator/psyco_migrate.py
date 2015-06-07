import psycopg2

# Connect to an existing database
#conn = psycopg2.connect("dbname=otm1 user=postgres")
conn = psycopg2.connect("host=131.247.223.141 dbname=otm1 user=otm_user password=fdbambh$UnN389y8")

# Open a cursor to perform database operations
cur = conn.cursor()

# Query the database and obtain data as Python objects
cur.execute("SELECT * FROM treemap_species;")
cur.fetchone()


# Close communication with the database
cur.close()
conn.close()
