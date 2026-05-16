import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators, RegistrationPageLocators
from data import TEST_EMAIL, TEST_PASSWORD, INVALID_EMAIL


class TestRegistration:

    def test_user_registration_success(self, driver):
        email = f"user{random.randint(1000, 9999)}@test.com"
        password = TEST_PASSWORD

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.NO_ACCOUNT_BUTTON
            )
        )

        driver.find_element(*LoginPageLocators.NO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.EMAIL_INPUT
            )
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(
            *RegistrationPageLocators.REPEAT_PASSWORD_INPUT
        ).send_keys(password)

        driver.find_element(
            *LoginPageLocators.CREATE_ACCOUNT_BUTTON
        ).click()

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                RegistrationPageLocators.USER_NAME
            )
        ).is_displayed()

    def test_invalid_email_error(self, driver):
        email = INVALID_EMAIL

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.NO_ACCOUNT_BUTTON
            )
        )

        driver.find_element(*LoginPageLocators.NO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.EMAIL_INPUT
            )
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

        driver.find_element(
            *LoginPageLocators.CREATE_ACCOUNT_BUTTON
        ).click()

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                RegistrationPageLocators.ERROR_MESSAGE
            )
        ).is_displayed()

    def test_existing_user_registration_error(self, driver):
        email = TEST_EMAIL
        password = TEST_PASSWORD

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.NO_ACCOUNT_BUTTON
            )
        )

        driver.find_element(*LoginPageLocators.NO_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.EMAIL_INPUT
            )
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(password)

        driver.find_element(
            *RegistrationPageLocators.REPEAT_PASSWORD_INPUT
        ).send_keys(password)

        driver.find_element(
            *LoginPageLocators.CREATE_ACCOUNT_BUTTON
        ).click()

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                RegistrationPageLocators.ERROR_MESSAGE
            )
        ).is_displayed()