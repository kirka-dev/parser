from database.requests import Request
from enums.stores import Stores
from utils.converter import Converter

from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth


class Rendezvous:
    service = Service("../chromedriver/chromedriver.exe")

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(service=service, options=options)

    stealth(
        browser,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )

    def start(self):
        for price in Request.find_prices(self, Stores.rendezvous.value):
            Request.update_price(self, Rendezvous.parser(price[2]), price[0])
        Rendezvous.browser.quit()

    def parser(self):
        Rendezvous.browser.get(self)
        price = WebDriverWait(
            driver=Rendezvous.browser,
            timeout=10,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        ).until(ec.presence_of_element_located((By.CLASS_NAME, "item-price-value"))).text
        result = Converter.price(price)

        print("[SUCCESS]", self, result)
        return result