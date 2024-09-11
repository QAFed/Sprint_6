
from pages.order_page import OrderPage
class TestOrderPositive:

        driver = None

        @classmethod
        def setup_class(cls):
            cls.driver = webdriver.Firefox()

        def test_positive_order_scenario_start_to_click_button_in_header(self):
            self.driver.get('https://qa-scooter.praktikum-services.ru/order')
            order_page = OrderPage(self.driver)
            order_page.wait_first_screen_user_data()


            assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/order'

        @classmethod
        def teardown_class(cls):
            cls.driver.quit()
