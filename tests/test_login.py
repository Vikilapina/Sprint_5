from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import LoginPageLocators, RegistrationPageLocators
from data import TEST_EMAIL, TEST_PASSWORD


class TestLogin:

    def test_user_login(self, driver):
        email = TEST_EMAIL
        password = TEST_PASSWORD

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.EMAIL_INPUT
            )
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

        driver.find_element(
            *LoginPageLocators.PASSWORD_INPUT
        ).send_keys(password)

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.LOGIN_SUBMIT_BUTTON
            )
        )

        driver.find_element(
            *LoginPageLocators.LOGIN_SUBMIT_BUTTON
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                RegistrationPageLocators.USER_NAME
            )
        )

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                RegistrationPageLocators.USER_NAME
            )
        ).is_displayed()

    def test_user_logout(self, driver):
        email = TEST_EMAIL
        password = TEST_PASSWORD

        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.EMAIL_INPUT
            )
        )

        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)

        driver.find_element(
            *LoginPageLocators.PASSWORD_INPUT
        ).send_keys(password)

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.LOGIN_SUBMIT_BUTTON
            )
        )

        driver.find_element(
            *LoginPageLocators.LOGIN_SUBMIT_BUTTON
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.LOGOUT_BUTTON
            )
        )

        driver.find_element(
            *LoginPageLocators.LOGOUT_BUTTON
        ).click()

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.LOGIN_BUTTON
            )
        ).is_displayed()