from database.requests import Request
from selenium import webdriver
from selenium_stealth import stealth
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from enums.stores import Stores
from multiprocessing import Pool
import re
from database.requests import Request

useragent = UserAgent()

options = webdriver.ChromeOptions()
#user-agent каждый раз рандомный юзер
options.add_argument(f"user-agent={useragent.random}")

#отключение что это автоматизированное ПО
options.add_experimental_option(
    "excludeSwitches", ['enable-automation'])
#полное окно браузера
options.add_argument("start-maximized")
# headless mode

options.headless = True

class Sneakerhead:
    s = Service("C:\\Users\\Vlad\\Desktop\\megaparser\\chromedriver\\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)
    stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
        )

    def start(self):
        for price in Request.find_prices(self, Stores.sneakerhead.value):
            Request.update_price(self, Sneakerhead.parser(price[2]), price[0])
        Sneakerhead.browser.quit()

    def parser(self):
        # тело парсера, которое возвращает цену
        Sneakerhead.browser.get(self)
        print("Цена передана:", self)
        return Sneakerhead.browser.find_element(By.CLASS_NAME, "product__price-value").text
        # time.sleep(random.randrange(3,10))

