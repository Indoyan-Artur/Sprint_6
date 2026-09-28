import pytest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import HomePage

BASE_URL = "https://qa-scooter.education-services.ru/"

class TestQuestionsImportant:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(BASE_URL)
        cls.wait = WebDriverWait(cls.driver, 20)
        cls.home_page = HomePage(cls.driver)

    def scroll_page(self):
        scroll = self.driver.find_element(*self.home_page.cost_of_scooter)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll)   

    FAQ_CASES = [
        {
            "id": "cost_and_payment",
            "heading": "cost_of_scooter",
            "answer": "answer_cost_of_scooter",
            "expected": "Сутки — 400 рублей. Оплата курьеру — наличными или картой.",
        },
        {
            "id": "several_scooters",
            "heading": "several_scooters",
            "answer": "answer_several_scooters",
            "expected": "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.",
        },
        {
            "id": "time_calculation",
            "heading": "time_calculation",
            "answer": "answer_time_calculation",
            "expected": "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.",
        },
        {
            "id": "order_scooter_today",
            "heading": "order_scooter_today",
            "answer": "answer_order_scooter_today",
            "expected": "Только начиная с завтрашнего дня. Но скоро станем расторопнее.",
        },
        {
            "id": "extend_return_earlier",
            "heading": "extend_return_earlier",
            "answer": "answer_extend_return_earlier",
            "expected": "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.",
        },
        {
            "id": "charging_and_scooter",
            "heading": "charging_and_scooter",
            "answer": "answer_charging_and_scooter",
            "expected": "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.",
        },
        {
            "id": "cancel_the_order",
            "heading": "cancel_the_order",
            "answer": "answer_cancel_the_order",
            "expected": "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.",
        },
        {
            "id": "bring_beyond_mkad",
            "heading": "bring_beyond_mkad",
            "answer": "answer_bring_beyond_mkad",
            "expected": "Да, обязательно. Всем самокатов! И Москве, и Московской области.",
        },
    ]

    @pytest.mark.parametrize("case", FAQ_CASES, ids=lambda c: c["id"])
    @allure.title("Проверка кнопок раздела Вопросы о важном")
    def test_faq_question_opens_answer(self, case):
        self.scroll_page()
        self.wait.until(EC.element_to_be_clickable(getattr(self.home_page, case["heading"]))).click()
        text = self.wait.until(EC.visibility_of_element_located(getattr(self.home_page, case["answer"]))).text
        assert text == case["expected"], f"Текст ответа: {text}"

