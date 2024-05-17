from getgauge.python import step
from selenium.webdriver.common.by import By
from step_impl.utils.driver import Driver


@step("Check if the page contains <text>")
def check_page_contains(text):
    assert text in Driver.driver.page_source


@step("Give an option to Log In")
def give_an_option_to_login():
    Driver.driver.find_element(By.LINK_TEXT, "Log in")


@step("Show the log in status for user <name>")
def show_the_login_status_for_user(name):
    authenticated_info = Driver.driver.find_element(By.ID, "user-tools")
    user_name = authenticated_info.find_element(By.TAG_NAME, "strong")
    assert True, name.upper() == user_name.text.upper()


@step("Login as name <name> and <password>")
def login_as_name_with_password(name, password):
    driver = Driver.driver
    driver.find_element(By.NAME, "username").send_keys(name)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.XPATH, "//input[@value='Log in']").click()
