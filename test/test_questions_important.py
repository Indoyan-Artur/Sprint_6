import allure
import pytest

from test_data.faq_cases import FAQ_CASES


class TestQuestionsImportant:
    @pytest.mark.parametrize("case", FAQ_CASES, ids=lambda c: c["id"])
    @allure.title("Проверка кнопок раздела Вопросы о важном")
    def test_faq_question_opens_answer(self, case, ready_home_page):
        ready_home_page.click_faq_question(case["heading"])
        text = ready_home_page.get_faq_answer_text(case["answer"])
        assert text == case["expected"], f"Текст ответа: {text}"

