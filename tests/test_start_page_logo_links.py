import time

from selenium import webdriver
from pages.home_page import HomePageScooter
from pages.base_page import HeaderElements

class TestStartPage:

    def test_logo_yandex_click_go_to_dzen(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/order')
        header_elements = HeaderElements(driver)
        header_elements.click_button(header_elements.logo_yandex)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(2)
        assert "dzen.ru" in driver.current_url

    def test_logo_samokat_click_go_to_home_page(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/order')
        header_elements = HeaderElements(driver)
        header_elements.click_button(header_elements.logo_scooter)
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_logo()
        assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

