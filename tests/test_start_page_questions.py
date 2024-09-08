import pytest
from selenium import webdriver
from pages.home_page import HomePageSamokat
from add_data.data_for_tests import QestAndAnswers

class TestStartPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('quest, answer', QestAndAnswers.div_list)
    def test_corresponds_answer_to_questions(self, quest, answer):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        home_page = HomePageSamokat(self.driver)
        home_page.wait_for_load_logo()
        home_page.check_answer_by_question(quest, answer)

    @pytest.mark.parametrize('quest', [x[0]for x in QestAndAnswers.div_list])
    def test_answers_is_hidden_by_default(self, quest):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        home_page = HomePageSamokat(self.driver)
        home_page.wait_for_load_logo()
        home_page.check_answers_is_hidden(quest)

    @pytest.mark.parametrize('quest',  [x[0]for x in QestAndAnswers.div_list])
    def test_answer_not_hidden_after_click(self, quest):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        home_page = HomePageSamokat(self.driver)
        home_page.wait_for_load_logo()
        home_page.check_answer_not_hidden_after_click(quest)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
