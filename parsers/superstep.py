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


class Superstep:
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
        for price in Request.find_prices(self, Stores.superstep.value):
            Request.update_price(self, Superstep.parser(price[2]), price[0])
        Superstep.browser.quit()

    def parser(self):
        Superstep.browser.get(self)
        price = WebDriverWait(
            driver=Superstep.browser,
            timeout=10,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        ).until(ec.presence_of_element_located((By.CLASS_NAME, "product-detail__sale-price--black"))).text
        result = Converter.price(price)

        print("[SUCCESS]", self, result)
        return result
