from database.requests import Request
from enums.stores import Stores


class Streetbeat:
    def start(self):
        for price in Request.find_prices(self, Stores.streetbeat.value):
            Request.update_price(self, Streetbeat.parser(price[2]), price[0])

    def parser(self):
        # тело парсера, которое возвращает цену
        return 92999