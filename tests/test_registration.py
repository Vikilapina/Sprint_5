import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    LOGIN_BUTTON_METHOD, 
    LOGIN_BUTTON_LOCATOR,
    NO_ACCOUNT_BUTTON_METHOD,
    NO_ACCOUNT_BUTTON_LOCATOR,
    EMAIL_INPUT_METHOD,
    EMAIL_INPUT_LOCATOR,
    PASSWORD_INPUT_METHOD,
    PASSWORD_INPUT_LOCATOR,
    REPEAT_PASSWORD_INPUT_METHOD,
    REPEAT_PASSWORD_INPUT_LOCATOR,
    CREATE_ACCOUNT_BUTTON_METHOD,
    CREATE_ACCOUNT_BUTTON_LOCATOR,
    USER_NAME_METHOD,
    USER_NAME_LOCATOR,
    ERROR_MESSAGE_METHOD,
    ERROR_MESSAGE_LOCATOR
)

class TestRegistration:
    def test_user_registration_success(self, driver):
        email = f"user{random.randint(1000, 9999)}@test.com"
        password = "Password123" 
    
        driver.find_element(LOGIN_BUTTON_METHOD, LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NO_ACCOUNT_BUTTON_METHOD, NO_ACCOUNT_BUTTON_LOCATOR)))
        driver.find_element(NO_ACCOUNT_BUTTON_METHOD, NO_ACCOUNT_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR)))

        driver.find_element(EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR).send_keys(email)
        driver.find_element(PASSWORD_INPUT_METHOD, PASSWORD_INPUT_LOCATOR).send_keys(password)
        driver.find_element(REPEAT_PASSWORD_INPUT_METHOD, REPEAT_PASSWORD_INPUT_LOCATOR).send_keys(password)
        driver.find_element(CREATE_ACCOUNT_BUTTON_METHOD, CREATE_ACCOUNT_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((USER_NAME_METHOD, USER_NAME_LOCATOR)))
    
        user_name = driver.find_element(USER_NAME_METHOD, USER_NAME_LOCATOR).text

        assert "User" in user_name

        driver.quit()

    def test_invalid_email_error(self, driver):
        email = "test@test"
    
        driver.find_element(LOGIN_BUTTON_METHOD, LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NO_ACCOUNT_BUTTON_METHOD, NO_ACCOUNT_BUTTON_LOCATOR)))
        driver.find_element(NO_ACCOUNT_BUTTON_METHOD, NO_ACCOUNT_BUTTON_LOCATOR).click()
   
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR)))
   
        driver.find_element(EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR).send_keys(email)
        driver.find_element(CREATE_ACCOUNT_BUTTON_METHOD, CREATE_ACCOUNT_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((ERROR_MESSAGE_METHOD,ERROR_MESSAGE_LOCATOR)))

        error_message = driver.find_element(ERROR_MESSAGE_METHOD,ERROR_MESSAGE_LOCATOR).text

        assert error_message == "Ошибка"

        driver.quit()

    def test_existing_user_registration_error(self,driver):
        email = "test@test.com"
        password = "Password123" 
    
        driver.find_element(LOGIN_BUTTON_METHOD, LOGIN_BUTTON_LOCATOR).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((NO_ACCOUNT_BUTTON_METHOD, NO_ACCOUNT_BUTTON_LOCATOR)))
        driver.find_element(NO_ACCOUNT_BUTTON_METHOD, NO_ACCOUNT_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR)))

        driver.find_element(EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR).send_keys(email)
        driver.find_element(PASSWORD_INPUT_METHOD, PASSWORD_INPUT_LOCATOR).send_keys(password)
        driver.find_element(REPEAT_PASSWORD_INPUT_METHOD, REPEAT_PASSWORD_INPUT_LOCATOR).send_keys(password)
        driver.find_element(CREATE_ACCOUNT_BUTTON_METHOD, CREATE_ACCOUNT_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((ERROR_MESSAGE_METHOD,ERROR_MESSAGE_LOCATOR)))

        error_message = driver.find_element(ERROR_MESSAGE_METHOD,ERROR_MESSAGE_LOCATOR).text

        assert error_message == "Ошибка"

        driver.quit()