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
import pickle
from selenium.webdriver.support.ui import WebDriverWait as wait

useragent = UserAgent()

options = webdriver.ChromeOptions()
#user-agent каждый раз рандомный юзер
options.add_argument(f"user-agent={useragent.random}")

#убрать уебищные уведомления
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)

#отключение что это автоматизированное ПО
options.add_experimental_option(
    "excludeSwitches", ['enable-automation'])
#полное окно браузера
options.add_argument("start-maximized")
# headless mode

#увеличение скорости
options.add_argument('blink-settings=imagesEnabled=false')


class Streetbeat:
    s = Service("C:\\Users\\Vlad\\Desktop\\megaparser\\chromedriver\\chromedriver.exe")
    browser = webdriver.Chrome(service=s, options=options)

    stealth(browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True
        )



    def start(self):
        for price in Request.find_prices(self, Stores.streetbeat.value):
            Request.update_price(self, Streetbeat.parser(price[2]), price[0])
        Streetbeat.browser.quit()

    def parser(self):
        Streetbeat.browser.get(self)
        Streetbeat.browser.add_cookie({'name': 'user_city', 'value': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0'})
        time.sleep(10)
        return print(Streetbeat.browser.find_element(By.TAG_NAME, "span").text)







