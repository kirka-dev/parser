from database.requests import Request
from enums.stores import Stores


class Superstep:
    def start(self):
        for price in Request.find_prices(self, Stores.superstep.value):
            Request.update_price(self, Superstep.parser(price[2]), price[0])

    def parser(self):
        # тело парсера, которое возвращает цену
        return 99999
