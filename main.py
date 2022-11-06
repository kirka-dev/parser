import psycopg2
from parsers.brandshop import Brandshop
from parsers.sneakerhead import Sneakerhead
from parsers.streetbeat import Streetbeat
from parsers.superster import Superstep

try:
    connection = psycopg2.connect(
        host="localhost",
        user="postgres",
        password="1234",
        database="bd"
    )
    print("[SUCCESSFUL CONNECTION]")
    with connection.cursor() as cursor:
        Brandshop.start(cursor)
        Sneakerhead.start(cursor)
        Streetbeat.start(cursor)
        Superstep.start(cursor)

except Exception as _ex:
    print("[ERROR]: ", _ex)

finally:
    if connection:
        connection.commit()
        connection.close()
        print("[CLOSE CONNECTION]")
