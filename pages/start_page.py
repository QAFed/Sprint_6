from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePageSamokat:
    logo_yandex = [By.XPATH, '//a[contains(@class, "Header_LogoYandex")]']
    button_order_in_header = [By.XPATH, '//div[contains(@class, "Header_Nav")]/button[text()="Заказать"]']
    button_order_in_body = [By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]']

    def __init__(self, driver):
        self.driver = driver

    def wait_for_load_logo(self):
        WebDriverWait(self.driver,5).until(expected_conditions.visibility_of_element_located(self.logo_yandex))

    def click_button_order_in_header(self):
        self.driver.find_element(*self.button_order_in_header).click()

    def click_button_order_in_body(self):
        self.driver.find_element(*self.button_order_in_body).click()

    def scroll_to_question(self):
        

