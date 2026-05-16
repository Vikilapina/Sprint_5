from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import (
    LoginPageLocators,
    RegistrationPageLocators,
    AdsPageLocators
)
from data import (
    TEST_EMAIL,
    TEST_PASSWORD,
    AD_TITLE,
    AD_DESCRIPTION,
    AD_PRICE
)


class TestAds:

    def test_unauthorized_user_cannot_create_ad(self, driver):

        driver.find_element(
            *AdsPageLocators.CREATE_AD_BUTTON
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AdsPageLocators.AUTH_MODAL_TEXT
            )
        )

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AdsPageLocators.AUTH_MODAL_TEXT
            )
        ).is_displayed()

    def test_authorized_user_can_create_ad(self, driver):
        email = TEST_EMAIL
        password = TEST_PASSWORD
        title = AD_TITLE
        description = AD_DESCRIPTION
        price = AD_PRICE

        driver.find_element(
            *LoginPageLocators.LOGIN_BUTTON
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                LoginPageLocators.EMAIL_INPUT
            )
        )

        driver.find_element(
            *LoginPageLocators.EMAIL_INPUT
        ).send_keys(email)

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
                AdsPageLocators.CREATE_AD_BUTTON
            )
        )

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                RegistrationPageLocators.USER_NAME
            )
        )

        driver.find_element(
            *AdsPageLocators.CREATE_AD_BUTTON
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AdsPageLocators.AD_TITLE_INPUT
            )
        )

        driver.find_element(
            *AdsPageLocators.AD_TITLE_INPUT
        ).send_keys(title)

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AdsPageLocators.AD_DESCRIPTION_INPUT
            )
        )

        driver.find_element(
            *AdsPageLocators.AD_DESCRIPTION_INPUT
        ).send_keys(description)

        driver.find_element(
            *AdsPageLocators.AD_PRICE_INPUT
        ).send_keys(price)

        driver.find_element(
            *AdsPageLocators.USED_CONDITION_RADIO
        ).click()

        driver.find_element(
            *AdsPageLocators.PUBLISH_AD_BUTTON
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                RegistrationPageLocators.USER_NAME
            )
        )

        driver.find_element(
            *AdsPageLocators.PROFILE_BUTTON
        ).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AdsPageLocators.MY_ADS_TITLE
            )
        )

        assert WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(
                AdsPageLocators.CREATED_AD_TITLE
            )
        ).is_displayed