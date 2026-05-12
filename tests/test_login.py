from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    LOGIN_BUTTON_METHOD,
    LOGIN_BUTTON_LOCATOR,
    EMAIL_INPUT_METHOD,
    EMAIL_INPUT_LOCATOR,
    PASSWORD_INPUT_METHOD,
    PASSWORD_INPUT_LOCATOR,
    LOGIN_SUBMIT_BUTTON_METHOD,
    LOGIN_SUBMIT_BUTTON_LOCATOR,
    USER_NAME_METHOD,
    USER_NAME_LOCATOR,
    LOGOUT_BUTTON_METHOD,
    LOGOUT_BUTTON_LOCATOR
)

class TestLogin:
    def test_user_login(self, driver):
        email = "test@test.com"
        password = "Password123" 

        driver.find_element(LOGIN_BUTTON_METHOD, LOGIN_BUTTON_LOCATOR).click()
    
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR)))
        driver.find_element(EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR).send_keys(email)
    
        driver.find_element(PASSWORD_INPUT_METHOD, PASSWORD_INPUT_LOCATOR).send_keys(password)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LOGIN_SUBMIT_BUTTON_METHOD, LOGIN_SUBMIT_BUTTON_LOCATOR)))
        driver.find_element(LOGIN_SUBMIT_BUTTON_METHOD, LOGIN_SUBMIT_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((USER_NAME_METHOD, USER_NAME_LOCATOR)))
    
        user_name = driver.find_element(USER_NAME_METHOD, USER_NAME_LOCATOR).text

        assert "User" in user_name

        driver.quit()

    def test_user_logout(self,driver):
        email = "test@test.com"
        password = "Password123" 

        driver.find_element(LOGIN_BUTTON_METHOD, LOGIN_BUTTON_LOCATOR).click()
    
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR)))
        driver.find_element(EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR).send_keys(email)
        driver.find_element(PASSWORD_INPUT_METHOD, PASSWORD_INPUT_LOCATOR).send_keys(password)
    
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LOGIN_SUBMIT_BUTTON_METHOD, LOGIN_SUBMIT_BUTTON_LOCATOR)))
        driver.find_element(LOGIN_SUBMIT_BUTTON_METHOD, LOGIN_SUBMIT_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LOGOUT_BUTTON_METHOD, LOGOUT_BUTTON_LOCATOR)))
        driver.find_element(LOGOUT_BUTTON_METHOD,LOGOUT_BUTTON_LOCATOR).click()

        login_button = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LOGIN_BUTTON_METHOD, LOGIN_BUTTON_LOCATOR)))

        assert login_button.is_displayed()

        driver.quit()