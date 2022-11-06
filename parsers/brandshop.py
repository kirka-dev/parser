from database.requests import Request
from enums.stores import Stores

from selenium import webdriver
from selenium.common import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium_stealth import stealth


class Brandshop:
    service = Service("../chromedriver/chromedriver.exe")

    desired_capabilities = DesiredCapabilities().CHROME
    desired_capabilities["pageLoadStrategy"] = "none"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(service=service, desired_capabilities=desired_capabilities, options=options)

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
        for price in Request.find_prices(self, Stores.brandshop.value):
            Request.update_price(self, Brandshop.parser(price[2]), price[0])
        Brandshop.browser.quit()

    def parser(self):
        Brandshop.browser.get(self)
        price = WebDriverWait(
            driver=Brandshop.browser,
            timeout=5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        ).until(ec.presence_of_element_located((By.CLASS_NAME, "product-order__price-wrapper"))).text
        print("[SUCCESS]", self, price)
        return price