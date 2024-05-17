from getgauge.python import after_suite, before_suite
from selenium import webdriver


class Driver(object):
    driver = None

    @before_suite
    def init(self):
        Driver.driver = webdriver.Chrome()

    @after_suite
    def close(self):
        Driver.driver.close()
