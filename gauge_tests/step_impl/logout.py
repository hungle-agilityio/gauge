from getgauge.python import step
from selenium.webdriver.common.by import By
from step_impl.utils.driver import Driver


@step("Clear previous login")
def clear_previous_login():
    try:
        Driver.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    except Exception as error:
        print("No previous logins", error)


@step("Give an option to Log Out")
def give_an_option_to_logout():
    assert True, Driver.driver.find_element(By.LINK_TEXT, "Log out") != null


@step("Log out the customer")
def logout_the_customer():
    try:
        Driver.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    except Exception as error:
        print("No account login", error)
