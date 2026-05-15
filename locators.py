from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Вход и регистрация']")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выйти']")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Нет аккаунта']")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[normalize-space()='Создать аккаунт']")


class RegistrationPageLocators:
    REPEAT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    USER_NAME = (By.XPATH, "//h3[contains(text(), 'User')]")
    ERROR_MESSAGE = (By.XPATH, "//span[normalize-space()='Ошибка']")


class AdsPageLocators:
    CREATE_AD_BUTTON = (By.XPATH, "//button[normalize-space()='Разместить объявление']")
    AUTH_MODAL_TEXT = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление')]")
    AD_TITLE_INPUT = (By.NAME, "name")
    AD_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@placeholder='Описание товара']")
    AD_PRICE_INPUT = (By.NAME, "price")
    USED_CONDITION_RADIO = (By.XPATH, "//label[normalize-space()='Б/У']")
    PUBLISH_AD_BUTTON = (By.XPATH, "//button[normalize-space()='Опубликовать']")
    MY_ADS_TITLE = (By.XPATH, "//h1[normalize-space()='Мои объявления']")
    CREATED_AD_TITLE = (By.CSS_SELECTOR, "img.picture")
    PROFILE_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")