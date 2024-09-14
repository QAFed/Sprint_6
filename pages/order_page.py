from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class OrderPage:
    header_first_screen_user_data = [By.XPATH, '//div[text()="Для кого самокат"]']
    name_input = [By.XPATH, '//input[@placeholder="* Имя"]']
    family_input = [By.XPATH, '//input[@placeholder="* Фамилия"]']
    address_input = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']
    metro_station_input = [By.XPATH, '//input[@placeholder="* Станция метро"]']
    tel_number_input = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']
    dalee_button = [By.XPATH, '//button[text()="Далее"]']
    header_second_screen_user_data = [By.XPATH, '//div[text()="Про аренду"]']
    date_delivery_input = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']
    rental_period_dropdown = [By.XPATH, '//div[@class="Dropdown-placeholder" and text()="* Срок аренды"]/parent::div/parent::div']
    black_samokat_checkbox = [By.XPATH, '//div[text()="Цвет самоката"]/parent::div//label[text()="чёрный жемчуг"]/input']
    grey_samokat_checkbox = [By.XPATH, '//div[text()="Цвет самоката"]/parent::div//label[text()="серая безысходность"]/input']
    comment_for_courier_input = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']
    zakazat_button = [By.XPATH, '//div[contains(@class,"Order_Buttons")]/button[text()="Заказать"]']
    confirm_popup_button_yes = [By.XPATH, '//button[text()="Да"]']
    header_confirm_popup = [By.XPATH, '//div[text()="Хотите оформить заказ?"]']
    header_finish_order_poup = [By.XPATH, '//div[text()="Заказ оформлен"]']
    message_finish_order_poup = [By.XPATH, '//div[contains(@class,"Order_Text")]']
    cookie_button = [By.XPATH, '//button[contains(@class,"App_CookieButton")]']

    def __init__(self, driver):
        self.driver = driver

    def wait_first_screen_user_data(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.header_first_screen_user_data))

    def insert_name_into_input(self, name):
        self.driver.find_element(*self.name_input).send_keys(name)

    def insert_family_into_input(self, family):
        self.driver.find_element(*self.family_input).send_keys(family)

    def insert_address_into_input(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    def choice_metro_station(self, metro):
        metro_locator = [By.XPATH, f'//div[text()="{metro}"]']
        self.driver.find_element(*self.metro_station_input).click()
        self.driver.find_element(*self.metro_station_input).send_keys(metro)
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(metro_locator))
        self.driver.find_element(*metro_locator).click()

    def insert_tel_number_into_input(self, tel_number):
        self.driver.find_element(*self.tel_number_input).send_keys(tel_number)

    def click_dalee_button(self):
        self.driver.find_element(*self.dalee_button).click()

    def wait_second_screen_user_data(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.header_second_screen_user_data))

    def insert_date_delivery_into_input(self, date_delivery):
        self.driver.find_element(*self.date_delivery_input).send_keys(date_delivery)

    def rental_period_dropdown_choice(self, period):
        period_locator = [By.XPATH, f'//div[contains(@class,"Dropdown-option") and text()="{period}"]']
        # period_locator = [By.XPATH, '//div[contains(@class,"Dropdown-option") and text()="сутки"]']
        self.driver.find_element(*self.rental_period_dropdown).click()
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(period_locator))
        self.driver.find_element(*period_locator).click()

    def black_color_saomkat_choice(self):
        self.driver.find_element(*self.black_samokat_checkbox).click()

    def grey_color_saomkat_choice(self):
        self.driver.find_element(*self.grey_samokat_checkbox).click()

    def insert_comment_for_courier_input(self, comment_for_courier):
        self.driver.find_element(*self.comment_for_courier_input).send_keys(comment_for_courier)

    def click_zakazat_button(self):
        self.driver.find_element(*self.zakazat_button).click()

    def wait_confirm_popup(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.header_confirm_popup))

    def click_confirm_popup_button_yes(self):
        self.driver.find_element(*self.confirm_popup_button_yes).click()

    def assert_popup_finish_is_present_with_number_of_order(self):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(self.message_finish_order_poup))
        text_message = self.driver.find_element(*self.message_finish_order_poup).text
        assert "Номер заказа" in text_message

    def set_user_data_on_first_screen_order(self, user_data_dict):
        self.insert_name_into_input(user_data_dict['name'])
        self.insert_family_into_input(user_data_dict['family'])
        self.insert_address_into_input(user_data_dict['address'])
        self.choice_metro_station(user_data_dict['metro'])
        self.insert_tel_number_into_input(user_data_dict['tel_number'])

    def set_user_data_on_second_screen_order(self, user_data_dict):
        self.insert_date_delivery_into_input(user_data_dict['date_delivery'])
        if user_data_dict['color'] == "черный":
            self.black_color_saomkat_choice()
        if user_data_dict['color'] == "серый":
            self.black_color_saomkat_choice()
        self.insert_comment_for_courier_input(user_data_dict['comment_for_courier'])
        self.rental_period_dropdown_choice(user_data_dict['rental_period'])

    def accept_cookie(self):
        try:
            WebDriverWait(self.driver, 1).until(
                expected_conditions.visibility_of_element_located(self.cookie_button))
            self.driver.find_element(*self.cookie_button).click()
        except (TimeoutException, NoSuchElementException):
            pass

