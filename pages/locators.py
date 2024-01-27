from selenium.webdriver.common.by import By


class SbisMainLocators:
    CONTACTS_HEADER = (By.CSS_SELECTOR, 'a.sbisru-Header__menu-link[href="/contacts"]')


class SbisContactsLocators:
    TENSOR_CLICKABLE_BANNER = (By.CSS_SELECTOR, 'div.mt-xm-12 > a.sbisru-Contacts__logo-tensor')
    TENSOR_BANNER = (By.CSS_SELECTOR, TENSOR_CLICKABLE_BANNER[1] + ' > img')


class TensorMainPageLocators:
    POWER_OF_MAN_BLOCK = (By.CSS_SELECTOR, ".tensor_ru-Index__block4-content.tensor_ru-Index__card")
    POWER_OF_MAN_BLOCK_ABOUT_BUTTON = (By.XPATH, "//a[text()='Подробнее' and @href='/about']")


class TensorAboutPageLocators:
    WORKING_BLOCK = (By.CSS_SELECTOR, ".tensor_ru - About__block - title - block +.s - Grid - container")