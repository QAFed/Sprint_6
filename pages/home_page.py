from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePageSamokat:
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

    # def scroll_to_question(self):


    def check_answer_by_question(self, question, answer):
        question_locator = f'//div[contains(@id,"accordion__heading") and text()="{question}"]'
        question_element = self.driver.find_element(By.XPATH, question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, question_locator)))
        self.driver.find_element(By.XPATH, f'{question_locator}/parent::div/parent::div').click()
        answer_locator = [By.XPATH, f'{question_locator}/parent::div/parent::div/div/p']
        answer_text = self.driver.find_element(*answer_locator).text
        # print("ОЖИДАЕМЫЙ ОТВЕТ", answer)
        # print("ФАКТИЧЕСКИЙ ОТВЕТ", answer_text)
        assert answer_text == answer


    def check_answer_by_question(self, question, answer):
        question_locator = f'//div[contains(@id,"accordion__heading") and text()="{question}"]'
        question_element = self.driver.find_element(By.XPATH, question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, question_locator)))
        self.driver.find_element(By.XPATH, f'{question_locator}/parent::div/parent::div').click()
        answer_locator = [By.XPATH, f'{question_locator}/parent::div/parent::div/div/p']
        answer_text = self.driver.find_element(*answer_locator).text
        # print("ОЖИДАЕМЫЙ ОТВЕТ", answer)
        # print("ФАКТИЧЕСКИЙ ОТВЕТ", answer_text)
        assert answer_text == answer

    def check_answers_is_hidden(self, question):
        question_locator = f'//div[contains(@id,"accordion__heading") and text()="{question}"]'
        question_element = self.driver.find_element(By.XPATH, question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, question_locator)))
        answer_div_locator = [By.XPATH, f'{question_locator}/parent::div/parent::div/div/p/parent::div']
        answer_div = self.driver.find_element(*answer_div_locator)
        assert answer_div.get_attribute("hidden") is not None

    def check_answer_not_hidden_after_click(self, question):
        question_locator = f'//div[contains(@id,"accordion__heading") and text()="{question}"]'
        question_element = self.driver.find_element(By.XPATH, question_locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question_element)
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, question_locator)))
        self.driver.find_element(By.XPATH, f'{question_locator}/parent::div/parent::div').click()
        answer_div_locator = [By.XPATH, f'{question_locator}/parent::div/parent::div/div/p/parent::div']
        answer_div = self.driver.find_element(*answer_div_locator)
        assert answer_div.get_attribute("hidden") is None

    def click_zakazat(self, where):
        if where == "header":
            self.click_button_order_in_header()
        if where == "body":
            self.click_button_order_in_body()
