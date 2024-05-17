import os

from getgauge.python import step
from step_impl.utils.driver import Driver


@step("Go to the page <endpoint>")
def goto_the_page(endpoint):
    URL = f'{os.getenv("APP_ENDPOINT")}/{endpoint}'
    Driver.driver.get(URL)
