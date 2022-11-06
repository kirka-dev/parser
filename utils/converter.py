import re


class Converter:
    def price(self):
        return re.sub("[^0-9]", "", self)

    def sizes():
        return False
        # получает список размеров в виде массива
        # определяет категорию размеров обувь/одежда/акссесуар
        # по таблице выставляет соответствующие размеры
