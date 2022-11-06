import psycopg2
from config import host, user, password, database
from parsers.brandshop import Brandshop
from parsers.sneakerhead import Sneakerhead
from parsers.streetbeat import Streetbeat
from parsers.superster import Superstep
from parsers.lamoda import Lamoda

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("[SUCCESSFUL CONNECTION]")
    with connection.cursor() as cursor:
        Brandshop.start(cursor)
        Sneakerhead.start(cursor)
        Streetbeat.start(cursor)
        Superstep.start(cursor)
        Lamoda.start(cursor)


except Exception as _ex:
    print("[ERROR]: ", _ex)

finally:
    if connection:
        connection.commit()
        connection.close()
        print("[CLOSE CONNECTION]")
