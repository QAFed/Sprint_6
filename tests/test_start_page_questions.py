import pytest
from pages.home_page import HomePageScooter
from add_data.data_for_tests import QestAndAnswers

class TestStartPage:

    @pytest.mark.parametrize('quest, answer', QestAndAnswers.div_list, ids=lambda val: val[0])
    def test_corresponds_answer_to_questions(self, driver, quest, answer):
        driver.get(HomePageScooter.get_url_page())
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_logo()
        home_page.check_answer_by_question(quest, answer)

    @pytest.mark.parametrize('quest', [x[0]for x in QestAndAnswers.div_list], ids=lambda val: val[0])
    def test_answers_is_hidden_by_default(self, driver, quest):
        driver.get(HomePageScooter.get_url_page())
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_logo()
        home_page.check_answers_is_hidden(quest)

    @pytest.mark.parametrize('quest',  [x[0]for x in QestAndAnswers.div_list], ids=lambda val: val[0])
    def test_answer_not_hidden_after_click(self, driver, quest):
        driver.get(HomePageScooter.get_url_page())
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_logo()
        home_page.check_answer_not_hidden_after_click(quest)

