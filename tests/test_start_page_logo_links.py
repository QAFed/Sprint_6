import time

from selenium import webdriver
from pages.home_page import HomePageSamokat
from pages.base_page import HeaderElements

class TestStartPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_logo_yandex_click_go_to_dzen(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        header_elements = HeaderElements(self.driver)
        header_elements.click_button(header_elements.logo_yandex)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        time.sleep(2)
        assert "dzen.ru" in self.driver.current_url

    def test_logo_samokat_click_go_to_home_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/order')
        header_elements = HeaderElements(self.driver)
        header_elements.click_button(header_elements.logo_samokat)
        home_page = HomePageSamokat(self.driver)
        home_page.wait_for_load_logo()
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
