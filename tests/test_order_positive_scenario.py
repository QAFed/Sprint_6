import time

import pytest
from add_data.data_for_tests import UsersDataForOrder
from pages.order_page import OrderPage
from selenium import webdriver
class TestOrderPositive:

        driver = None

        @classmethod
        def setup_class(cls):
            cls.driver = webdriver.Firefox()

        @pytest.mark.parametrize('user_data_dict' , [UsersDataForOrder.user_1, UsersDataForOrder.user_2])

        def test_positive_order_scenario_start_to_click_button_in_header(self, user_data_dict):
            self.driver.get('https://qa-scooter.praktikum-services.ru/order')
            order_page = OrderPage(self.driver)
            order_page.wait_first_screen_user_data()
            order_page.set_user_data_on_first_screen_order(user_data_dict)
            order_page.click_dalee_button()
            order_page.set_user_data_on_second_screen_order(user_data_dict)
            order_page.click_zakazat_button()
            order_page.wait_confirm_popup()
            order_page.click_confirm_popup_button_yes()
            order_page.assert_popup_finish_is_present_with_number_of_order()
        @classmethod
        def teardown_class(cls):
            cls.driver.quit()
