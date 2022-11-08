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


class Streetbeat:
    service = Service("../chromedriver/chromedriver")

    desired_capabilities = DesiredCapabilities().CHROME
    desired_capabilities["pageLoadStrategy"] = "none"

    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option("excludeSwitches", ['enable-automation'])
    options.add_argument("start-maximized")
    options.add_argument("blink-settings=imagesEnabled=false")
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
        for price in Request.find_prices(self, Stores.streetbeat.value):
            Request.update_price(self, Streetbeat.parser(price[2]), price[0])
        Streetbeat.browser.quit()

    def parser(self):
        Streetbeat.browser.get(self)
        price = WebDriverWait(
            driver=Streetbeat.browser,
            timeout=5,
            ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
        ).until(ec.presence_of_element_located((By.XPATH, '//span[@class="price-tag__discount" or @class="price-tag__default"]'))).get_attribute("innerHTML")
        result = Converter.price(price)

        print("[SUCCESS]", self, result)
        return result
        #try:
            #price = WebDriverWait(
                #driver=Streetbeat.browser,
                #timeout=15,
                #ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
            #).until(ec.presence_of_element_located((By.CLASS_NAME, "price-tag__discount"))).get_attribute("innerHTML")

        #except:
            #price = WebDriverWait(
                #driver=Streetbeat.browser,
                #timeout=15,
                #ignored_exceptions=[NoSuchElementException, StaleElementReferenceException]
            #).until(ec.presence_of_element_located((By.CLASS_NAME, "price-tag__default"))).get_attribute("innerHTML")

        #finally:
            #result = Converter.price(price)

        #print("[SUCCESS]", self, result)
        #return result
