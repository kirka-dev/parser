from database.requests import Request
from enums.stores import Stores


class Brandshop:
    def start(self):
        for price in Request.find_prices(self, Stores.brandshop.value):
            Request.update_price(self, Brandshop.parser(price[2]), price[0])

    def parser(self):
        # тело парсера, которое возвращает цену
        return 99999
