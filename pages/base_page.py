from selenium.webdriver.common.by import By

class HeaderElements:
    logo_yandex = [By.XPATH, '//a[contains(@class, "Header_LogoYandex")]']
    logo_scooter = [By.XPATH, '//a[contains(@class,"Header_LogoScooter")]']

    def __init__(self, driver):
        self.driver = driver
    def click_button(self, locator):
        self.driver.find_element(*locator).click()