import time
import psycopg2
from database.connection import host, user, password, database
from parsers.brandshop import Brandshop
from parsers.lamoda import Lamoda
from parsers.sneakerhead import Sneakerhead
from parsers.streetbeat import Streetbeat
from parsers.superstep import Superstep
from parsers.sportmaster import SportMaster
from parsers.sbermegamarket import Sbermegamarket
from parsers.rendezvous import Rendezvous
from parsers.fitnessplace import Fitnessplace
from parsers.henderson import Henderson
from parsers.guess import Guess

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
        SportMaster.start(cursor)
        Sbermegamarket.start(cursor)
        Rendezvous.start(cursor)
        Fitnessplace.start(cursor)
        Henderson.start(cursor)
        Guess.start(cursor)

except Exception as _ex:
    print("[ERROR]: ", _ex)

finally:
    if connection:
        connection.commit()
        connection.close()
        print("[CLOSE CONNECTION]")
