import sys

import psycopg2


from __init__ import SPECIES 

conn = psycopg2.connect(dbname="otm2", user="otm_user", password="fdbambh$UnN389y8")
conn2 = psycopg2.connect(dbname="otm2", user="otm_user", password="fdbambh$UnN389y8")
cur = conn.cursor()
upcur = conn2.cursor()

cur.execute("select * from treemap_species")

for arow in cur:
    for spec in SPECIES:
        if (spec["genus"].lower() == arow[2].lower() and 
            spec["species"].lower() == arow[3].lower()):
            otm_code = spec["otm_code"]
            update_str = """
            update treemap_species 
            set otm_code = '%s'
            where id = %s""" % (otm_code, arow[0])
            print update_str

            upcur.execute(update_str)
            conn2.commit()


conn.close()
conn2.close()
