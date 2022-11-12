import psycopg2
from concurrent import futures
from concurrent.futures import as_completed
from concurrent.futures.thread import ThreadPoolExecutor

from database.connection import host, user, password, database
from parsers.brandshop import Brandshop
from parsers.fitnessplace import Fitnessplace
from parsers.guess import Guess
from parsers.henderson import Henderson
from parsers.lamoda import Lamoda
from parsers.rendezvous import Rendezvous
from parsers.sbermegamarket import Sbermegamarket
from parsers.sneakerhead import Sneakerhead
from parsers.sportmaster import SportMaster
from parsers.streetbeat import Streetbeat
from parsers.superstep import Superstep

parsers = [
    Brandshop.start,
    Fitnessplace.start,
    Guess.start,
    Henderson.start,
    Lamoda.start,
    Rendezvous.start,
    Sbermegamarket.start,
    Superstep.start,
    Sneakerhead.start,
    SportMaster.start,
    Streetbeat.start,
]

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("[SUCCESSFUL CONNECTION]")

    with connection.cursor() as cursor:
        with ThreadPoolExecutor(max_workers=2) as executor:
            futures = [executor.submit(parser, cursor) for parser in parsers]

            for future in as_completed(futures):
                result = future.result()

except Exception as _ex:
    print("[ERROR]: ", _ex)

finally:
    if connection:
        connection.commit()
        connection.close()
        print("[CLOSE CONNECTION]")
