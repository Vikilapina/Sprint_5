from selenium.webdriver.common.by import By

LOGIN_BUTTON_METHOD = By.XPATH
LOGIN_BUTTON_LOCATOR = "//button[normalize-space()='Вход и регистрация']"

NO_ACCOUNT_BUTTON_METHOD = By.XPATH
NO_ACCOUNT_BUTTON_LOCATOR = "//button[normalize-space()='Нет аккаунта']"

EMAIL_INPUT_METHOD = By.NAME
EMAIL_INPUT_LOCATOR = "email"

PASSWORD_INPUT_METHOD = By.NAME
PASSWORD_INPUT_LOCATOR = "password"

REPEAT_PASSWORD_INPUT_METHOD = By.NAME
REPEAT_PASSWORD_INPUT_LOCATOR = "submitPassword"

CREATE_ACCOUNT_BUTTON_METHOD = By.XPATH
CREATE_ACCOUNT_BUTTON_LOCATOR = "//button[normalize-space()='Создать аккаунт']"

USER_NAME_METHOD = By.XPATH
USER_NAME_LOCATOR = "//h3[contains(text(), 'User')]"

ERROR_MESSAGE_METHOD = By.XPATH
ERROR_MESSAGE_LOCATOR = "//span[normalize-space()='Ошибка']"

LOGIN_SUBMIT_BUTTON_METHOD = By.XPATH
LOGIN_SUBMIT_BUTTON_LOCATOR = "//button[normalize-space()='Войти']"

LOGOUT_BUTTON_METHOD = By.XPATH
LOGOUT_BUTTON_LOCATOR = "//button[normalize-space()='Выйти']"

CREATE_AD_BUTTON_METHOD = By.XPATH
CREATE_AD_BUTTON_LOCATOR = "//button[normalize-space()='Разместить объявление']"

AUTH_MODAL_TEXT_METHOD = By.XPATH
AUTH_MODAL_TEXT_LOCATOR = "//h1[contains(text(), 'Чтобы разместить объявление')]"

AD_TITLE_INPUT_METHOD = By.NAME
AD_TITLE_INPUT_LOCATOR = "name"

AD_DESCRIPTION_INPUT_METHOD = By.XPATH
AD_DESCRIPTION_INPUT_LOCATOR = "//textarea[@placeholder='Описание товара']"

AD_PRICE_INPUT_METHOD = By.NAME
AD_PRICE_INPUT_LOCATOR = "price"

CITY_DROPDOWN_METHOD = By.NAME
CITY_DROPDOWN_LOCATOR = "city"

USED_CONDITION_RADIO_METHOD = By.XPATH
USED_CONDITION_RADIO_LOCATOR = "//label[normalize-space()='Б/У']"

PUBLISH_AD_BUTTON_METHOD = By.XPATH
PUBLISH_AD_BUTTON_LOCATOR = "//button[normalize-space()='Опубликовать']"

MY_ADS_TITLE_METHOD = By.XPATH
MY_ADS_TITLE_LOCATOR = "//h1[normalize-space()='Мои объявления']"

CREATED_AD_TITLE_METHOD = By.XPATH
CREATED_AD_TITLE_LOCATOR = "//img[contains(@alt, 'Тестовое объявление')]"

PROFILE_BUTTON_METHOD = By.CSS_SELECTOR
PROFILE_BUTTON_LOCATOR = "button.circleSmall"