class Request:
    def update_price(cursor, price, id):
        sql = """UPDATE prices SET price = %s WHERE id = %s"""
        cursor.execute(sql, (price, id))

    def find_prices(cursor, store):
        sql = """SELECT id, price, link FROM prices WHERE "storeId" = %s"""
        cursor.execute(sql, [store])
        return cursor.fetchall()

    def update_sizes(cursor, sizes, id):
        return False
        # обновляет размеры
