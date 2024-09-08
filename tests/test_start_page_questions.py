from selenium import webdriver
from pages.start_page import HomePageSamokat


class TestStartPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_click_order_in_header_open_order_page(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        home_page = HomePageSamokat(self.driver)
        home_page.wait_for_load_logo()




    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
