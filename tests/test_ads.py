from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import(
    CREATE_AD_BUTTON_METHOD,
    CREATE_AD_BUTTON_LOCATOR,
    AUTH_MODAL_TEXT_METHOD,
    AUTH_MODAL_TEXT_LOCATOR,
    LOGIN_BUTTON_METHOD,
    LOGIN_BUTTON_LOCATOR,
    EMAIL_INPUT_METHOD,
    EMAIL_INPUT_LOCATOR,
    PASSWORD_INPUT_METHOD,
    PASSWORD_INPUT_LOCATOR,
    LOGIN_SUBMIT_BUTTON_METHOD,
    LOGIN_SUBMIT_BUTTON_LOCATOR,
    AD_TITLE_INPUT_METHOD,
    AD_TITLE_INPUT_LOCATOR,
    AD_DESCRIPTION_INPUT_METHOD,
    AD_DESCRIPTION_INPUT_LOCATOR,
    AD_PRICE_INPUT_METHOD,
    AD_PRICE_INPUT_LOCATOR,
    USED_CONDITION_RADIO_METHOD,
    USED_CONDITION_RADIO_LOCATOR,
    PUBLISH_AD_BUTTON_METHOD,
    PUBLISH_AD_BUTTON_LOCATOR,
    USER_NAME_METHOD,
    USER_NAME_LOCATOR,
    MY_ADS_TITLE_METHOD,
    MY_ADS_TITLE_LOCATOR,
    CREATED_AD_TITLE_METHOD,
    CREATED_AD_TITLE_LOCATOR,
    PROFILE_BUTTON_METHOD,
    PROFILE_BUTTON_LOCATOR
)

class TestAds:
    def test_unauthorized_user_cannot_create_ad(self, driver):
        driver.find_element(CREATE_AD_BUTTON_METHOD, CREATE_AD_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((AUTH_MODAL_TEXT_METHOD, AUTH_MODAL_TEXT_LOCATOR)))

        modal_text = driver.find_element(AUTH_MODAL_TEXT_METHOD,AUTH_MODAL_TEXT_LOCATOR).text

        assert "Чтобы разместить объявление, авторизуйтесь" in modal_text

        driver.quit()

    def test_authorized_user_can_create_ad(self, driver):
        email = "test@test.com"
        password = "Password123"
        title = "Тестовое объявление"
        description = "Описание тестового товара"
        price = "1000"

        driver.find_element(LOGIN_BUTTON_METHOD, LOGIN_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR)))

        driver.find_element(EMAIL_INPUT_METHOD, EMAIL_INPUT_LOCATOR).send_keys(email)
        driver.find_element(PASSWORD_INPUT_METHOD, PASSWORD_INPUT_LOCATOR).send_keys(password)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((LOGIN_SUBMIT_BUTTON_METHOD, LOGIN_SUBMIT_BUTTON_LOCATOR)))

        driver.find_element(LOGIN_SUBMIT_BUTTON_METHOD, LOGIN_SUBMIT_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((CREATE_AD_BUTTON_METHOD, CREATE_AD_BUTTON_LOCATOR)))
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((USER_NAME_METHOD, USER_NAME_LOCATOR)))

        driver.find_element(CREATE_AD_BUTTON_METHOD, CREATE_AD_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((AD_TITLE_INPUT_METHOD, AD_TITLE_INPUT_LOCATOR)))

        driver.find_element(AD_TITLE_INPUT_METHOD, AD_TITLE_INPUT_LOCATOR).send_keys(title)
    
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((AD_DESCRIPTION_INPUT_METHOD, AD_DESCRIPTION_INPUT_LOCATOR)))
    
        driver.find_element(AD_DESCRIPTION_INPUT_METHOD, AD_DESCRIPTION_INPUT_LOCATOR).send_keys(description)
        driver.find_element(AD_PRICE_INPUT_METHOD, AD_PRICE_INPUT_LOCATOR).send_keys(price)

        driver.find_element(USED_CONDITION_RADIO_METHOD, USED_CONDITION_RADIO_LOCATOR).click()
        driver.find_element(PUBLISH_AD_BUTTON_METHOD, PUBLISH_AD_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((USER_NAME_METHOD, USER_NAME_LOCATOR)))

        driver.find_element(PROFILE_BUTTON_METHOD, PROFILE_BUTTON_LOCATOR).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((MY_ADS_TITLE_METHOD, MY_ADS_TITLE_LOCATOR)))
    
        created_ad_title = WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((CREATED_AD_TITLE_METHOD, CREATED_AD_TITLE_LOCATOR))).get_attribute("alt")

        assert title in created_ad_title

        driver.quit()